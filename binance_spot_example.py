import requests
import json

# Binance API endpoint
api_endpoint = "https://api.binance.com"

# Your Binance API key and secret
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

# OCO order details
symbol = "BTCUSDT"
stop_loss_price = "55000"
take_profit_price = "60000"
quantity = "0.01"

# Create the request headers
headers = {
    "X-MBX-APIKEY": api_key
}

# Create the request payload
data = {
    "symbol": symbol,
    "side": "SELL",
    "stopPrice": stop_loss_price,
    "takeProfit": take_profit_price,
    "quantity": quantity,
    "newOrderRespType": "FULL",
    "type": "OCO"
}

# Send the request to the Binance API
response = requests.post(f"{api_endpoint}/fapi/v1/order", headers=headers, json=data)

# Print the response
print(json.dumps(response.json(), indent=4))
