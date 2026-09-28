import re, random
from colorama import Fore, init


init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["tokyo", "paris", "NYC"]
    }

jokes = [
    "Why don't the programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus"
    "Why do travellers always feel warm? Because of all their hot spots!"
]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def reccomended():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You:")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestions = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestions}?")
        print(Fore.CYAN + "TravelBot: Do you like it?(yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
           print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestions}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another.")
            reccomended()
        else:
             print(Fore.RED + "TravelBot:, Sorry, I don't have that type of destination.")
             reccomended()

def packing_tips:
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You:  "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack Versatile clothes. ")
    print(Fore.GREEN + "- Check the weather forecast.")

def tell_joke():
     print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}]")
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "-Suggest travel spots (say 'reccomendation')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

def chat
    print(Fore.CYAN + "Hello! Im TravelBot.")
    name = input(Fore.YELLOW + "Your name?")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:
      user_input = input(Fore.YELLOW + f"{name}: ")
      user_input = normalize_input(user_input)

      if "reccomend" in user_input or "suggest" in user_input:
        reccomended()
      elif "pack" in user_input or "packing" in user_input:
         packing_tips()
      elif "joke" in user_input or "funny" in user_input:
         tell_joke()
      elif "help" in user_input:
          show_help()
      elif "exit" in user_input or "bye" in user_input:
          print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
          break
      else:
          print(Fore.RED + "TravelBot: Could you rephrase?")

if __name__ == "__main__":
   chat()
