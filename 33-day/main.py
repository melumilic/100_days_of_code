import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# print(data)

response = requests.get("https://api.sunrise-sunset.org/json")
response.raise_for_status()

