# Importing necessary libraries
import os
import platform
import pygame
import speech_recognition as srp
import pyautogui
import pywhatkit
from datetime import datetime
import time



#########################
'''
Below code is used to enable the AI voice
'''
#########################
def speak(text):

    # Select a voice
    ''' Best Voice to use US female voice
    en-US-AriaNeural, en-US-AnaNeural, en-US-JennyNeural, en-US-MichelleNeural, 
    '''
    voice = "en-US-AnaNeural"  #"zh-TW-HsiaoChenNeural"   #"chaina voice 

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
    # Create a Recognizer instance
    rec = srp.Recognizer()

    # Use a microphone as the audio source
    with srp.Microphone() as source:
        # Notify the user that the AI is listening
        speak("I'm listening. Please speak.")

        # Set the pause threshold for audio input
        rec.pause_threshold = 1

        try:
            # Capture audio from the microphone
            audio = rec.listen(source)
        except srp.WaitTimeoutError:
            # Handle the case where there's a timeout (no speech detected)
            speak("Sorry, I didn't hear anything. Please try again.")
            return ""

    try:
        # Notify the user that the AI is recognizing the voice
        print("Recognizing the voice.")

        # Use Google Speech Recognition to convert audio to text
        query = rec.recognize_google(audio, language='en-us')
        return query

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

    # Return the recognized query
    return ""#query

'''
Below code is used to switch the tab and close the tab based on the user system
'''
#######################################
'''
"Darwin" in this context refers to the Darwin operating system kernel, which is the open-source Unix-like operating system core that underlies macOS. Apple's macOS is built on top of the Darwin operating system.
'''

########################
'''
Defining the all while loop function here
'''
# ##########################

# ########################################################
# Function to greet the user based on the time of day        
def greet_user():
    # Get the current time
    current_time = datetime.now()
    hour = current_time.hour

    # Greet the user based on the time of day
    if 3 <= hour < 12:
        speak("Good morning, sir!")
    elif 12 <= hour < 18:
        speak("Good afternoon, sir!")
    elif 18 <= hour < 24:
        speak("Good evening, sir!")
    else:
        speak("Good night, sir!")
# Greet the user
greet_user()


#######################END#################################
# Introduce the AI
speak("I'm Your Personal AI, My name is Rose")
speak("Hello Boss! How can I assist you today....?")


##################################
# Initialize app_name outside the loop
app_name = ""
# Initialize sleep mode state
sleep_mode = False

# While loop for user interactions
while True:
    query = command_from_user().lower()
    print('\nYou said: ' + query)

    if 'open' in query:
        app_name = query.replace('open', '')
        speak('opening ' + app_name)
        pyautogui.hotkey('command', 'space')
        pyautogui.typewrite(app_name)
        pyautogui.sleep(0.5)
        pyautogui.press('enter')

# Check if the query contains the word 'switch tab'
    elif 'switch right' in query:
        #pyautogui.hotkey('command','tab') #this line of code switch tab for mac
        #pyautogui.hotkey('alt','tab') #this line is for Win user
        #switchTab()
        pyautogui.hotkey('Ctrl','tab')
        time.sleep(2)
        speak('tab is switch sir')
        
    elif 'switch left' in query:
        #pyautogui.hotkey('command','tab') #this line of code switch tab for mac
        #pyautogui.hotkey('alt','tab') #this line is for Win user
        #switchTab()
        pyautogui.hotkey('Ctrl','shift','tab')
        time.sleep(2)
        speak('tab is switch sir')
        
    elif 'close tab' in query:
        #pyautogui.hotkey('command','w') #this line is to close the tab fro mac
        #pyautogui.hotkey('alt','w') #this line is for win user
        #closeTab()
        pyautogui.hotkey('command','w')
        time.sleep(2)
        speak('tab is closed sir')
        
    elif 'close' in query:
        pyautogui.hotkey('command','q')
        time.sleep(4)
        speak(app_name + ' is closed, sir')

# Check if the query contains the word 'Play'
    elif 'play' in query:
        song_name = query.replace('play', '')
        speak('As your command, sir. Playing ' + song_name + ' for you.')
        pywhatkit.playonyt(song_name)

# Check if the query contains the word 'time'
    elif 'time' in query:
        current_time = datetime.now().strftime('%I:%M %p')#Get the current time and format it as hh:mm AM/PM
        '''
%H: Represents the hour in 24-hour format (00 to 23).
%I: Represents the hour in 12-hour format (01 to 12).
%M: Represents the minute (00 to 59).
%p: Represents either AM or PM, depending on the time.
        '''
        speak('current time is '+ current_time)
        
#Stop and exit from the current window
    elif any(keyword in query for keyword in ['stop', 'exit', 'quit']): 
        speak('Goodbye, sir!')
        break
        
    elif 'search' in query:
        search_query = query.replace('search', '')
        speak(f"Searching the web for {search_query}")
        pywhatkit.search(search_query)

    elif 'sleep' in query:
        speak('As your command sir,' +'I''m going to sleep but you can call me anytime just you have to say wake up and I will be there for you')
        sleep_mode = True
        
    elif 'wake up' in query:
        speak('I am awake sir. How can i serve you sir!')

    else:
        speak("I'm not sure how to handle that, sir")

'''
Below step is used to stop the infinite while loop for stop
'''
# Cleanup code if needed
# Stop and quit the pygame.mixer
pygame.mixer.music.stop()
pygame.mixer.quit()   