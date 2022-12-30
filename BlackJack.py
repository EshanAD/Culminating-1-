import os
import pygame
import random
def imageLoad(imgName, cardNum):
    """
    This function loads an image file and returns it, along with its rectangle object.
    If there is an issue loading the image, it will raise an exception.
    """

    imgDir = "images/cards/" if cardNum == 1 else "images"
    fullPath = os.path.join(imgDir, imgName)

    try:
        img = pygame.image.load(fullPath)
    except pygame.error as err:
        print(f"Unable to load image: {imgName}")
        raise SystemExit(err)

    img = img.convert()
    return img, img.get_rect()


def display(font, sentence):
    """
    This function displays a message at the bottom of the screen, using the specified font.
    The message will be white text on a black background.
    """

    textSurface = font.render(sentence, True, (255, 255, 255), (0, 0, 0))
    return textSurface



def shufflerDeck(deck):
        """ Shuffles the deck using the Fisher-Yates shuffling algorithm. In this code n is equal to the length of the deck - 1 since lists start at 0 not 1. When n > 0, a random number represented by k between 0 and n is created, and the card in the deck that is represented by the n just created is swapped with the card in the deck
represented by the k just created. After this finishes n is decreased by 1 as the loop repeates"""

        n = len(deck) - 1
        while n > 0:
            k = random.randint(0, n)
            deck[k], deck[n] = deck[n], deck[k]
            n -= 1

        return deck

def Deck():
        """ A deck with a default of 52 cards is created and is returned"""

        deck = [
            'sj', 'sq', 'sk', 'sa', 'hj', 'hq', 'hk', 'ha', 'cj', 'cq', 'ck',
            'ca', 'dj', 'dq', 'dk', 'da'
        ]
        deckvalues = range(2, 11)
        for x in deckvalues:
            spades = "s" + str(x)
            hearts = "h" + str(x)
            clubs = "c" + str(x)
            diamonds = "d" + str(x)
            deck.append(spades)
            deck.append(hearts)
            deck.append(clubs)
            deck.append(diamonds)
        return deck