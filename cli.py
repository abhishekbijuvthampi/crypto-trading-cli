import argparse
import pandas as pd
from data.logging_config import get_logger

parser = argparse.ArgumentParser(
    description="Trading Bot CLI"
    )

subparsers = parser.add_subparsers(dest="command")


# Subcommand Acoount
parser_account = subparsers.add_parser(
    "account",
    help="to Account Details"
    )
parser_account.add_argument(
    '-a', 
    '--asset', 
    type=str, 
    help='to Check Asset (eg: BTC, USDT, BNB)'
    )
parser_account.add_argument(
    '-l',
    '--log',
    help="show account logs",
    action='store_true'
    )


# Subcommand Trade
parser_trade = subparsers.add_parser(
    "trades",
    help="to Trade in Market"
    )
parser_trade.add_argument(
    '-sb',
    '--symbol', 
    type=str,
    help="symbol to place Trade",
    required=True
    )
parser_trade.add_argument(
    '-s',
    '--side', 
    choices=['BUY', 'SELL'],
    help="choose : BUY or SELL (CAPS)",
    required=True
    )
parser_trade.add_argument(
    'quantity',
    type=float,
    help="quantity of the trade"
    )

args = parser.parse_args()

logger = get_logger()


def checkCMD(account, order):
    if args.command == 'account':
        if args.asset:
            info = account.show_asset(args.asset)
        
        elif args.log:
            with open("data/app.log", "r") as f:
                for line in f:
                    print(line.strip())
            info  = "Checked Log info"
    
    elif args.command == 'trades':
        if args.side == 'BUY':
            info = order.market_buy(args.symbol, 
                args.quantity)
        
        elif args.side == 'SELL':
            info = order.market_sell(args.symbol, 
                args.quantity)

    logger.info(info)
    
