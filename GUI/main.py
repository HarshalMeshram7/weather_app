from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
import requests
import datetime
from io import BytesIO

# Initialize Tkinter window
root = Tk()
root.title("Harshal's Weather Forecasting App")
root.geometry("500x500")

# Get current date and time
now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# Search bar for city input
search_bar = Entry(root)

# Function to clear entry field
def clear_label():
    search_bar.delete(0, END)

# Function to retrieve city name from entry field
def get_city():
    city = search_bar.get()
    return city if city.strip() else "Nagpur"

# Function to fetch weather data
def get_weather():
    city = get_city()
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key=746ab0fadcc74303abe53757250606&q={city}&aqi=yes").json()
    return response

def update_conditionicon():
    response = get_weather()
    icon_url = f"https:{response['current']['condition']['icon']}"
    request_icon = requests.get(icon_url, stream=True)
    condition_icon_data = request_icon.content
    condition_icon = Image.open(BytesIO(condition_icon_data)).resize((200, 200), Image.Resampling.LANCZOS)
    condition_icon_tk = ImageTk.PhotoImage(condition_icon)
    condition_icon_label.config(image=condition_icon_tk)
    condition_icon_label.place(x=0, y=70)
    condition_icon_label.image = condition_icon_tk


# Fetch default weather data for Nagpur
# response = requests.get(f"http://api.weatherapi.com/v1/current.json?key=746ab0fadcc74303abe53757250606&q=Nagpur&aqi=yes").json()
response = get_weather()
# Fetch weather condition icon
# icon_url = f"https:{response['current']['condition']['icon']}"
# request_icon = requests.get(icon_url, stream=True)
# condition_icon_data = request_icon.content

# Font settings
current_weather_font = tkFont.Font(family="Arial", size=14)

# Load icons
search_icon = ImageTk.PhotoImage(Image.open("magnifier.png").resize((20, 20), Image.Resampling.LANCZOS))
location_icon = ImageTk.PhotoImage(Image.open("location.png").resize((20, 20), Image.Resampling.LANCZOS))
# condition_icon = Image.open(BytesIO(condition_icon_data)).resize((180, 180), Image.Resampling.LANCZOS)
# condition_icon_tk = ImageTk.PhotoImage(condition_icon)
condition_icon = ImageTk.PhotoImage(Image.open("weather-app.png").resize((180, 180), Image.Resampling.LANCZOS))

# Create labels and buttons
search_bar = Entry(root)
search_bar.insert(0, "Enter City Name: ")

exit_button = Button(root, text="Exit", command=root.quit, padx=20, pady=5)
clear_button = Button(root, text="Clear", command=clear_label, padx=20, pady=5)

current_weather_label = Label(root, text="Current Weather:", padx=50, font='Arial 14 bold', fg="#dd5202")
city_name = Label(root, text=response['location']['name'], font='Arial 12 bold')
current_time = Label(root, text=now, font='Arial 12 bold')
temperature = Label(root, text=f"{response['current']['temp_c']} °C", font='Arial 30 bold')

humidity_tag = Label(root, text="Humidity", font='Arial 12 bold')
humidity_value = Label(root, text=f"{response['current']['humidity']} %", font='Arial 12 bold')

wind_speed_tag = Label(root, text="Wind Speed & Direction", bg="#b1f0af", font='Arial 10 bold', width=15)
wind_speed_value = Label(root, text=f"{response['current']['wind_kph']} KM/H ({response['current']['wind_dir']})", bg="#b1f0af", font='Arial 10 bold', width=15)

cloudy_tag = Label(root, text="Clouds", font='Arial 12 bold')
cloudy_value = Label(root, text=f"{response['current']['cloud']} %", font='Arial 12 bold')

visibility_tag = Label(root, text="Visibility", bg="#b1f0af", font='Arial 10 bold', width=15)
visibility_value = Label(root, text=f"{response['current']['vis_km']} KM", bg="#b1f0af", font='Arial 10 bold', width=15)

pressure_tag = Label(root, text="Atmospheric Pressure", bg="#b1f0af", font='Arial 10 bold', width=20)
pressure_value = Label(root, text=f"{response['current']['pressure_mb']} mb", bg="#b1f0af", font='Arial 10 bold', width=20)

air_quality_tag = Label(root, text="Air Quality", bg="#b1f0af", font='Arial 10 bold', width=15)
air_quality_value = Label(root, text=f"{response['current']['air_quality']['pm2_5']} µg/m³", bg="#b1f0af", font='Arial 10 bold', width=15)

feels_like_tag = Label(root, text="Feels Like:", font='Arial 12 bold')
feels_like_value = Label(root, text=f"{response['current']['feelslike_c']} °C | {response['current']['condition']['text']}", font='Arial 12 bold')

# Placement of elements
search_bar.place(x=50, y=10, width=250, height=20)
exit_button.place(relx=1.0, rely=1.0, anchor=SE)
clear_button.place(relx=0, rely=1.0, anchor=SW)

search_icon_label = Button(root, image=search_icon, command=update_conditionicon)
search_icon_label.place(x=18, y=10)

location_icon_label = Label(root, image=location_icon)
location_icon_label.place(x=380, y=80)

current_weather_label.place(x=280, y=40)
city_name.place(x=400, y=80)
current_time.place(x=330, y=110)

condition_icon_label = Label(root, image=f"{condition_icon}", width=200, height=200)
condition_icon_label.place(x=0, y=70)
condition_icon_label.image = condition_icon

temperature.place(x=200, y=160)

humidity_tag.place(x=390, y=170)
humidity_value.place(x=410, y=200)

wind_speed_tag.place(x=165, y=370)
wind_speed_value.place(x=160, y=390)

cloudy_tag.place(x=395, y=250)
cloudy_value.place(x=405, y=280)

visibility_tag.place(x=390, y=370)
visibility_value.place(x=390, y=390)

pressure_tag.place(x=0, y=370)
pressure_value.place(x=0, y=390)

air_quality_tag.place(x=290, y=370)
air_quality_value.place(x=285, y=390)

feels_like_tag.place(x=210, y=230)
feels_like_value.place(x=210, y=255)

# Ensure image references persist
search_icon_label.image = search_icon
location_icon_label.image = location_icon
condition_icon_label.image = condition_icon

# Run Tkinter main loop
root.mainloop()