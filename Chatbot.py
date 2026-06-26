# Task 4: Basic Chatbot
# CodeAlpha Python Programming Internship
# Author: [Karan Kumar]

def get_response(user_input):
    """
    Returns a response based on user input.
    Uses if-elif-else to match keywords.
    """
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you today?"

    elif user_input in ["how are you", "how are you doing", "how r u"]:
        return "I'm doing great, thanks for asking! How about you?"

    elif user_input in ["i am fine", "i'm fine", "i'm good", "good", "fine"]:
        return "That's wonderful to hear!"

    elif user_input in ["what is your name", "who are you", "your name"]:
        return "I'm CodeBot, a simple chatbot created as part of the CodeAlpha internship!"

    elif user_input in ["what can you do", "What is your task", "help", "features"]:
        return ("I can have a basic conversation with you!\n"
                "        Try saying: hello, how are you, bye, etc.")

    elif user_input in ["who created you", "who made you"]:
        return "I was created by [Karan] as part of the CodeAlpha Python Internship."

    elif user_input in ["bye", "goodbye", "see you", "exit", "quit"]:
        return "EXIT"

    else:
        return "I'm sorry, I didn't quite understand that. Could you rephrase?"


def display_welcome():
    print("=" * 45)
    print("       Welcome to CodeBot - CodeAlpha")
    print("=" * 45)
    print("  Type 'help' to see what I can do.")
    print("  Type 'bye' to exit the chatbot.")
    print("=" * 45)
    print()


def main():
    display_welcome()

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                print("Bot: Please type something!\n")
                continue

            response = get_response(user_input)

            if response == "EXIT":
                print("Bot: Goodbye! Have a great day. ")
                print("=" * 45)
                break

            print(f"Bot: {response}\n")

        except KeyboardInterrupt:
            print("\nBot: Session ended. Goodbye!")
            break


if __name__ == "__main__":
    main()
