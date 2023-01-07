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
        # if hand value exceeds 21, reduce the value of each ace by 10 until the hand value is 21 or less
      if totalValue > 21:
          for card in hand:
              if card[1:] == 'a':
                  totalValue -= 10
                  num_aces -= 1
              if totalValue <= 21:
                  break
              elif num_aces == 0:
                  break
              else:
                  continue
      
      return totalValue
def blackJack(deck, garbageDeck, handOfPlayer, handOfDealer, funds, bet, cards,cardSprite):
        """ Called when the player or the dealer is determined to have blackjack. Hands are compared to determine the outcome. """

        textFont = pygame.font.Font(None, 28)

        playerValue = checkValue(handOfPlayer)
        dealerValue = checkValue(handOfDealer)

        if playerValue == 21 and dealerValue == 21:
            # The opposing player ties the original blackjack getter because he also has blackjack
            # No money will be lost, and a new hand will be dealt
            displayFont = display(
                textFont,
                "Blackjack! The dealer also has blackjack, so it's a push!")
            deck, handOfPlayer, handOfDealer, garbageDeck, funds, roundEnd = endRound(
                deck, handOfPlayer, handOfDealer, garbageDeck, funds, 0, bet, cards,
                cardSprite)

        elif playerValue == 21 and dealerValue != 21:
            # Dealer loses
            displayFont = display(textFont,
                                  "Blackjack! You won $%.2f." % (bet * 1.5))
            deck, handOfPlayer, handOfDealer, garbageDeck, funds, roundEnd = endRound(
                deck, handOfPlayer, handOfDealer, garbageDeck, funds, bet, 0, cards,
                cardSprite)

        elif dealerValue == 21 and playerValue != 21:
            # Player loses, money is lost, and new hand will be dealt
            deck, handOfPlayer, handOfDealer, garbageDeck, funds, roundEnd = endRound(
                deck, handOfPlayer, handOfDealer, garbageDeck, funds, 0, bet, cards,
                cardSprite)
            displayFont = display(
                textFont, "Dealer has blackjack! You lose $%.2f." % (bet))

        return displayFont, handOfPlayer, handOfDealer, garbageDeck, funds, roundEnd
  
def bust(deck, handOfPlayer, handOfDealer, garbageDeck, funds, moneyGained,moneyLost, cards, cardSprite):
      """ This is only called when player busts by drawing too many cards. """
  
      font = pygame.font.Font(None, 28)
      playerValue = checkValue(handOfPlayer)
      if playerValue > 21:
          displayFont = display(font, "You bust! You lost $%.2f." % (moneyLost))
          deck, handOfPlayer, handOfDealer, garbageDeck, funds, roundEnd = endRound(
              deck, handOfPlayer, handOfDealer, garbageDeck, funds, moneyGained,
              moneyLost, cards, cardSprite)
      else:
          displayFont = None
          roundEnd = False
  
      return deck, handOfPlayer, handOfDealer, garbageDeck, funds, roundEnd, displayFont

#Check if I need this calculations (Will keep them for now just in case)
def endRound(deck, handOfPlayer, handOfDealer, garbageDeck, funds, moneyGained, moneyLost, cards, cardSprite):
      """Called at the end of a round to determine what happens to the cards, the money gained or lost,and such. It also shows the dealer's hand to the player, by deleting the old sprites and showing all the cards."""
      if len(handOfPlayer) >= 2:
        if "a" in handOfPlayer[0] or "a" in handOfPlayer[1]:
          # If the player has blackjack, pay his bet back 3:2
          moneyGained += (moneyGained / 2.0)
      # Remove old dealer's cards and display the new ones
      cards.empty()
      dealer_card_pos = (75, 100)
      for card in handOfDealer:
          card_obj = cardSprite(card, dealer_card_pos)
          dealer_card_pos = (dealer_card_pos[0] + 110, dealer_card_pos[1])
          cards.add(card_obj)
  
      # Add the cards from the player's and dealer's hands to the discard pile
      garbageDeck.extend(handOfPlayer)
      garbageDeck.extend(handOfDealer)
  
      # Clear the player's and dealer's hands
      handOfPlayer.clear()
      handOfDealer.clear()
  
      # Update the player's funds
      funds += moneyGained
      funds -= moneyLost
  
      textFont = pygame.font.Font(None, 28)
  
      if funds <= 0:
        if exitButton.rect.collidepoint(mX, mY) == 1:
          m.main_menu()

  
      roundEnd = 1
  
      return deck, handOfPlayer, handOfDealer, garbageDeck, funds, roundEnd

def handComparison(deck, garbageDeck, handOfPlayer, handOfDealer, funds, bet, cards,
                     cardSprite):
        """ Called at the end of a round (after the player stands), or at the beginning of a round
        if the player or dealer has blackjack. This function compares the values of the respective hands of
        the player and the dealer and determines who wins the round based on the rules of blacjack. """

        textFont = pygame.font.Font(None, 28)
        # How much money the player loses or gains, default at 0, changed depending on outcome
        moneyGained = 0
        moneyLost = 0

        dealerValue = checkValue(handOfDealer)
        playerValue = checkValue(handOfPlayer)

        # Dealer hits until he has 17 or over
        while 1:
            if dealerValue < 17:
                # dealer hits when he has less than 17, and stands if he has 17 or above
                deck, garbageDeck, handOfDealer = hit(deck, garbageDeck, handOfDealer)
                dealerValue = checkValue(handOfDealer)
            else:
                # dealer stands
                break

        if playerValue > dealerValue and playerValue <= 21:
            # Player has beaten the dealer, and hasn't busted, therefore WINS
            moneyGained = bet
            deck, handOfPlayer, handOfDealer, garbageDeck, funds, roundEnd = endRound(
                deck, handOfPlayer, handOfDealer, garbageDeck, funds, bet, 0, cards,
                cardSprite)
            displayFont = display(textFont, "You won $%.2f." % (bet))
        elif playerValue == dealerValue and playerValue <= 21:
            # Tie
            deck, handOfPlayer, handOfDealer, garbageDeck, funds, roundEnd = endRound(
                deck, handOfPlayer, handOfDealer, garbageDeck, funds, 0, 0, cards,
                cardSprite)
            displayFont = display(textFont, "It's a push!")
        elif dealerValue > 21 and playerValue <= 21:
            # Dealer has busted and player hasn't
            deck, handOfPlayer, handOfDealer, garbageDeck, funds, roundEnd = endRound(
                deck, handOfPlayer, handOfDealer, garbageDeck, funds, bet, 0, cards,
                cardSprite)
            displayFont = display(textFont,
                                  "Dealer busts! You won $%.2f." % (bet))
        else:
            # Dealer wins in every other siutation taht i can think of
            deck, handOfPlayer, handOfDealer, garbageDeck, funds, roundEnd = endRound(
                deck, handOfPlayer, handOfDealer, garbageDeck, funds, 0, bet, cards,
                cardSprite)
            displayFont = display(textFont,
                                  "Dealer wins! You lost $%.2f." % (bet))

        return deck, garbageDeck, roundEnd, funds, displayFont
