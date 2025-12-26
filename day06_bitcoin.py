import sys
import requests
import json

def main():
    buying_price = cli_input()
    current_price = real_time_bitcoin_price()
    difference = current_price - buying_price
    if difference > 0:
        print(f"current price ${current_price:,.2f} and profit ${difference:,.2f}")
    if difference < 0:
        print(f"current price ${current_price:,.2f} and loss ${difference * -1:,.2f}")
    if difference == 0:
        print(f"current price ${current_price:,.2f} and no loss/profit")    

def cli_input():
    if len(sys.argv) != 2:
        sys.exit("too many arguments")
    else:
        try:
            value = float(sys.argv[1].strip())
            return value
        except ValueError:
            sys.exit("numbers only!")

def real_time_bitcoin_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response_from_web = requests.get(url).json()
        btcn = response_from_web['bitcoin']
        currnt_prce = btcn['usd']
        return float(currnt_prce)
    except:
        sys.exit("Try again later!")

main()
