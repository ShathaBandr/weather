import requests

api_key = '6d14bde3f7856fbf132dfd03703cbc40'

user_input = input("Enter City: ")
print(user_input)

weather__data = requests.get(
    f'http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric'
)

if weather__data.json()['cod'] == '404':
    print("City not found, please try again.")
else:
    weather = weather__data.json()['weather'][0]['main']
    temp = round(weather__data.json()['main']['temp'])
    print(f"Weather in {user_input} is {weather} with a temperature of {temp}°C.")
