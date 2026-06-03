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

def add_common_args(p):
    p.add_argument(
        'side', 
        choices=['b', 's'],
        help="choose : 'b' (buy), 's' (sell) "
        )
    p.add_argument(
        '-p',
        '--pair', 
        type=str,
        help="Trading Pair",
        required=True
        )
    p.add_argument(
        'quantity',
        type=float,
        help="quantity of the trade"
        )


# Subcommand Trade
parser_trade = subparsers.add_parser(
    "trade",
    help="to Trade"
    )

subparsers_trade = parser_trade.add_subparsers(dest="subcommand")

#market buy/sell
market_trade = subparsers_trade.add_parser(
    "market",
    help="For market BUY/SELL")
add_common_args(market_trade)

#limit buy/sell
limit_trade = subparsers_trade.add_parser(
    "limit",
    help="For limit BUY/SELL")
add_common_args(limit_trade)
limit_trade.add_argument(
    'price', 
    help="Price when the trade should be executed."
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
    
    elif args.command == 'trade':
        if args.subcommand == 'market':
            if args.side == 'b':
                info = order.market_buy(args.pair, 
                    args.quantity)
        
            elif args.side == 's':
                info = order.market_sell(args.pair, 
                    args.quantity)
                
        if args.subcommand == 'limit':
            if args.side == 'b':
                info = order.limit_buy(args.pair, 
                    args.quantity, args.price)
        
            elif args.side == 's':
                info = order.limit_sell(args.pair, 
                    args.quantity, args.price)
        
    # logger.info(info)

    df = pd.Series(info)
    logger.info(df)
    
    return df 
    
