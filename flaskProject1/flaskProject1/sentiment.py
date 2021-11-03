# VADER sentiment analysis
# import SentimentIntensityAnalyzer class
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# function to print sentence sentiments
def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # create sentiment dictionary with polarity scores
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")

    print("Sentence Overall Rated As", end=" ")

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        print("Positive")

    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative")

    else:
        print("Neutral")


# Driver code
if __name__ == "__main__":
    print("\n1st statement :")
    sentence = "i love johnny depp"

    # function calling
    sentiment_scores(sentence)

    print("\n2nd Statement :")
    sentence = "watching the new johnny depp movie"
    sentiment_scores(sentence)

    print("\n3rd Statement :")
    sentence = "i hate johnny depp"
    sentiment_scores(sentence)