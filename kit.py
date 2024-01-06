import random
import datetime
import speech_recognition as srp
import pyttsx3

def speak(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech

    # Speak the provided text
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

def command_from_user():
    # Create a Recognizer instance
    rec = srp.Recognizer()

    # Use a microphone as the audio source
    with srp.Microphone() as source:
        print("Listening to your voice....!")

        # Set the pause threshold for audio input
        rec.pause_threshold = 1

        # Capture audio from the microphone
        audio = rec.listen(source)

    try:
        print("Recognizing the voice.....!")

        # Use Google Speech Recognition to convert audio to text
        query = rec.recognize_google(audio, language='en-us')
        return query

    except srp.UnknownValueError:
        # Handle the case where speech recognition could not understand the audio
        print("Sorry, I couldn't understand the audio.")
        return ""

    except srp.RequestError as e:
        # Handle the case where there is an error with the Google Speech Recognition service
        print(f"Error with the Google Speech Recognition service: {e}")
        return ""

    except Exception as e:
        # Handle any other unexpected errors
        print(e)
        return " "

    # Return the recognized query
    return query

def greet():
    return random.choice(["Hello", "Hi", "Hey", "Greetings"])

def respond_to_user_input(user_input):
    if "how are you" in user_input.lower():
        return random.choice(["I'm doing great, thank you", "I'm doing well", "I'm doing good"])
    elif "what is your name" in user_input.lower():
        return "My name is ChatBot"
    elif "who created you" in user_input.lower():
        return "I was created by a developer"
    else:
        return "Sorry, I don't understand"

# Get the current time
current_time = datetime.datetime.now()
hour = current_time.hour

# Greet the user based on the time of


