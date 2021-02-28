'''
CS 5003 Recital
Fall 2019
Lab 3
'''

from lab3_part2_sentiment_function import analysis


AQUAMAN_REVIEWS = ["Doesn't hold a candle to Wonder Woman", "Good movie to watch", "Arthur Curry is a lame joke no longer", "It is a good superhero and special effects extravaganza", "So reliant upon a British legend that you don’t know why the people who made this movie bothered", "The travelogue stuff coral-colored pretty as it is can only take you so far before boredom sets in", "Aquaman is as formulaic excessively thrashy, as any other entry in the DCEU but its imagination is exciting and transportive and dare I say fun", "Jason Momoa tosses off coy one-liners with humor that goes to waste in this bloated and sludgy movie", "A thoroughly entertaining ride", "A very fun movie to watch, and it exceeded all of my expectations", "It's a hoot", "some of the worst dialogue I can remember from these capes and tights exercises"]
BATMAN_V_SUPERMAN_REVIEWS = ["a tiresome, ill-tempered film, and one too lazy even to earn its dismal outlook", "DC comic fans will try to do mental gymnastics to describe the crap biscuit they were just force-fed", "Wondering how to teach your offspring that the world is a horrifying, random, awful place?", "Completely misunderstood. This is a great comic book movie", "This is awesome, and the city of this film just like in comicbook", "99% unenjoyable garbage", "It's basically a hot-mess", "To put it bluntly, this sucked"] 

def main():

    liked = 0
    disliked = 0

    for words in AQUAMAN_REVIEWS:
        words = words.split()

        reviews = analysis(words)

        if reviews > 0:
            liked += 1
        elif reviews < 0:
            disliked += 1

    print(liked, "people liked the movie and ", disliked, " people disliked the movie. The rest were neutral")


    for words2 in BATMAN_V_SUPERMAN_REVIEWS:
        words2 = words2.split()
        reviews = analysis(words2)

        if reviews > 0:
            liked += 1
        elif reviews < 0:
            disliked += 1

    print(liked, "people liked the movie and ", disliked, " people disliked the movie. The rest were neutral")


main()