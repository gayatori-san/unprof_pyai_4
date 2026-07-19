import requests

def get_weather(city, api_key):
    # The endpoint for OpenWeatherMap's current weather data
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Setting up the parameters for the GET request
    # 'units=metric' converts the temperature to Celsius
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric" 
    }

    try:
        # Making the GET request
        response = requests.get(base_url, params=params)

        # Handling specific API errors gracefully
        if response.status_code == 404:
            print(f"\n❌ Error: Could not find city '{city}'. Please check the spelling.")
            return
        elif response.status_code == 401:
            print("\n❌ Error: Invalid API Key. Please check your credentials.")
            return

        # Catch any other HTTP errors
        response.raise_for_status() 
        
        # Parsing the JSON response
        data = response.json()

        # Extracting the specific data points we need
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].title()

        # Displaying the final output in the terminal
        print(f"\n🌤️  Weather in {city.title()}:")
        print(f"🌡️  Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁️  Condition: {condition}\n")

    # Handling network or connection errors
    except requests.exceptions.RequestException as e:
        print(f"\n❌ A network error occurred: {e}")
    # Handling unexpected JSON structures
    except KeyError:
        print("\n❌ Error parsing the weather data. The API response might have changed.")

if __name__ == "__main__":
    # ⚠️ Replace 'YOUR_API_KEY_HERE' with your actual OpenWeatherMap API key
    API_KEY = "API KEY"

    print("--- 🌦️ Python CLI Weather App ---")
    user_city = input("📍 Enter a city name: ")

    # Basic input validation to ensure the user actually typed something
    if user_city.strip():
        get_weather(user_city, API_KEY)
    else:
        print("\n❌ You must enter a valid city name.")
