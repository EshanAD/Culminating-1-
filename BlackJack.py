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

def createDeck():
        """ Creates a default deck which contains all 52 cards and returns it. """
    
        suits = ["s", "h", "c", "d"]
        values = ["j", "q", "k", "a"]
        values.extend(range(2, 11))

        deck = [f"{suit}{value}" for suit in suits for value in values]
        return deck

def returnFromDead(deck, garbageDeck):
      """ Appends the cards from the garbageDeck to the deck that is in play. This is called when the main deck has been emptied. """
  
      deck.extend(garbageDeck)
      del garbageDeck[:]
      random.shuffle(deck)
  
      return deck, garbageDeck
  
  
      handOfDealer, handOfPlayer = [], []
    
def deckDeal(deck, garbageDeck, handOfDealer, handOfPlayer):
      """ Shuffles the deck, takes the top 4 cards off the deck, appends them to the player's and dealer's hands, and returns the player's and dealer's hands. """
  
      deck = shuffle(deck)
  
      if len(deck) < 4:
          deck, garbageDeck = returnFromDead(deck, garbageDeck)
  
      for i in range(4):
          if i % 2 == 0:
              handOfPlayer.append(deck.pop(0))
          else:
              handOfDealer.append(deck.pop(0))
  
      return deck, garbageDeck, handOfPlayer, handOfDealer
  
      
          # Call the deckDeal function, passing the handOfDealer and handOfPlayer lists as arguments
      deck, garbageDeck = deckDeal(deck, garbageDeck, handOfDealer, handOfPlayer)
          
def hit(deck, garbageDeck, hand):
        """ Checks to see if the deck is gone, in which case it takes the cards from
        the dead deck (cards that have been played and discarded)
        and shuffles them in. Then if the player is hitting, it gives
        a card to the player, or if the dealer is hitting, gives one to the dealer."""
    
        # if the deck is empty, shuffle in the dead deck
        if len(deck) == 0:
            deck, garbageDeck = returnFromDead(deck, garbageDeck)
    
        hand.append(deck.pop(0))
    
        return deck, garbageDeck, hand

 def checkValue(hand):
      """ Checks the value of the cards in the player's or dealer's hand. """
  
      totalValue = 0
      num_aces = 0
  
      # check for natural blackjack (21 with just two cards)
      if len(hand) == 2:
          if hand[0][1:] == 'a' and hand[1][1:] in ('j', 'q', 'k'):
              return 21
          elif hand[1][1:] == 'a' and hand[0][1:] in ('j', 'q', 'k'):
              return 21
  
      for card in hand:
          value = card[1:]
  
          # Jacks, kings and queens are all worth 10, and aces are worth 11
          if value == 'j' or value == 'q' or value == 'k':
              value = 10
          elif value == 'a':
              value = 11
              num_aces += 1
          else:
              value = int(value)
  
          totalValue += value
#Finish function