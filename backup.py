import os
import pygame
import pyautogui
import pywhatkit
from datetime import datetime
import time
import speech_recognition as srp
import Youtube_skip
import requests
from pyfiglet import Figlet
from termcolor import colored
import emoji
import random
import threading
import wikipedia

# Define your text with emoji
text_with_emoji = "R O S E"

# Pass the text to figlet_format() function
f = Figlet(font='3-d',width=1080)
rendered_text = f.renderText(text_with_emoji)

# Append the emoji to the rendered text
emoji = "🌹" * 10
text_with_emoji = rendered_text.strip() + "\n" + emoji

# Apply color to the combined text
colored_text = colored(text_with_emoji, color='blue')  # You can choose any color you want

# Print the colored text
print(colored_text)


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
        print("I'm listening. please speak!")
        # rec.pause_threshold = 0.5 #if pause if more than .5sec it assume speech is finish and start searching 

        try:
            audio = rec.listen(source)
            print("Analyzing the voice...!")
            query_general = rec.recognize_google(audio, language='en-us')

        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}")
            return ""

    # Return the recognized query_general
    return query_general

def greet_user():
    current_time = datetime.now().hour
    if 3 <= current_time < 12:
        speak("Good morning, sir!")
    elif 12 <= current_time < 18:
        speak("Good afternoon, sir!")
    else:
        speak("Good evening, sir!")

def rose_greeting():
    speak("I'm Your Personal AI, My name is Rose")
    speak("Master, How can I assist you today")

# Define a flag to indicate whether rose_intro is currently running
rose_intro_running = False

def rose_intro():
    developer_name = "Shivam Goyal"
    age = "I don't have an age. I am just an AI program."
    name_preference = ["Yes, I like my name!", "My name serves its purpose.", "I don't have feelings, but my name is functional."]
    
    # Updated possible questions and corresponding answers
    questions = {
        "who created you": f"I was created by {developer_name}.",
        "what is your developer name": f"My developer's name is {developer_name}.",
        "what is your age": age,
        "do you like your name": random.choice(name_preference),
        "what can you do": "I can perform various tasks such as opening applications, playing music, providing news updates, and much more. Just let me know what you need!",
        "how are you feeling": "As an AI, I don't have feelings, but I'm here and ready to assist you!",
        "where are you located": "I exist in the digital realm, always ready to assist you wherever you are!",
        "what is your purpose": "My purpose is to assist you with tasks, answer your questions, and make your life easier.",
        "can you tell me a joke": "Sure! Why don't scientists trust atoms? Because they make up everything!",
        "can you sing a song": "I'm sorry, I'm not programmed to sing, but I can play music for you!",
        "do you have any siblings": "As an AI, I don't have siblings, but I'm here solely for you!",
        "what languages do you speak": "I can communicate in various languages including English, Spanish, French, German, Italian, and more!",
        "can you do math": "Yes, I can perform basic arithmetic operations like addition, subtraction, multiplication, and division.",
        "can you help me with my homework": "Of course! I can provide explanations, help you understand concepts, and guide you through problems.",
        "what is the meaning of life": "The meaning of life is subjective and varies from person to person. Some believe it's about happiness, others about fulfillment. What do you think?",
        "other stuff": "I'm here to assist you with any questions you have!"
    }
    
    while True:
        speak("What do you wanna know?")
        user_input = command_from_user().lower()
        
        if 'you can stop now' in user_input:
            speak("I hope my answers satisfy you!")
            break
        
        if user_input in questions:
            speak(questions[user_input])
        else:
            speak("I'm not sure how to answer that.")

def process_open_command(query_general):
    app_name = query_general.replace('open', '')
    speak(f'opening {app_name}')
    with pyautogui.hold('command'):
        pyautogui.press('space')
    pyautogui.typewrite(app_name)
    pyautogui.sleep(0.2)
    pyautogui.press('enter')

def process_switch_tab_command_right(query_general):
    pyautogui.hotkey('Ctrl','tab')
    time.sleep(2)
    speak('tab is switched sir')

def process_switch_tab_command_left(query_general):
    pyautogui.hotkey('Ctrl','shift','tab')
    time.sleep(2)
    speak('tab is switched sir')

def process_close_tab_command(query_general):
    with pyautogui.hold('command'):
        pyautogui.press('w')
    time.sleep(0.5)
    speak('tab is closed sir')

def process_close_app_command(query_general, app_name):
    with pyautogui.hold('command'):
        time.sleep(4)
        pyautogui.press('q')
    time.sleep(4)
    speak(f'{app_name} is closed, sir')

def process_play_command(query_general):
    song_name = query_general.replace('play', '')
    try:
        speak(f'As your command, sir. Playing {song_name} for you.')
        pywhatkit.playonyt(song_name)
        time.sleep(10)
        #click_skip_ad_button()

    except Exception as e:
        speak("Sorry, there was an issue playing the requested song")
    
    # speak(f'As your command, sir. Playing {song_name} for you.')
    # pywhatkit.playonyt(song_name)
    time.sleep(10)  # Assuming 10 seconds for the video to start, adjust as needed
    # click_skip_ad_button()

def get_current_time():
    current_time = datetime.now().strftime('%I:%M %p')
    return current_time

def process_time_command():
    current_time = get_current_time()
    speak(f'The current time is {current_time}')

# Additional functions for handling other commands...

def click_skip_ad_button():
    try:
        ad_text_path = '//*[@id="ad-text:7"]' # XPath for skip ad
        skip_button_location = pyautogui.locateCenterOnScreen(ad_text_path)
        if skip_button_location is not None:
            pyautogui.click(skip_button_location)
        else:
            speak("Skip button not found on the screen. You may need to wait for the ad to finish or handle it manually.")

    except Exception as e:
        print("Error clicking the skip ad button:", e)

def news(language_code, country_code):
    news_api = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=3bb710bf6d6747a69cb404799be74b32'
    
    params = {
        "country": country_code,
        "language": language_code,
        "apiKey": news_api
    }

    response = requests.get(news_api, params=params)
    data = response.json()

    return data

###############################################################################################################        

# query_youtube_skip = ""
def main():
    app_name = ""

    sleeping_mode = False # Flag to indicate if AI is in sleep mode
    
    greet_user()
    rose_greeting()

    while True:
        query_general = command_from_user().lower()

        print('\nYou said (General):', query_general)
        #print('\nYou said (YouTube skip):', query_youtube_skip)

        if 'tell me about you' in query_general and not rose_intro_running:
            # Start rose_intro in a separate thread
            threading.Thread(target=rose_intro).start()

        elif 'open' in query_general:
            process_open_command(query_general)

        elif 'search' in query_general:
            search_query_general = query_general.replace('search', '')
            try:
                speak(f"Searching the web for {search_query_general}")
                pywhatkit.search(search_query_general)
            except Exception as e:
                speak("Sorry, there was an issue with the search.")

        elif 'wikipedia' in query_general:
            speak('searching on wikipedia.....!')
            query_general = query_general.replace("wikipedia","")
            result=wikipedia.summary(query_general, sentence=2)
            speak("according to wikipedia")
            speak(result)
        
        elif 'switch right' in query_general:
            process_switch_tab_command_right(query_general)

        elif 'switch left' in query_general:
            process_switch_tab_command_left(query_general)
            
        elif 'close tab' in query_general:
            process_close_tab_command(query_general)

        elif f'close the {app_name}' in query_general:
            process_close_app_command(query_general, app_name)

        elif 'play' in query_general:
            process_play_command(query_general)
        
        elif 'time' in query_general:
            process_time_command()
            
            # Sleep mode commands
        elif 'sleep' in query_general:
            speak("I am going to sleep mode, but you can call me anytime just say the word wake up and i will assist you again!")
            sleeping_mode = True
            
        elif 'news' in query_general:
            language_mapping = {
                "english": "en",
                "hindi": "hi",
                "spanish": "es",
                "french": "fr",
                "german": "de",
                "italian": "it",
                "danish": "da",
                # Add more languages as needed
            }

            # Prompt the user to specify a supported language for news
            speak("Which language would you like to hear the news in?")
            available_languages = ", ".join(language_mapping.keys())
            speak(f"You can choose from the following languages: {available_languages}")
    
            while True:
                user_input = command_from_user().lower()
                user_language = None
                for lang in language_mapping:
                    if lang in user_input:
                        user_language = lang
                        break

                if user_language:
                    language_code = language_mapping[user_language]
                    break
                else:
                    print("Sorry, I didn't catch that. Please specify a language from the options provided.")

            country_code = ""  # Adjust country code as needed

            news_data = news(language_code, country_code)
            articles = news_data['articles']

            for i, article in enumerate(articles[:5]):
                speak(f"Today's {i + 1} news is: {article['title'],}", language_code)
                response = command_from_user().lower()
                if 'stop' in response:
                    print("Alright, stopping the news.")
                    break

        elif any(keyword in query_general for keyword in ['stop', 'exit', 'quit', 'by rose']):
            speak('Thank you for using rose ai, have a great day, sir!')
            speak('If you need assistance in the future, feel free to call upon me. Goodbye!')
            break

        else:
            # speak("I'm not sure how to handle that, sir")
            pass
        
        while sleeping_mode:
            query_general = command_from_user().lower()
            if 'wake up' in query_general:
                speak('I am awake now sir, How may i assist you')
                sleeping_mode = False # Exit sleep mode and resume normal operation

    # Cleanup code if needed
    pygame.mixer.music.stop()
    pygame.mixer.quit()

if __name__ == "__main__":
    main()
    
    
