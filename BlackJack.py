import os
import pygame
import random
def loadImage(name, card):
    """Function that loads an card images based on their name. Raises an exception if card can't be loaded"""

    if card == 1:
        fullname = os.path.join("images/cards/", name)
    else:
        fullname = os.path.join('images', name)

    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()

    return image, image.get_rect()

def displayText(font, sentence):
    """ Function displaying text located at the bottom of the screen"""

    displayFont = pygame.font.Font.render(font, sentence, 1, (255, 255, 255),
                                          (0, 0, 0))
    return displayFont

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