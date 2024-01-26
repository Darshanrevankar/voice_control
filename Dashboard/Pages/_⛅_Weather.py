import streamlit as st
from PIL import Image
import requests
API_KEY = "3045dd712ffe6e702e3245525ac7fa38"

img1 = Image.open("Rain.jpg")
img2 = Image.open("Summer.jpeg")
img3 = Image.open("Winter.jpeg")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def find_current_weather(city):
    base_url  = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    weather_data = requests.get(base_url).json()
    try:
        temperature = round(weather_data['main']['temp'])
        humidity = round(weather_data['main']['humidity'])
        pressure = round(weather_data['main']['pressure'])
    except KeyError:
        st.error("City Not Found")
        st.stop()
    return temperature,humidity,pressure


def main():
    st.header("Weather Dashboard")
    city = st.text_input("Enter the City").lower()
    if city:
        temperature,humidity,pressure = find_current_weather(city)
        temperature = (temperature - 273)
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label = "Temperature",value=f"{temperature}°C")
            st.metric(label = "Humidity",value=f"{humidity}%",)
            st.metric(label = "Pressure",value=f"{pressure}hPa")
            if temperature >= 25:
                st.image(img2)
            elif temperature >= 18 and temperature<25:
                st.image(img3)
            elif temperature >= 10 and temperature<18:
                st.image(img1)
    
    # st.metric(label = "Temperature",value=f"{temperature}°C")
    # st.metric(label = "Humidity",value=f"{humidity}%",)
    # st.metric(label = "Pressure",value=f"{pressure}hPa")
    
if __name__ == '__main__':
    main()

