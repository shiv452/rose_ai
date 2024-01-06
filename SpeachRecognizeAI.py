# Importing necessary libraries
import os
import pygame
import speech_recognition as srp
import pyautogui
import pywhatkit
import datetime



def speak(text):
    # Select a voice
    voice = "zh-TW-HsiaoChenNeural" 

    # Build the command for the edge-tts tool
    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "audio/output.mp3"'

    # Run the command using os.system
    os.system(command)

    # Initialize pygame and pygame.mixer
    pygame.init()
    pygame.mixer.init()

    try:
        # Load the audio file into the mixer
        pygame.mixer.music.load("audio/output.mp3")

        # Play the loaded audio file
        pygame.mixer.music.play()

        # Wait until the audio is finished playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(5)

    except Exception as e:
        # Print any exceptions that occur
        print(e)
    
    # ##Temporary comment     command + /
    # finally:
    #     # Stop and quit the pygame.mixer
    #     pygame.mixer.music.stop()
    #     pygame.mixer.music.quit()
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

# Get the current time
current_time = datetime.datetime.now()
hour = current_time.hour

# Greet the user based on the time of day
if 3 <= hour < 12:
    speak("Good morning, sir!")
elif 12 <= hour < 18:
    speak("Good afternoon, sir!")
else:
    speak("Good evening, sir!")

# Greet the user
speak("I'm Your Personal AI, My name is Rose")
speak("Hey Boss! How can I help you today?")

# Capture user input through voice command
query = command_from_user()
print(query)


###################################

while True:
    query = command_from_user().lower()
    print('\nYou said: ' + query)

    if 'open' in query:
        app_name = query.replace('open', '')
        speak('Opening ' + app_name)
        pyautogui.hotkey('command', 'space')
        pyautogui.typewrite(app_name)
        pyautogui.sleep(0.5)
        pyautogui.press('enter')

    elif 'close' in query:
        pyautogui.hotkey('command','q')
        speak(app_name + ' is closed, sir')

    elif 'play' in query:
        song_name = query.replace('play', '')
        speak('As you command, sir. Playing ' + song_name + ' for you....!')
        pywhatkit.playonyt(song_name)

    elif 'stop' in query or 'exit' in query or 'quit' in query:
        speak('Goodbye, sir!')
        break

    else:
        speak("I'm not sure how to handle that, sir.")

# Cleanup code if needed
# Stop and quit the pygame.mixer
pygame.mixer.music.stop()
pygame.mixer.music.quit()


