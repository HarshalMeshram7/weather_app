from tkinter import *
from PIL import Image, ImageTk
import requests
import datetime
from io import BytesIO


now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")


response = requests.get(f"http://api.weatherapi.com/v1/current.json?key=746ab0fadcc74303abe53757250606&q=Nagpur&aqi=yes").json()

icon_url = f"https:{response['current']['condition']['icon']}"
request_icon = requests.get(icon_url, stream=True)
condition_icon_data = request_icon.content

root = Tk()
root.title("Harshal's Weather Forcasting App") 
root.geometry("500x500")

search_icon = ImageTk.PhotoImage(Image.open("magnifier.png").resize((20,20), Image.Resampling.LANCZOS))
location_icon = ImageTk.PhotoImage(Image.open("location.png").resize((20,20), Image.Resampling.LANCZOS))
condition_icon = Image.open(BytesIO(condition_icon_data)).resize((250,250), Image.Resampling.LANCZOS)
search_icon_label = Label(image=search_icon)
location_icon_label = Label(image=location_icon)
condition_icon_tk = ImageTk.PhotoImage(condition_icon)

def clear_label():
    search_bar.delete(0, END)

search_bar = Entry(root)
exit_button = Button(root, text="Exit", command=root.quit, padx=20, pady=5)
clear_button = Button(root, text="Clear", command=clear_label, padx=20, pady=5)
current_weather_label = Label(root, text="Current Weather:", padx=50)
city_name = Label(root, text=response['location']['name'])
current_time = Label(root, text=now)
temperature = Label(root, text=f"{response['current']['temp_c']} *c")
humidity_tag = Label(root, text="Humidity")
humidity_value = Label(root, text=f"{response['current']['humidity']} %")
wind_speed_tag = Label(root, text="Wind Speed \n& Direction")
wind_speed_value = Label(root, text=f"{response['current']['wind_kph']} KM/H ({response['current']['wind_dir']})")
cloudy_tag = Label(root, text="Clouds")
cloudy_value = Label(root, text=f"{response['current']['cloud']} %")
visibility_tag = Label(root, text="Visibility")
visibility_value = Label(root, text=f"{response['current']['vis_km']} KM")
pressure_tag = Label(root, text="Atmospheric Pressure")
pressure_value = Label(root, text=f"{response['current']['pressure_mb']} mb")
air_quality_tag = Label(root, text="Air Quality")
air_quality_value = Label(root, text=f"{response['current']['air_quality']['pm2_5']} µg/m³")
feels_like_tag = Label(root, text="Feels Like")
feels_like_value = Label(root, text=f"{response['current']['feelslike_c']} *c | {response['current']['condition']['text']}")



search_bar.place(x=50, y=10, width=250, height=20)
exit_button.place(relx=1.0, rely=1.0, anchor=SE)
clear_button.place(relx=0, rely=1.0, anchor=SW)
search_icon_label.place(x= 18, y=10)
current_weather_label.place(x=320, y=30)
location_icon_label.place(x=300, y=70)
city_name.place(x=400, y=70)
current_time.place(x=350, y=100)
condition_icon_label = Label(root, image=condition_icon_tk, width=200, height=200)
condition_icon_label.place(x=5, y=100)
condition_icon_label.image = condition_icon_tk
temperature.place(x=250,y=200)
humidity_tag.place(x=350, y=150)
humidity_value.place(x=380,y=180)
wind_speed_tag.place(x=200, y=350)
wind_speed_value.place(x=200, y=370)
cloudy_tag.place(x=350, y=200)
cloudy_value.place(x=350, y=220)
visibility_tag.place(x=400, y=350)
visibility_value.place(x=400, y=370)
pressure_tag.place(x=20, y=350)
pressure_value.place(x=20, y=370)
air_quality_tag.place(x=300, y=350)
air_quality_value.place(x=300, y=370)
feels_like_tag.place(x=250, y=250)
feels_like_value.place(x=305, y=250)







search_icon_label.image = search_icon
location_icon_label.image = location_icon
condition_icon_tk.image = condition_icon_tk
root.mainloop()
