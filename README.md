🗣️ Python Voice Assistant

A simple yet powerful **voice-enabled assistant** built in Python that can perform tasks such as telling the time/date, searching Wikipedia, playing YouTube videos, telling jokes, getting weather updates, and more.

---

## 📋 Features

* 🎤 Voice input (with fallback to text input if microphone fails)
* 🗣️ Voice responses using `pyttsx3`
* ⏰ Tells current time and date
* 📚 Searches Wikipedia
* 📺 Plays videos on YouTube
* 🔍 Searches the web (via Google)
* 🌦️ Retrieves current weather (via OpenWeatherMap API)
* 😂 Tells jokes (via `pyjokes`)
* 🧮 Performs basic calculations
* 🔄 Continuous interaction loop
* ❌ Supports exit/quit/stop commands

---

## 📦 Requirements

Install dependencies via pip:

```bash
pip install pyttsx3 SpeechRecognition pyjokes pywhatkit wikipedia requests
```

Additionally:

* For speech recognition to work properly, install **PyAudio**:

  * Windows:

    ```bash
    pip install pipwin
    pipwin install pyaudio
    ```
  * macOS:

    ```bash
    brew install portaudio
    pip install pyaudio
    ```
  * Linux:

    ```bash
    sudo apt-get install python3-pyaudio
    pip install pyaudio
    ```

---

## 🚀 How to Use

1. Save the script as `voice_assistant.py`.

2. Open terminal/command prompt in the directory.

3. Replace the placeholder in the code with your **OpenWeatherMap API key**:

   ```python
   api_key = "your_openweather_api_key"
   ```

   Get one for free at [https://openweathermap.org/api](https://openweathermap.org/api)

4. Run the script:

```bash
python voice_assistant.py
```

---

## 🧠 Supported Commands

| Command                | Action                                                 |
| ---------------------- | ------------------------------------------------------ |
| `what's the time`      | Tells current time                                     |
| `what's the date`      | Tells today's date                                     |
| `tell me a joke`       | Says a random joke                                     |
| `search wikipedia ...` | Searches and reads summary from Wikipedia              |
| `play ...`             | Plays song/video on YouTube                            |
| `search`               | Asks for a topic and opens Google search               |
| `weather`              | Asks for a city and provides weather info              |
| `calculate`            | Takes a math expression and evaluates it (e.g., `5*5`) |
| `exit`, `stop`, `quit` | Ends the assistant session                             |

---

## 💡 Example Interaction

```
Assistant: Hello! I am your assistant. How can I help you?
🎤 Listening...
User said: what's the weather
Assistant: Which city?
🎤 Listening...
User said: New York
Assistant: The temperature in New York is 28°C with clear sky
```

---

## 🛠 Troubleshooting

* If microphone access fails, you'll be prompted for **text input**.
* Make sure your OpenWeatherMap API key is valid.
* If `speech_recognition` fails, check for proper microphone setup and permissions.

---

## 📁 File Structure

```
voice_assistant.py      # Main assistant script
README.md               # Project documentation
```

---

* Convert it into a desktop app
* Add custom voice or background music
