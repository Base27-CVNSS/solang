# Bài lab Solidity → Solang

Ví dụ minh họa cần tự biên dịch và kiểm tra IDL.

```bash
mkdir -p build
solang --version
solang compile --target solana -v -o build examples/Flipper.sol
solang compile --target solana -v -o build examples/AuthorityCounter.sol
solang compile --target solana -v -o build examples/AccountLab.sol
```

Lưu ý: repository chưa có compiler runner, unit tests tự động hoặc deployment; chỉ compile thành công chưa đủ deploy. Với target Solana còn cần data account, IDL, signer và client.
