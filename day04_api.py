import requests
from colorama import init, Fore, Style

init()

def get_bitcoin_price():
    # SWITCHING TARGETS: Using CoinGecko instead of CoinDesk
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # New Data Structure: {'bitcoin': {'usd': 96000}}
        price = data['bitcoin']['usd']
        
        return price
    except Exception as e:
        print(f"⚠️ DEBUG INFO: {e}")
        return "Error"

def main():
    print("⏳ Connecting to the Global Financial Network...")
    
    price = get_bitcoin_price()
    
    if price == "Error":
        print(Fore.RED + "❌ Failed to fetch data." + Style.RESET_ALL)
    else:
        # 5. Display the Prize
        print(Fore.GREEN + f"💰 Current Bitcoin Price: ${price}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()