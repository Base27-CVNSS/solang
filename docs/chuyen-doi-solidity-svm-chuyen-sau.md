# Cẩm nang chuyển Solidity / Ethereum sang Solang / Solana — hướng dẫn thực chiến

> Phạm vi: Solidity được biên dịch bằng Solang target Solana. Không phải mọi contract Ethereum đều biên dịch hoặc vận hành nguyên trạng. Các ví dụ ở đây cần tự chạy với phiên bản compiler đã cài. Nguồn tham chiếu: https://solang.readthedocs.io/en/latest/targets/solana.html.

## Bước 1 — Tách 5 lớp của hợp đồng Ethereum

Đối với một contract Solidity đã có, hãy phân loại: (1) logic nghiệp vụ thuần; (2) trạng thái lưu trữ; (3) danh tính và phân quyền; (4) chuyển tiền/token; (5) kết nối hợp đồng khác. Phần (1) thường có thể tái sử dụng nhiều hơn; (2)–(5) phải thiết kế lại theo account model.

Ví dụ hệ thống điểm thưởng ERC-20 trên Ethereum: contract giữ balances, totalSupply, quyền mint/burn. Trên Solana, **SPL Token Program** đã giải quyết luồng token chuẩn; chương trình riêng nên chỉ giữ business rules cần thiết. Không coi việc copy/paste hợp đồng ERC-20 thành một SPL token.

## Bước 2 — Vẽ lại account model

Một chương trình có Program ID và có thể có nhiều data accounts. Lập bảng sau **trước khi code**:

| Account | Ai tạo | Owner | Signer | Writable | Dữ liệu |
|---|---|---|---|---|---|
| Program | CLI deploy | Loader | Không trong instruction thường | Không | Binary SBF |
| Record PDA | Client/Program | Chương trình của bạn | PDA ký qua seeds khi cần | Khi ghi | Owner, hash, nonce, version |
| Authority wallet | Người dùng | System Program thông thường | Khi cần auth | Tùy giao dịch | Public key và lamports |
| System Program | Runtime | Hệ thống | Không | Không | Tạo/chuyển tài khoản |
| Token Program | Cluster | Hệ thống | Không | Không | Thực thi token ops |

Những dòng trên là thiết kế mẫu, không phải IDL bắt buộc. IDL thật do compiler xác định danh sách và order.

## Bước 3 — Thay mẫu msg.sender, msg.value, payable

**Ví dụ EVM:**
```solidity
address public owner;
function update() external {
    require(msg.sender == owner, "forbidden");
}
```

**Chuyển đổi tư duy Solang:**
```solidity
import "solana";
contract Registry {
    address authority;

    constructor(address initialAuthority) {
        authority = initialAuthority;
    }

    @signer(admin)
    function update() external {
        assert(tx.accounts.admin.is_signer);
        assert(tx.accounts.admin.key == authority);
        // write state after successful authorization
    }
}
```

- `@signer` mô tả account bắt buộc ký; kiểm tra key chống dùng chữ ký của tài khoản bất kỳ.
- `msg.value` không hỗ trợ trên target Solana. Việc client khai báo đã chuyển tiền không có giá trị chứng minh: nếu ứng dụng yêu cầu nạp tiền, thực hiện/kiểm tra chuyển SOL thực và invariant của transaction.
- `receive()` không có cùng ngữ nghĩa; token SPL cũng không được coi là token ERC-20.

## Bước 4 — Lựa chọn PDA, account space và lifecycle

Dùng seed có namespace để tránh xung đột (ví dụ `"record"`, public key owner và định danh bản ghi). Xác thực PDA derivation trên client và on-chain, ngăn client thay record khác. Với data account được tạo on-chain, các annotation `@payer`, `@space`, `@seed`, `@bump` cần tương thích cú pháp và thứ tự input của compiler version.

```solidity
@space(512)
@payer(payer)
constructor(@seed bytes recordId, @bump bytes1 bump) {
    // Constructor ví dụ, yêu cầu data-account lifecycle hợp lệ.
}
```

Đừng copy con số 512 thành kích thước luôn đúng: chạy `solang compile --target solana -v ...`, đọc kích thước compiler báo và tính phí rent theo cluster.

## Bước 5 — Biên dịch và đọc IDL

```bash
solang --version
mkdir -p build
solang compile --target solana -v -o build examples/AuthorityCounter.sol
```

Kiểm tra thực tế: instruction name và discriminator, danh sách accounts, signer/writable flags, constructor, arguments/types. Nếu dùng JS/Anchor client, **tên hàm có thể được camelCase** và một số kiểu số dùng BN tùy SDK. Đọc tài liệu của phiên bản package đang dùng.

## Bước 6 — Tạo client mới, không tái dùng EVM ABI

Luồng client là: chọn cluster → tải IDL đã sinh → xác minh program ID → tạo instruction data qua codec tương ứng → truyền AccountMeta theo IDL → chữ ký hợp lệ → simulation → send → confirm → đọc state. Pseudocode:

```typescript
// Pseudocode, KHÔNG chạy độc lập:
const idl = loadValidatedIDL();
const accounts = buildAccountMetasFromIDL(idl, userInputs);
assertKnownProgramId(programId);
assertExpectedSignerAndPda(accounts);
const transaction = buildTransaction(idl, accounts, args);
const simulated = await simulate(transaction);
assertNoRuntimeError(simulated);
const signature = await signAndSend(transaction);
await confirmAndReadBack(signature);
```

Trong quy trình kiểm thử, tránh chỉ dựa vào `isSigner` hoặc `isWritable` do client đưa vào. Runtime và logic on-chain phải xác minh bằng nguồn tin cậy.

## Bước 7 — Kiểm thử an ninh trước khi tối ưu

Test âm tính cho: sai authority, account giả/owner sai, thiếu signer, account read-only, sai thứ tự, PDA sai seeds, program ID CPI bị thay, overflow, data layout V1 vs V2. Sau đó chạy benchmark CU trên cùng workload, không coi CU bằng gas theo tỷ lệ cố định.

## Bước 8 — Triển khai có kiểm soát

Local validator → Devnet → review code/IDL/binary → Mainnet chỉ sau khi có quy trình khóa, quyền nâng cấp, kiểm toán, kế hoạch sự cố. Không xóa upgrade authority nếu chưa xác định rõ ràng cơ chế governance.

### Ma trận kiểm tra hoàn thành chuyển đổi

| Đầu mục | Yêu cầu |
|---|---|
| Compile | Có tệp SBF .so và IDL chính xác, ghi version |
| Account model | Rõ ownership, lifecycle, signer, writable, PDA seeds |
| Access | Mọi phương thức nhạy cảm đều có invariant auth |
| Client | Không dùng ethers EVM ABI cho Solana target |
| Test | Happy path, fail path, rollback, account substitution |
| Deploy | Program ID và quyền nâng cấp đã kiểm kê |
| Monitoring | Transaction signature, logs, state sau confirm |
| Security | Không có private key thật trong repo hoặc website |
