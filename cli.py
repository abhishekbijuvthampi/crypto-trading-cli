import argparse

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

def checkCMD(account, order):
    if args.command == 'account':
        if args.asset:
            account.show_asset(args.asset)

    elif args.command == 'trades':
        if args.side == 'BUY':
            order.market_buy(args.symbol, 
                args.quantity)
        elif args.side == 'SELL':
            order.market_sell(args.symbol, 
                args.quantity)
