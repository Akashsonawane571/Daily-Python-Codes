# Day13_WeatherApp_GUI.py
# Simple Weather App with Tkinter + OpenWeather API

import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    api_key = api_entry.get()

    if not city or not api_key:
        messagebox.showerror("Error", "Please enter both City and API Key")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", "City not found!")
            return

        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result.set(f"🌡 {temp}°C\n {condition}\n Humidity: {humidity}%\n Wind: {wind} m/s")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", str(e))


# GUI Setup
root = tk.Tk()
root.title(" Weather App")
root.geometry("300x300")

tk.Label(root, text="Enter City:").pack(pady=5)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Label(root, text="Enter API Key:").pack(pady=5)
api_entry = tk.Entry(root, show="*")
api_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12), justify="center").pack(pady=20)

root.mainloop()
