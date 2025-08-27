# Day12_WeatherApp.py
# Fetch weather details using OpenWeather API

import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get("cod") != 200:
            print(" City not found!")
            return None

        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"].capitalize(),
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather

    except requests.exceptions.RequestException as e:
        print(f" Error: {e}")
        return None


if __name__ == "__main__":
    api_key = input("Enter your OpenWeather API Key: ")
    city = input("Enter city name: ")

    weather_data = get_weather(city, api_key)

    if weather_data:
        print(f"\n Weather in {weather_data['city']}:")
        print(f" Temperature: {weather_data['temperature']}°C")
        print(f" Condition: {weather_data['description']}")
        print(f" Humidity: {weather_data['humidity']}%")
        print(f" Wind Speed: {weather_data['wind_speed']} m/s")
