from colorama import Fore, init

init()

text = input("Enter your sentence: ")

positive_words = ["love", "good", "great","happy","awesome"]
negative_words = ["hate", "bad", "sad", "worst", "terrible"]

words = text.lower().split()

positive_count = 0
negative_count = 0

for word in words:

    if word in positive_words:
        positive_count += 1

    if word in negative_words:
        negative_count += 1

if positive_count > negative_count:
    print(Fore.GREEN + "😀Positive Sentiment")

elif negative_count > positive_count:
    print(Fore.RED + "😡Negative Sentiment")

else:
    print(Fore.YELLOW + "😕Neutral Sentiment")