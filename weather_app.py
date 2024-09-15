from tkinter import *
import requests
import json
from datetime import datetime
 
#Initialize Window
 
root =Tk()
root.geometry("700x550") 
root.resizable(0,0) 
bg = PhotoImage( file = "sky.png") 
label1 = Label( root, image = bg,height=700,width=700) 
label1.place(x = 0,y = 0) 
root.title("Weather App")
 
 
# Functions to fetch and display weather info
location_value = StringVar()
 
 
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
 
location_value = StringVar()
 
def showWeather():
    api_key = "a75089587886432a93f301d645f72e9e"  
    location_name=location_value.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location_name + '&appid='+api_key
    response = requests.get(weather_url)
    weather_info = response.json()
    tfield.delete("1.0", "end")   
 
 
    if weather_info['cod'] == 200:
        kelvin = 273 
        temp = int(weather_info['main']['temp'] - kelvin)                                     #converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed =round((weather_info['wind']['speed'] * 3.6),2)
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']["all"]
        description = weather_info['weather'][0]['description']
        high = round(weather_info['main']['temp_max'])
        low = round(weather_info['main']['temp_min'])
 
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
 
         
        weather = f"\nThe weather in {location_name[0].upper()}{location_name[1:]} is {temp}°C with {description}.\n\nIt feels like {feels_like_temp}°C.\n\nToday's high is {high}°C and today's low is {low}°C.\n\nSunrise is expected at {sunrise_time} and sunset is expected at {sunset_time}.\n\n{cloudy}% clouds spread over the sky.\n\nWind blowing at rate of {wind_speed} km/h\n\n{humidity}% humidity.\n\nPressure level:{pressure} hPa"
    else:
        weather = f"\n\tWeather for '{location_name}' not found!\n\tKindly Enter valid Location !!"
    tfield.insert(INSERT, weather)   
 
 
#Interface
location_head= Label(root, text = 'Enter Location', font = 'Arial 12 bold').pack(pady=10) 
inp_location = Entry(root, textvariable = location_value,  width = 24, font='Arial 14').pack()
Button(root, command = showWeather, text = "Predict Weather", font="Arial 10 bold", bg='black', fg='white', activebackground="grey", padx=10, pady=10 ).pack(pady= 10)
 
#output
weather_now = Label(root, text = "Weather Forecast", font = 'arial 12 bold').pack(pady=10)
tfield = Text(root, width=70, height=18)
tfield.pack()
root.mainloop()