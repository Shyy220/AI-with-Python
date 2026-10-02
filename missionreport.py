
print("Welcome to the Sentiment Analysis Chatbot!")
print("Type 'stats', 'history', 'reset', or 'exit'.")

positive = ["happy", "good", "great", "love", "awesome"]
negative = ["sad", "bad", "hate", "angry", "terrible"]

pos = 0
neg = 0
neu = 0
history = []

while True:
    message = input("\nYou: ").lower()

    if message == "exit":
        break

    elif message == "stats":
        print("Positive:", pos)
        print("Negative:", neg)
        print("Neutral:", neu)

    elif message == "history":
        print(history)

    elif message == "reset":
        pos = 0
        neg = 0
        neu = 0
        history = []
        print("Data reset!")

    else:
        if any(word in message for word in positive):
            sentiment = "Positive"
            pos += 1

        elif any(word in message for word in negative):
            sentiment = "Negative"
            neg += 1

        else:
            sentiment = "Neutral"
            neu += 1

        print("Sentiment:", sentiment)
        history.append((message, sentiment))

print("\n===== FINAL REPORT =====")
print("Positive messages:", pos)
print("Negative messages:", neg)
print("Neutral messages:", neu)
print("Total messages:", pos + neg + neu)
print("Thank you for chatting!")
