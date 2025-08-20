import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
import pywhatkit
import wikipedia
import webbrowser
import requests
import sys

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speak function
def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# Listen function with fallback to text
def take_command():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
    except:
        query = input("📝 Type your command: ")
    return query.lower()

# Get weather
def get_weather(city):
    api_key = "your_openweather_api_key" # Replace with your key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            return f"The temperature in {city} is {temp}°C with {desc}"
        else:
            return "City not found."
    except:
        return "Failed to get weather info."

# Calculator
def calculate():
    speak("What should I calculate?")
    expr = take_command()
    try:
        result = eval(expr)
        speak(f"The result is {result}")
    except:
        speak("Sorry, I couldn't calculate that.")

# Main function
def run_assistant():
    speak("Hello! I am your assistant. How can I help you?")

    while True:
        query = take_command()

        if 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {time}")

        elif 'date' in query:
            date = datetime.datetime.now().strftime('%B %d, %Y')
            speak(f"Today is {date}")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia...")
                speak(result)
            except:
                speak("Sorry, I couldn't find that on Wikipedia.")

        elif 'play' in query:
            song = query.replace('play', '')
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        elif 'search' in query:
            speak("What should I search for?")
            topic = take_command()
            url = f"https://www.google.com/search?q={topic}"
            webbrowser.open(url)
            speak(f"Here are the results for {topic}")

        elif 'weather' in query:
            speak("Which city?")
            city = take_command()
            weather = get_weather(city)
            speak(weather)

        elif 'calculate' in query:
            calculate()

        elif 'exit' in query or 'stop' in query or 'quit' in query:
            speak("Goodbye! Have a great day.")
            sys.exit()

        else:
            speak("Sorry, I didn’t understand. Try saying joke, play song, or weather.")

# Run
if __name__ == "__main__":
    run_assistant()
