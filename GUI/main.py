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

# Font settings
current_weather_font = tkFont.Font(family="Arial", size=14)

# Search bar for city input
search_bar = Entry(root)
search_bar.insert(0, "Enter City Name: ")

def clear_label():
    search_bar.delete(0, END)

def get_city():
    city = search_bar.get()
    return city if city.strip() else "Nagpur"

# Function to fetch weather data safely
def get_weather():
    city = get_city()
    try:
        response = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key=746ab0fadcc74303abe53757250606&q={city}&aqi=yes"
        ).json()
        if "error" in response:
            raise ValueError(response['error']['message'])
        return response
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return {}

# Update all UI elements with new weather data
def update_weather():
    response = get_weather()
    location = response.get('location', {})
    current = response.get('current', {})
    condition = current.get('condition', {})
    air_quality = current.get('air_quality', {})

    city_name.config(text=location.get('name', '-'))
    current_time.config(text=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    temperature.config(text=f"{current.get('temp_c', '-')} °C")
    humidity_value.config(text=f"{current.get('humidity', '-')} %")
    wind_speed_value.config(text=f"{current.get('wind_kph', '-')} KM/H ({current.get('wind_dir', '-')})")
    cloudy_value.config(text=f"{current.get('cloud', '-')} %")
    visibility_value.config(text=f"{current.get('vis_km', '-')} KM")
    pressure_value.config(text=f"{current.get('pressure_mb', '-')} mb")
    air_quality_value.config(text=f"{air_quality.get('pm2_5', '-')} µg/m³")
    feels_like_value.config(text=f"{current.get('feelslike_c', '-')} °C | {condition.get('text', '-')}")

    icon_url = condition.get('icon')
    if icon_url:
        try:
            full_icon_url = f"https:{icon_url}"
            icon_response = requests.get(full_icon_url, stream=True)
            icon_image = Image.open(BytesIO(icon_response.content)).resize((200, 200), Image.Resampling.LANCZOS)
            icon_tk = ImageTk.PhotoImage(icon_image)
            condition_icon_label.config(image=icon_tk)
            condition_icon_label.image = icon_tk
        except Exception as e:
            print("Failed to load icon:", e)

# Load default icons
search_icon = ImageTk.PhotoImage(Image.open("magnifier.png").resize((20, 20), Image.Resampling.LANCZOS))
location_icon = ImageTk.PhotoImage(Image.open("location.png").resize((20, 20), Image.Resampling.LANCZOS))
condition_icon = ImageTk.PhotoImage(Image.open("weather-app.png").resize((180, 180), Image.Resampling.LANCZOS))

# Create labels and buttons
exit_button = Button(root, text="Exit", command=root.quit, padx=20, pady=5, bg="#ec6d6d")
clear_button = Button(root, text="Clear", command=clear_label, padx=20, pady=5, bg="#36e630")
search_icon_button = Button(root, image=search_icon, command=update_weather)

current_weather_label = Label(root, text="Current Weather:", padx=50, font='Arial 14 bold', fg="#dd5202")

city_name = Label(root, text="-", font='Arial 12 bold')
current_time = Label(root, text=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), font='Arial 12 bold')
temperature = Label(root, text="- °C", font='Arial 30 bold')

humidity_tag = Label(root, text="Humidity", font='Arial 12 bold')
humidity_value = Label(root, text="- %", font='Arial 12 bold')
\
wind_speed_tag = Label(root, text="Wind Speed", bg="#b1f0af", font='Arial 10 bold', width=15)
wind_speed_value = Label(root, text="- KM/H (-)", bg="#b1f0af", font='Arial 10 bold', width=15)

cloudy_tag = Label(root, text="Clouds", font='Arial 12 bold')
cloudy_value = Label(root, text="- %", font='Arial 12 bold')

visibility_tag = Label(root, text="Visibility", bg="#b1f0af", font='Arial 10 bold', width=15)
visibility_value = Label(root, text="- KM", bg="#b1f0af", font='Arial 10 bold', width=15)

pressure_tag = Label(root, text="Atmospheric Pressure", bg="#b1f0af", font='Arial 10 bold', width=20)
pressure_value = Label(root, text="- mb", bg="#b1f0af", font='Arial 10 bold', width=20)

air_quality_tag = Label(root, text="Air Quality", bg="#b1f0af", font='Arial 10 bold', width=15)
air_quality_value = Label(root, text="- µg/m³", bg="#b1f0af", font='Arial 10 bold', width=15)

feels_like_tag = Label(root, text="Feels Like:", font='Arial 12 bold')
feels_like_value = Label(root, text="- °C | -", font='Arial 12 bold')

condition_icon_label = Label(root, image=condition_icon, width=200, height=200)
condition_icon_label.image = condition_icon

# Place widgets
search_bar.bind("<Return>", lambda event: update_weather())
search_bar.place(x=50, y=10, width=250, height=20)
search_icon_button.place(x=18, y=10)
exit_button.place(relx=1.0, rely=1.0, anchor=SE)
clear_button.place(relx=0, rely=1.0, anchor=SW)

current_weather_label.place(x=280, y=40)
city_name.place(x=400, y=80)
current_time.place(x=330, y=110)

location_icon_label = Label(root, image=location_icon)
location_icon_label.place(x=380, y=80)

condition_icon_label.place(x=0, y=70)
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

feels_like_tag.place(x=20, y=320)
feels_like_value.place(x=120, y=320)

# Initial fetch
update_weather()

# Run Tkinter main loop
root.mainloop()
