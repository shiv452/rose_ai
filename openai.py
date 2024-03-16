import speech_recognition as sr
from gtts import gTTS
import os
import requests

def speak(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")

def process_command(command):
    if "change voice" in command:
        # Change voice or language here
        lang = 'en'  # Change language to the desired language
        speak("Voice changed to English", lang)
    elif "search" in command:
        query = command.replace("search", "").strip()
        # Perform API call to search for the query
        # Replace 'YOUR_API_KEY' with your actual API key
        api_key = 'apikey="AIzaSyBHM_AMISuJ-TYP7te-xfb8xCeegVks210'
        url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx=YOUR_CX&q={query}'
        response = requests.get(url)
        results = response.json()['items']
        if results:
            speak(f"I found {len(results)} results for {query}. Here is the first one.")
            speak(results[0]['snippet'])
        else:
            speak("I'm sorry, I couldn't find any results for that query.")

def main():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said: " + command)
        process_command(command)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    main()
