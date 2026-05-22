from fetch_weather import get_weather

def generate_alert(city):

    weather = get_weather(city)

    temperature = weather["main"]["temp"]

    if temperature > 35:
        return "Heat Alert"

    elif temperature < 10:
        return "Cold Alert"

    return "Weather Normal"


if __name__ == "__main__":

    city = input("Enter City: ")

    print(generate_alert(city))