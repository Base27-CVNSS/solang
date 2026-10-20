import "solana";
contract AccountLab {
    @account(readMe)
    @signer(authority)
    @mutableAccount(output)
    function inspect() external view returns (address) {
        assert(tx.accounts.authority.is_signer);
        return tx.accounts.readMe.key;
    }
}
