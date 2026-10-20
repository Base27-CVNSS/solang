# Bắt đầu với máy tính cá nhân

## Cài đặt

Cài Git, VS Code, Node.js LTS, Solana CLI và Solang compiler theo hướng dẫn chính thức. Có binary cho Linux/macOS/Windows hoặc Docker image.

- https://solang.readthedocs.io/en/latest/installing.html
- https://solang.readthedocs.io/en/latest/running.html
- https://solana.com/docs

```bash
solang --version
solang compile --help
solana --version
solana config get
```

## Build đầu tiên

```bash
mkdir -p build
solang compile --target solana -v -o build examples/Flipper.sol
```

Xem thông tin compiler về data account; kiểm tra metadata JSON tạo ra cho instruction, accounts, discriminator và bản .so. File được sinh ra có thể khác tên tùy contract/tool version.

## Local validator

Chạy `solana-test-validator` trên terminal riêng. Terminal khác: `solana config set --url localhost`, `solana config get`, rồi deploy thử. Không lấy ví mainnet để chạy bài lab. Tạo data accounts và client sau khi nắm IDL.

**Trên Windows**: binary Windows hoặc Docker/WSL2. **Trên macOS**: Homebrew tap `hyperledger/solang/solang`. Ghi đúng phiên bản tại mỗi lab.
