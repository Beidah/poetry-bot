import random

from chain import get_chain

chain = get_chain()


def get_tweet():
    tweet = ""
    start1, start2 = random.choice(list(chain.keys()))

    tweet += start1 + " " + start2

    while True:
        try:
            next_word = random.choice(chain[(start1, start2)])
        except KeyError:
            return tweet
        if len(tweet) + len(next_word) + 1 <= 280:
            tweet += " " + next_word
            start1, start2 = start2, next_word
        else:
            break

    return tweet
