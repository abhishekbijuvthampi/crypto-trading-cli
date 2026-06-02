import argparse

parser = argparse.ArgumentParser(
    description="Trading Bot CLI"
    )

subparsers = parser.add_subparsers(dest="command")

parser_account = subparsers.add_parser(
    "account",
    help="To Account Details"
    )
parser_account.add_argument(
    '-a', 
    '--asset', 
    type=str, 
    help='To Check Asset (eg: BTC, USDT, BNB)'
    )
parser_account.add_argument(
    '-l',
    '--log',
    action='store_false'
    )



args = parser.parse_args()