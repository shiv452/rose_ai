import pygame
import os
import speech_recognition as srp
import pyautogui
import pywhatkit
from datetime import datetime
import time

def speak(text):

    # Rose voice
    voice = "en-US-AriaNeural"

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
    

def command_from_user():
    rec = srp.Recognizer()

    with srp.Microphone() as source:
        rec.pause_threshold = 0.5

        try:
            audio = rec.listen(source)
            query_general = rec.recognize_google(audio, language='en-us')

        except srp.UnknownValueError:
            return ""

        except srp.RequestError as e:
            print(f"Error with the Google Speech Recognition service: {e}")
            return ""

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return ""

    return query_general.lower()

def click_skip_ad_button():
    """
    Clicks the YouTube skip ad button using pyautogui.

    Raises:
        Exception: If an error occurs during the button click.
    """
    try:
        skip_path = '//*[@id="ad-text:7"]'                                      #'//*[@id="skip-button:1n"]/span/button' #XPath for skip btn
        pyautogui.click(pyautogui.locateCenterOnScreen('skip_path'))  
        #click perfom here
    except Exception as e:
        print("Error clicking the skip ad button:", e)

def play_youtube_video(song_name):
    """
    Plays a YouTube video using pywhatkit.

    Args:
        song_name (str): The name of the song to be played.

    Raises:
        Exception: If an error occurs during video playback.
    """
    try:
        speak('As your command, sir. Playing ' + song_name + ' for you.')
        pywhatkit.playonyt(song_name)
        time.sleep(10)
        click_skip_ad_button()

    except Exception as e:
        speak("Sorry, there was an issue playing the requested song")
