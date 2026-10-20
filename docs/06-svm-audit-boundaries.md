# So sánh công cụ Audit EVM và Solang/Solana SBF

| Tool | Dùng tốt cho EVM | KHÔNG mặc nhiên bao phủ trên Solang SBF | Phương án Solang |
|---|---|---|---|
| Foundry / Forge | Unit/fuzz/stateful invariant, EVM test | Runtime Solana, account owner, CPI, compute units | Compile Solang + chạy test trên local validator |
| Slither | Solidity/Vyper static analysis qua toolchain EVM | Binary SBF, runtime owner/program semantics | Review Solang annotations, IDL và account validators |
| Echidna / Medusa | Ethereum-based property/coverage fuzz | Không chạy trực tiếp account model SVM | Custom tests dữ liệu account với validator |
| Halmos | Bounded symbolic testing EVM bytecode | Proof không chuyển đổi thành proof SBF | Tách spec/assumptions và test SBF độc lập |
| Certora | Rule-based proof theo phiên bản/target được hỗ trợ | Không giả định có support Solang/SBF | Kiểm tra hỗ trợ chính thức rồi mới nêu bằng chứng |
| Manual review | Logic, incentives, adversarial interaction | Có thể chuyển tư duy, không copy runtime assumptions | Soát PDA, signer, owner, writable, CPI, mint, upgrade |

**Checklist SBF:** verify program ID, signer pubkey đúng authority, PDA seeds+bump, data owner/schema, mutable/writable, account metas theo IDL, CPI program ID, mint/token account, address 32 byte, số fixed-point, storage layout/space, upgrade authority, compute budget, logs và state readback.

**Hai lớp bằng chứng:** bất biến kinh tế có thể kiểm tra trên mô hình/contract EVM độc lập; nhưng hành vi permission và execution của hợp đồng Solang chạy trên SBF phải được kiểm tra trong runtime Solana tương ứng. Tuyên bố “EVM tests pass” không đủ để nhận “Solang security audit pass”.

Nguồn: https://solang.readthedocs.io/en/latest/targets/solana.html ; https://github.com/crytic/slither ; https://github.com/crytic/echidna ; https://github.com/crytic/medusa ; https://github.com/a16z/halmos ; https://docs.certora.com/ ; https://solana.com/docs
