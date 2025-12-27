import sys
import requests

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python day07_sentinel.py <url1> <url2> ...")
    else:
        urls = sys.argv[1:]
        for url in urls:
            check_status(url)

def check_status(url):
    if not url.startswith("http"):
        targer_url = f"https://{url}"
    else:
        targer_url = url
    try:
        response = requests.get(targer_url, timeout=3)
        if response.status_code == 200:
            print(f"✅ {url} is ONLINE")
        else:
            print(f"⚠️ {url} returned status: {response.status_code}")
    except requests.RequestException:
        print(f"❌ {url} is DOWN (Connection Error)")

if __name__ == "__main__":
    main()