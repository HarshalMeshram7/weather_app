import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')

print("_____Welcome to Weather forcast_____")

def fetch_weather(city):
    try:
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes").json()
        if 'error' in response:
            raise ValueError(f"Error: {response['error']['message']}")
        return response
    except requests.RequestException as e:
        raise ConnectionError(f"Error connecting to API: {e}")

def display_weather():
    try:
        response = fetch_weather(city)
        print(
            f"City = {response['location']['name']}, {response['location']['region']}, {response['location']['country']}"
            f"\nTemperature = {response['current']['temp_c']}*c"
            f"\nFeels Like = {response['current']['feelslike_c']}*c"
            f"\nCondition = {response['current']['condition']['text']}"
            f"\nWind Speed = {response['current']['wind_kph']}KM/H"
            f"\nHumidity = {response['current']['humidity']}%"
        )
    except (ValueError, ConnectionError) as e:
        print(e)
    except KeyError:
        print("Error: Unable to process weather data. Please try again.")

while True:
    city = input("Please enter city name ('q' to exit): ").strip().lower()
    if city == 'q':
        break
    display_weather()


    








#______________________________________________________________________________________________________




# import requests
# from dotenv import load_dotenv
# import os

# load_dotenv()

# API_KEY = os.getenv('API_KEY')

# print("_____Welcome to Weather Forecast_____")

# city = input("Please enter city name: ").strip()

# def fetch_weather(city):
#     try:
#         response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes").json()
#         if 'error' in response:
#             raise ValueError(f"Error: {response['error']['message']}")
#         return response
#     except requests.RequestException as e:
#         raise ConnectionError(f"Error connecting to the weather API: {e}")

# def display_weather():
#     try:
#         response = fetch_weather(city)
#         print(
#             f"{response['location']['name']}\n"
#             f"Region = {response['location']['region']}, {response['location']['country']}\n"
#             f"Temperature = {response['current']['temp_c']}°C\n"
#             f"Feels Like = {response['current']['feelslike_c']}°C\n"
#             f"Condition = {response['current']['condition']['text']}\n"
#             f"Wind Speed = {response['current']['wind_kph']} KM/H\n"
#             f"Humidity = {response['current']['humidity']}%"
#         )
#     except (ValueError, ConnectionError) as e:
#         print(e)
#     except KeyError:
#         print("Error: Unable to process weather data. Please try again.")

# display_weather()