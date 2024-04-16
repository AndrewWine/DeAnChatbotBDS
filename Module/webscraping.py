import requests
import json

url = 'https://muaban.net/bat-dong-san/ha-noi'
username = 'vietanhls113'
apiKey = 'RKnDq5Q4MeFSUDN8K6kMWbW8E'

apiEndPoint = "http://api.scraping-bot.io/scrape/raw-html"

options = {
    "useChrome": False,  # Set to True if you want to use headless Chrome for JavaScript rendering.
    "premiumProxy": False,  # Set to True if you want to use premium proxies.
    "proxyCountry": None,  # Allows you to choose a country proxy (example: proxyCountry: "FR").
    "waitForNetworkRequests": False  # Wait for most Ajax requests to finish until returning the HTML content.
}

payload = json.dumps({"url": url, "options": options})
headers = {
    'Content-Type': "application/json"
}

response = requests.request("POST", apiEndPoint, data=payload, auth=(username, apiKey), headers=headers)

# Save response text to a file
with open('response_data.txt', 'w', encoding='utf-8') as file:
    file.write(response.text)

print("Response saved to 'response_data.txt'")
