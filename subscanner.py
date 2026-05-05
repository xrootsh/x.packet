import requests
from colorama import Fore, Style, init

# Initialize colors
init(autoreset=True)

def request(url):
    try:
        return requests.get("http://" + url, timeout=3)
    except:
        pass

def start_scanner():
    print(Fore.CYAN + Style.BRIGHT + """
    ✖️🔴PACKET SUBDOMAIN SCANNER
    ---------------------------
    """)
    
    target = input(Fore.YELLOW + "[+] Target URL (e.g. google.com): ").strip()
    wordlist = ["www", "mail", "dev", "admin", "test", "api", "blog", "vpn"]

    print(Fore.BLUE + f"[*] Scanning {target}...\n")
    
    for word in wordlist:
        test_url = word + "." + target
        response = request(test_url)
        if response:
            print(Fore.GREEN + f"[+] Found: {test_url} (Code: {response.status_code})")

if __name__ == "__main__":
    start_scanner()
