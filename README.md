# Automated On-Chain Trading Script

This project is a Python script that performs automated trading on the Solana blockchain using the `solathon` library. The script interacts with a specific contract address, executes multiple buy and sell transactions in a loop, and supports running instances for multiple wallets concurrently.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Features](#features)
- [Requirements](#requirements)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/solana-trading-script.git
    cd solana-trading-script
    ```

2. Install the required Python libraries:
    ```bash
    pip install solathon
    ```

## Usage

To run the script, you need to provide the contract address and wallet private keys as console arguments.

```bash
python main.py <CONTRACT_ADDRESS> <PRIVATE_KEY_1> <PRIVATE_KEY_2> 

```

## Configuration

```
The script uses the following configuration:

Contract Address: The Solana contract address you want to interact with.
- Wallet Private Keys: Private keys of the Solana wallets you want to use for trading.
- Buy Amounts: Amounts of SOL to buy in each cycle (defined in the script).
- Cycle Delays: Delays between transaction cycles to ensure transaction confirmations.

```


### Buy Amounts
``` 
The script includes an example list of buy amounts. You can modify these values in the script as needed:


buy_amounts = [0.01, 0.02, 0.01, 0.03, 0.01]  # Example buy amounts

```

## Features

```
- Automated Trading: Executes buy and sell transactions in a loop.
- Multi-Wallet Support: Runs concurrently for multiple wallets.
- On-Chain Transactions: Uses Solana's blockchain for all transactions.
- Customizable Buy Amounts: Easily modify the buy amounts and cycles.

```

## Requirements

```
- Python 3.6 or higher

- solathon library
```


## License

```
This project is licensed under the MIT License. See the LICENSE file for details.

```
