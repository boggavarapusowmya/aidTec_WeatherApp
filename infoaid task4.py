import requests

api_key = 'b0d0e0ec6cce941133d3ea921a0911e2'

while True:
    user_input = input("\n\nEnter city (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        break

    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    if weather_data.json().get('cod') == '404':
        print("No City Found")
    else:
        weather_info = weather_data.json()['weather'][0]
        weather_condition = weather_info['main']
        temperature = round(weather_data.json()['main']['temp'])
        humidity = weather_data.json()['main']['humidity']
        wind_speed = weather_data.json()['wind']['speed']

        print(f"The weather in {user_input} is: {weather_condition}")
        print(f"The temperature in {user_input} is: {temperature}ºF")
        print(f"The humidity in {user_input} is: {humidity}%")
        print(f"The wind speed in {user_input} is: {wind_speed} mph")
