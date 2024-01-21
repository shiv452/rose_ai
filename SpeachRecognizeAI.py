# Importing necessary libraries
import os
import platform
import pygame
import speech_recognition as srp
import pyautogui
import pywhatkit
from datetime import datetime
import time
import Youtube_skip

#########################
'''
Below code is used to enable the AI voice
'''
#########################
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
    
    ##Temporary comment     command + /
    # finally:
    #     # Stop and quit the pygame.mixer
    #     pygame.mixer.music.stop()
    #     pygame.mixer.music.quit()
    
    #####################################################
    '''
    Below line of code is used to Enable the Microphone and Voice Recognize in real time scenario
    '''
    #####################################################

def command_from_user():
    rec = srp.Recognizer()

    with srp.Microphone() as source:
        speak("I'm listening. please speak!")
        rec.pause_threshold = 0.2

        try:
            audio = rec.listen(source)
            print("Analyzing the voice...!")
            query_general_general = rec.recognize_google(audio, language='en-us')

        except srp.UnknownValueError:
            # Handle the case where speech recognition could not understand the audio
            speak("Sorry, I couldn't understand what you said. Please try again.")
            return ""

        except srp.RequestError as e:
            # Handle the case where there is an error with the Google Speech Recognition service
            print(f"Error with the Google Speech Recognition service: {e}")
            return ""

        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}")
            return ""

    # Return the recognized query_general
    return query_general
#######################################
'''
"Darwin" in this context refers to the Darwin operating system kernel, which is the open-source Unix-like operating system core that underlies macOS. Apple's macOS is built on top of the Darwin operating system.
'''


# ########################################################
# Function to greeting the user based on the time bases   
def greet_user():
    # Get the current time
    current_time = datetime.now()
    hour = current_time.hour

    # Greet the user based on the time of day
    if 3 <= hour < 12:
        speak("Good morning, sir!")
    elif 12 <= hour < 18:
        speak("Good afternoon, sir!")
    else:
        speak("Good evening, sir!")
# call function
greet_user()

########################################################
# ROSE Intro
speak("I'm Your Personal AI, My name is Rose")
speak("Hye Shivam, How can i assist you today....?")

##################################
# Initialize app_name outside the loop
app_name = ""

# # Initialize sleep mode state
# sleep_mode = False

# While loop for user interactions
# While loop for user interactions
while True:
    # Get general user input
    query_general = command_from_user().lower()

    # Check if the general query is not empty
    #if query_general:
    # Get YouTube-specific user input
    # Get YouTube-specific user input only if the general query is not empty
    query_youtube_skip = Youtube_skip.command_from_user()

    # Print the recognized queries for debugging
    print('\nYou said (General):', query_general)
    print('\nYou said (YouTube skip):', query_youtube_skip)

    if 'open' in query_general:
        app_name = query_general.replace('open', '')
        speak('opening ' + app_name)
        with pyautogui.hold('command'):
            pyautogui.press('space')
        pyautogui.typewrite(app_name)
        pyautogui.sleep(0.2)
        pyautogui.press('enter')

    # Check if the query_general contains the word 'switch tab'
    elif 'switch right' in query_general:
        #pyautogui.hotkey('command','tab') #this line of code switch tab for mac
        #pyautogui.hotkey('alt','tab') #this line is for Win user
        #switchTab()
        pyautogui.hotkey('Ctrl','tab')
        time.sleep(2)
        speak('tab is switch sir')
        
    elif 'switch left' in query_general:
        #pyautogui.hotkey('command','tab') #this line of code switch tab for mac
        #pyautogui.hotkey('alt','tab') #this line is for Win user
        #switchTab()
        pyautogui.hotkey('Ctrl','shift','tab')
        time.sleep(2)
        speak('tab is switch sir')
        
    elif 'close tab' in query_general:
        #pyautogui.hotkey('command','w') #this line is to close the tab fro mac
        #pyautogui.hotkey('alt','w') #this line is for win user
        #closeTab()
        with pyautogui.hold('command'):
            pyautogui.press('w')
        time.sleep(0.5)
        speak('tab is closed sir')
        
    elif 'close' in query_general:
        pyautogui.hotkey('command','q')
        time.sleep(4)
        speak(app_name + ' is closed, sir')
        
    # Check if the query_general contains the word 'Play' and play the song
    elif 'play' in query_general:
        song_name = query_general.replace('play', '')
        Youtube_skip.play_youtube_video(song_name)
        # try:
        #     speak('As your command, sir. Playing ' + song_name + ' for you.')
        #     pywhatkit.playonyt(song_name)
        # except Exception as e:
        #     speak("Sorry, there was an issue playing the requested song.")
            
        # speak('As your command, sir. Playing ' + song_name + ' for you.')
        # pywhatkit.playonyt(song_name)
        
    # Check if the query_general contains the word 'time'
    elif 'time' in query_general:
        current_time = datetime.now().strftime('%I:%M %p')#Get the current time and format it as hh:mm AM/PM
        '''
    %H: Represents the hour in 24-hour format (00 to 23).
    %I: Represents the hour in 12-hour format (01 to 12).
    %M: Represents the minute (00 to 59).
    %p: Represents either AM or PM, depending on the time.
        '''
        speak('current time is '+ current_time)
        
    elif 'search' in query_general:
        search_query_general = query_general.replace('search', '')
        try:
            speak(f"Searching the web for {search_query_general}")
            pywhatkit.search(search_query_general)
        except Exception as e:
                speak("Sorry, there was an issue with the search.")
        # speak(f"Searching the web for {search_query_general}")
        # pywhatkit.search(search_query_general)

    # elif 'sleep' in query_general:
    #     speak('As your command sir,' +'I''m going to sleep but you can call me anytime just you have to say wake up and I will be there for you')
    #     sleep_mode = True
    # Stop and exit from the current window
        
    elif any(keyword in query_general for keyword in ['stop', 'exit', 'quit', 'bye rose']):
        speak('Thank you for using rose ai, have a great day, sir!')
        speak('If you need assistance in the future, feel free to call upon me. Goodbye!')
        break

    else:
        speak("I'm not sure how to handle that, sir")

    '''
    Below step is used to stop the infinite while loop for stop
    '''
    # Cleanup code if needed
    # Stop and quit the pygame.mixer
pygame.mixer.music.stop()
pygame.mixer.quit()   