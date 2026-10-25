import requests

SECURITY_HEADERS = {
    "Content-Security-Policy": "Controls allowed content",
    "Strict-Transport-Security": "Encourages HTTPS",
    "X-Content-Type-Options": "Helps prevent MIME sniffing",
    "X-Frame-Options": "Helps reduce clickjacking",
    "Referrer-Policy": "Controls referrer information",
}

def scan_website(url):
    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    print("\nScanning:", url)
    print("-" * 45)

    try:
        response = requests.get(url, timeout=10)
        print("HTTP Status:", response.status_code)

        present = 0

        for header, explanation in SECURITY_HEADERS.items():
            if response.headers.get(header):
                print("[PRESENT]", header)
                present += 1
            else:
                print("[MISSING]", header)

        print("-" * 45)
        print("Headers present:", present, "of", len(SECURITY_HEADERS))
        print("Headers missing:", len(SECURITY_HEADERS) - present)

    except requests.RequestException as error:
        print("Error:", error)

if __name__ == "__main__":
    url = input("Enter a website URL: ").strip()
    if url:
        scan_website(url)
    else:
        print("Please enter a URL.")

