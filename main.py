import time
import sys
from solathon import Client, Transaction, Account
from solathon.core.instructions import Transfer

# Check if sufficient arguments are provided
if len(sys.argv) < 3:
    print("Usage: python script.py <CONTRACT_ADDRESS> <PRIVATE_KEY_1> [<PRIVATE_KEY_2> ...]")
    sys.exit(1)

# Get contract address and wallet keys from console arguments
contract_address = sys.argv[1]
wallet_keys = sys.argv[2:]

# Connect to Solana cluster
client = Client("https://api.mainnet-beta.solana.com")

# Define buy amounts and cycles
buy_amounts = [0.01, 0.02, 0.01, 0.03, 0.01]  # Example buy amounts

def perform_transactions(wallet_key):
    wallet = Account(wallet_key)
    for amount in buy_amounts:
        try:
            # Create a transfer transaction to simulate a buy
            txn = Transaction()
            transfer_instruction = Transfer(
                source=wallet.public_key,
                destination=contract_address,
                amount=int(amount * 10**9)
            )
            txn.add(transfer_instruction)

            # Send the transaction
            response = client.send_transaction(txn, wallet)
            print(f"Buy {amount} SOL: {response}")

            # Wait for confirmation
            time.sleep(15)
        except Exception as e:
            print(f"Error during buy transaction: {e}")

    try:
        # After buying cycle, simulate a sell (transfer all to contract address)
        balance = client.get_balance(wallet.public_key)["result"]["value"]
        sell_amount = balance - 5000  # Keep some lamports to cover fees

        if sell_amount > 0:
            txn = Transaction()
            transfer_instruction = Transfer(
                source=wallet.public_key,
                destination=contract_address,
                amount=sell_amount
            )
            txn.add(transfer_instruction)

            # Send the transaction
            response = client.send_transaction(txn, wallet)
            print(f"Sell {sell_amount / 10**9}} SOL: {response}")

            # Wait for confirmation
            time.sleep(15)
        else:
            print("Not enough balance to sell.")
    except Exception as e:
        print(f"Error during sell transaction: {e}")

# Main loop to run transactions for each wallet
while True:
    for wallet_key in wallet_keys:
        perform_transactions(wallet_key)
        # Add a delay between each wallet instance to avoid nonce issues
        time.sleep(30)
