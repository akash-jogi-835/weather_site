import streamlit as st
import requests

st.set_page_config(page_title="🌤️ Weather App", layout="centered")

st.title("🌦️ Weather Dashboard")
st.write("Enter a city name to get the current weather info.")

# Input from user
city = st.text_input("City Name")

# Weather function
def get_weather(city):
    api_key = "745911cbe8f0cd1df5c5f76b4314d886"  # Replace with your real API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "Temperature": f"{data['main']['temp']} °C",
            "Feels Like": f"{data['main']['feels_like']} °C",
            "Humidity": f"{data['main']['humidity']}%",
            "Weather": data['weather'][0]['description'].title(),
            "Wind Speed": f"{data['wind']['speed']} m/s"
        }
        return weather
    else:
        return None

# Show results
if city:
    weather = get_weather(city)
    if weather:
        st.success(f"Weather in {city.title()}")
        for key, value in weather.items():
            st.write(f"**{key}:** {value}")
    else:
        st.error("City not found. Please enter a valid city name.")
