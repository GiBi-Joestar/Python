import requests

city = input("Enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=1854c68a083d4252a99144443262003&q={city}&aqi=yes"

try:
    r = requests.get(url, timeout=5)
    r.raise_for_status()

    weatherDict = r.json()
    temp = weatherDict["current"]["temp_c"]

    print(temp)

except requests.exceptions.RequestException:
    print("Network error. Please check your connection.")

except KeyError:
    print("Invalid response. City might not be found.")