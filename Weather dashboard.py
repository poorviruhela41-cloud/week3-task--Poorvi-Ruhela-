import requests
import json
import os

# Replace with your OpenWeatherMap API key
API_KEY = "d405f42cfce8efb14fa5fac5785bb6ff" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

HISTORY_FILE = "history.json"


# ---------- Functions ----------
def fetch_weather(city):
    """Fetch full weather details for a city using OpenWeatherMap API"""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "temp_min": data["main"]["temp_min"],
            "temp_max": data["main"]["temp_max"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "condition": data["weather"][0]["description"].title()
        }
        return weather
    else:
        return None


def save_history(entry):
    """Save search history to file"""
    history = load_history()
    history.append(entry)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


def load_history():
    """Load search history"""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []


def show_last_five():
    """Display last 5 searches"""
    history = load_history()
    if not history:
        print("No search history found.")
    else:
        print("\n📜 Last 5 Searches:")
        for entry in history[-5:]:
            print(f"- {entry['city']}: {entry['temp']}°C, {entry['condition']}")


# ---------- Menu ----------
def main():
    while True:
        print("\n===== Weather Dashboard =====")
        print("1. Search Weather by City")
        print("2. Show Last 5 Searches")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            city = input("Enter city name: ")
            weather = fetch_weather(city)
            if weather:
                print(f"\n🌍 Weather in {weather['city']}:")
                print(f"   🌡 Temperature   : {weather['temp']}°C (Feels like {weather['feels_like']}°C)")
                print(f"   🔼 Max Temp      : {weather['temp_max']}°C")
                print(f"   🔽 Min Temp      : {weather['temp_min']}°C")
                print(f"   💧 Humidity      : {weather['humidity']}%")
                print(f"   🌬 Wind Speed    : {weather['wind_speed']} m/s")
                print(f"   ☁ Condition      : {weather['condition']}")
                save_history(weather)
            else:
                print("❌ City not found or API error.")

        elif choice == "2":
            show_last_five()

        elif choice == "3":
            print("👋 Exiting Weather Dashboard. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()