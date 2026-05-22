import requests

API_KEY = "YOUR_API_KEY"

def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    return response.json()


if __name__ == "__main__":

    city = input("Enter City: ")

    weather = get_weather(city)

    print(weather)