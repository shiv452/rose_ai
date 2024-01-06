# Importing necessary libraries
import os
import pygame

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


speak("Hello their! I'm Your Personal A I, My name is Rose")
speak("Hey Boss! How can I help you today!")

