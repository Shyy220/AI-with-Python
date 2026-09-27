print("Hello! I am an AI bot. Whats your name? :")
name = input()

print(f"Nice to meet you, {name}!")

print("How are you feeling today? (good/bad) : ")
mood = input().lower()


if mood == "good":
    print("im glad to hear that!")
elif mood == "bad":
    print("Im so sorry to hear that, hope things get better soon!!")
else:
    print("I see! Sometimes its hard to put feelings into words.")
print("What is your favourite school subject?")
subject = input().lower()

if subject == "math":
    print("Math is a great subject!")
elif subject == "science":
    print("Science is really interesting!")
else:
    print(f"{subject.capitalize()} sounds fun!")
    print(f"It was nice chatting with you {name}. Goodbye