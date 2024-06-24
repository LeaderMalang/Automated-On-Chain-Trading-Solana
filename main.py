import time
import sys
from solathon import Client, Transaction, PublicKey, Keypair
from solathon.core.instructions import transfer

# Check if sufficient arguments are provided
if len(sys.argv) < 3:
    print("Usage: python main.py <CONTRACT_ADDRESS> <PRIVATE_KEY_1> [<PRIVATE_KEY_2> ...]")
    sys.exit(1)

# Get contract address and wallet keys from console arguments
arg_contract_address=sys.argv[1]
arg_wallet_keys=sys.argv[2:]
contract_address = PublicKey(arg_contract_address)
wallet_keys = arg_wallet_keys

# Connect to Solana cluster
client = Client("https://api.mainnet-beta.solana.com")

# Define buy amounts and cycles
buy_amounts = [0.01, 0.02]  # Example buy amounts

def perform_transactions(wallet_key):
    wallet = Keypair().from_private_key(wallet_key)
    for amount in buy_amounts:
        try:
            # Create a transfer transaction to simulate a buy
            
            instruction  = transfer(
                from_public_key=wallet.public_key,
                to_public_key=contract_address,
                lamports=int(amount * 10**9)
            )
            transaction  = Transaction(instructions=[instruction], signers=[wallet])

            # Send the transaction
            response = client.send_transaction(transaction)
            print(f"Buy {amount} SOL: {response}")

            # Wait for confirmation
            time.sleep(15)
        except Exception as e:
            print(f"Error during buy transaction: {e}")

    try:
        # After buying cycle, simulate a sell (transfer all to contract address)
        balance = client.get_balance(wallet.public_key)
        sell_amount = balance - 5000  # Keep some lamports to cover fees

        if sell_amount > 0:
            
            sell_instruction = transfer(
                from_public_key=wallet.public_key,
                to_public_key=contract_address,
                lamports=sell_amount
            )
            sell_transaction  = Transaction(instructions=[sell_instruction], signers=[wallet])

            # Send the transaction
            sell_response = client.send_transaction(sell_transaction)
            print(f"Sell {sell_amount / 10**9} SOL: {sell_response}")

            # Wait for confirmation
            time.sleep(15)
        else:
            print("Not enough balance to sell.")
    except Exception as e:
        print(f"Error during sell transaction: {e}")

# Main loop to run transactions for each wallet
if __name__ == "__main__":
    for wallet_key in wallet_keys:
            perform_transactions(wallet_key)
            # Add a delay between each wallet instance to avoid nonce issues
            time.sleep(30)
