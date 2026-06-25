# 🌦️ CLI Weather App

> **A Python Command-Line Weather Application powered by the OpenWeatherMap API**

---

## ✨ Overview

The **CLI Weather App** is a Python-based command-line application that retrieves **real-time weather information** for any city across the globe using the **OpenWeatherMap REST API**.

The application demonstrates how to work with **REST APIs**, **JSON data**, **environment variables**, and **exception handling** while building a practical utility that can be executed directly from the terminal.

---

## 🚀 Features

### 🌍 Real-Time Weather Data

* Fetches live weather information from the **OpenWeatherMap API**
* Displays accurate and up-to-date weather conditions

### 🌡️ Weather Details

The application provides:

* 🌡️ Temperature (°C)
* 💧 Humidity (%)
* ☁️ Weather Description
* 🌬️ Current Weather Condition

### 🔐 Secure API Key Management

Instead of exposing credentials inside the source code, the application reads the API key from **environment variables**, following security best practices.

### ⚠️ Robust Error Handling

Gracefully handles common API and network issues, including:

* ❌ Invalid city names (`404 Not Found`)
* 🔑 Invalid API keys (`401 Unauthorized`)
* 🌐 Network or connection failures
* ⚡ Unexpected runtime errors

The program provides user-friendly messages without crashing.

### 🧩 JSON Parsing

Uses Python's built-in JSON support to extract only the required weather information from the API response.

---

# 🛠️ Technologies Used

* 🐍 Python 3
* 📦 Requests Library
* 🌐 OpenWeatherMap REST API
* 🔒 Environment Variables
* 📄 JSON

---

# 📂 Project Structure

```text
Task-4-CLI-Weather-App/
│
├── weather.py          # Main application
├── requirements.txt    # Project dependencies
├── README.md           # Documentation
└── .gitignore          # Ignore sensitive files
```

---

# ▶️ How to Run

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/gayatori-san/unprof_pyai_4
cd CLI-Weather-App
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install requests
```

---

## 3️⃣ Get an API Key

Create a free account on **OpenWeatherMap** and generate an API key.

---

## 4️⃣ Set the Environment Variable

### 🐧 Linux (Ubuntu / Kubuntu)

```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

### 🪟 Windows (PowerShell)

```powershell
$env:OPENWEATHER_API_KEY="your_api_key_here"
```

---

## 5️⃣ Run the Application

```bash
python weather.py
```

---

# 💻 Example Output

```text
Enter City Name: Mumbai

🌍 City: Mumbai
🌡️ Temperature: 30°C
💧 Humidity: 74%
☁️ Weather: Broken Clouds
```

---

# 📚 Concepts Demonstrated

* ✅ Working with REST APIs
* ✅ HTTP Requests using `requests`
* ✅ Parsing JSON Responses
* ✅ Exception Handling
* ✅ Environment Variables
* ✅ Secure Credential Management
* ✅ Command-Line Interface (CLI)

---

# 🎯 Learning Outcomes

By completing this project, you will learn how to:

* Connect Python applications to external APIs
* Work with real-time online data
* Parse JSON responses efficiently
* Handle API errors gracefully
* Protect sensitive credentials using environment variables
* Build practical command-line applications
---
