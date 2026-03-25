from textblob import TextBlob

while True:
    text = input("\nEnter text (or type 'exit'): ")

    if text.lower() == "exit":
        print("Exiting...")
        break

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    print(f"Polarity Score: {polarity}")

    if polarity > 0:
        print("Sentiment: Positive 😊")
    elif polarity < 0:
        print("Sentiment: Negative 😡")
    else:
        print("Sentiment: Neutral 😐")