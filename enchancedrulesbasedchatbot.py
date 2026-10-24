
import random
from colorama import Fore, init

init(autoreset=True)

def chatbot():
    print(Fore.GREEN + "Chatbot: Hello! I am your chatbot.")

    name = input("What is your name? ")
    print(Fore.CYAN + "Chatbot: Nice to meet you, " + name + "!")

    while True:
        message = input(Fore.YELLOW + "You: ").lower()

        if "hello" in message or "hi" in message:
            print(Fore.CYAN + "Chatbot: Hello! How are you?")

        elif "how are you" in message:
            print(Fore.CYAN + "Chatbot: I am doing great!")

        elif "weather" in message:
            print(Fore.CYAN + "Chatbot: It is sunny and warm today!")

        elif "news" in message:
            print(Fore.CYAN + "Chatbot: Here is some news: Scientists are making new discoveries!")

        elif "time" in message:
            print(Fore.CYAN + "Chatbot: The time in Chennai is 10:30 AM. (Example)")

        elif "joke" in message:
            jokes = [
                "Why did the computer go to the doctor? It had a virus!",
                "Why was the math book sad? It had too many problems!",
                "Why did the student eat his homework? The teacher said it was a piece of cake!"
            ]
            print(Fore.CYAN + "Chatbot: " + random.choice(jokes))

        elif "thank" in message:
            print(Fore.CYAN + "Chatbot: You're welcome!")

        elif "bye" in message:
            print(Fore.CYAN + "Chatbot: Goodbye, " + name + "!")
            break

        else:
            print(Fore.RED + "Chatbot: Sorry, I don't understand.")

chatbot()
