import requests
from twilio.rest import Client
import os

api_key = os.environ["API_KEY"]
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]


params = {
    "lat":37.548271,
    "lon": -121.988571,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(url=OWM_Endpoint, params=params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)




print(weather_data["hourly"][0]["weather"][0]["id"])

will_rain = False

weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Make sure you bring an umbrella!",
        from_='+14153404820',
        to='+14152250783'
    )

    print(message.status)
