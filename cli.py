import argparse
from execution.account import Account

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

def checkCMD(account):
    if args.command == 'account':
        if args.asset:
            account.show_asset(args.asset)