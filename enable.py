def enable_rose_ai():
    """
    Function to enable Rose AI and provide a welcome message.

    Returns:
        str: A welcome message indicating that Rose AI is now enabled.
    """
    return "Hello! Rose AI is now enabled."

def main():
    try:
        # Get user input
        user_input = input("Say something: ")

        # Check if the user input is a greeting
        if user_input.strip().lower() == "hi":
            response = enable_rose_ai()
            print(response)
        else:
            print("No special action taken.")
    
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("\nProgram terminated by user.")
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
