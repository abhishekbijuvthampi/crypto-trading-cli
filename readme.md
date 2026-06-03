# CLI-based crypto trading system

A CLI-based trading bot that interacts with Binance Testnet API to place trades and manage account data.

## Structue
```
Testing_bot/
|
|---config/
|   |
|   |---.env
|   |---settings.py
|
|---data/
|   |
|   |---app.log
|   |---logging_config.py
|   |---market_data.py
|
|---execution
|   |
|   |---account.py
|   |---orders.py
|
|---.gitignore
|
|---cli.py
|
|---main.py
|
|---README.md
|
|---requirements.txt
```

## Features
* Place Market and Limit orders on Binance Futures Testnet.
* Accepts and validates user input via CLI(argparse).
* Shows Current Account Assets.
* Logging of API requests and responses in log file.

## Installation
Clone this repository:
```bash 
git clone <your-repo-link> 
cd trading-bot
```
Install dependencies: 
```bash
pip install -r requirements.txt
```

Set up your API Keys in environment variables before running the application.

### How to generate Binance API keys
Using Binance Futures Testnet 

Setup:-

    - Register and activate a Binance Futures Testnet account(https://testnet.binance.vision/).
    - Log In with GitHub
    - Generate API credentials.
    - Copy API key, Secret key.
    - Rename .env.example to .env
    - Paste API key, Secret key there.

## Usage

### View Account Assets

```bash
python main.py account --asset <asset_symbol>
```
or
```bash
python main.py account -a <asset_symbol>
```

### Viw Activity Logs

```bash
python main.py account --logs
```
or
```bash
python main.py account -l
```

### Place a market order

```bash
python main.py trade market -p <PAIR> <side> <quantity>
```
Example:

```bash
python main.py trade market -p BTCUSDT b 0.01
```

### Place a limit order

```bash
python main.py trade limit -p <PAIR> <side> <quantity> <price>
```
Example:

```bash
python main.py trade limit -p BTCUSDT b 0.01 66939
```

## Technologies Used
- Python
- pandas
- python
- arparse
- logging
- python-dotenv
- os


## Author

Abhishek Biju V Thampi

- GitHub: https://github.com/abhishekbijuvthampi
- LinkedIn: https://www.linkedin.com/in/abhishekbijuvthampi