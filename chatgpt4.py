import g4f
import re
from g4f.gui import *

# Sample messages for testing
messages = [
    {'role': 'system', 'content': 'Hi'},
    {'role': 'system', 'content': 'naa'}
]

def gpt_process(*args):
    """
    Process input messages using GPT-4 model.

    Args:
        *args (str): Input messages.

    Returns:
        str: Generated response.
    """

    # Ensure that input arguments are provided
    assert args

    # Convert the global variable 'messages' to a list
    global messages

    # Concatenate input messages into a single string
    input_message = ''.join(args)

    # Append the user's input to the messages list
    messages.append({'role': 'user', 'content': input_message})

    # Use g4f library to create a chat completion
    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0631",
        provider=g4f.Provider.Bing,
        messages=messages,
        stream=True
    )

    # Initialize an empty string to store the response
    generated_response = ""

    # Iterate over the response and print each part
    for part in response:
        generated_response += part
        print(part, end="", flush=True)

    # Append the generated response to the messages list
    messages.append({'role': 'user', 'content': generated_response})

    return generated_response

# Example usage
result = gpt_process('Who are you?')

