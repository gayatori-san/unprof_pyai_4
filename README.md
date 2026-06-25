# Task 4: CLI Weather App 🌦️

## Overview
This project is part of Phase 1 – Python Intermediate. It is a command-line interface (CLI) application that fetches and displays real-time weather data for any city using the OpenWeatherMap API.

## Features
- **Real-Time Data Extraction:** Uses the `requests` library to connect to the OpenWeatherMap REST API and parse the JSON response.
- **Targeted Metrics:** Extracts and displays temperature (in Celsius), humidity percentage, and current weather conditions.
- **Robust Error Handling:** Gracefully handles `404 Not Found` (invalid city names), `401 Unauthorized` (invalid API keys), and general network connection errors without crashing.
- **Secure Credential Management:** Designed to read the API key from system environment variables to prevent hardcoding sensitive credentials in the source code.

## How to Run

1. **Get an API Key:** Sign up at [OpenWeatherMap](https://openweathermap.org/) and generate a free API key.
2. **Clone the Repository:** Navigate to the Task 4 directory on your machine.
3. **Set the Environment Variable:** Open your Kubuntu terminal and export your key securely:
   ```bash
   export OPENWEATHER_API_KEY="your_actual_api_key_here"
