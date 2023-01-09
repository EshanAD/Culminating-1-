class cardSprite(pygame.sprite.Sprite):
        """ Sprite that displays a specific card. """

        def __init__(self, card, position):
            pygame.sprite.Sprite.__init__(self)
            cardImage = card + ".png"
            self.image, self.rect = imageLoad(cardImage, 1)
            self.position = position

        def update(self):
            self.rect.center = self.position

    class hitButton(pygame.sprite.Sprite):
        """ Button that allows player to hit (take another card from the deck). """

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image, self.rect = imageLoad("hit-grey.png", 0)
            self.position = (735, 400)

        def update(self, mX, mY, deck, deadDeck, playerHand, cards, pCardPos,
                   roundEnd, cardSprite, click):
            """ If the button is clicked and the round is NOT over, Hits the player with a new card from the deck. It then creates a sprite
            for the card and displays it. """

            if roundEnd == 0: self.image, self.rect = imageLoad("hit.png", 0)
            else: self.image, self.rect = imageLoad("hit-grey.png", 0)

            self.position = (500, 400)
            self.rect.center = self.position

            if self.rect.collidepoint(mX, mY) == 1 and click == 1:
                if roundEnd == 0:
                    deck, deadDeck, playerHand = hit(deck, deadDeck,
                                                     playerHand)

                    currentCard = len(playerHand) - 1
                    card = cardSprite(playerHand[currentCard], pCardPos)
                    cards.add(card)
                    pCardPos = (pCardPos[0] - 80, pCardPos[1])

                    click = 0

            return deck, deadDeck, playerHand, pCardPos, click

    class standButton(pygame.sprite.Sprite):
        """ Button that allows the player to stand (not take any more cards). """

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image, self.rect = imageLoad("stand-grey.png", 0)
            self.position = (735, 365)

        def update(self, mX, mY, deck, deadDeck, playerHand, dealerHand, cards,
                   pCardPos, roundEnd, cardSprite, funds, bet, displayFont):
            """ If the button is clicked and the round is NOT over, let the player stand (take no more cards). """

            if roundEnd == 0: self.image, self.rect = imageLoad("stand.png", 0)
            else: self.image, self.rect = imageLoad("stand-grey.png", 0)

            self.position = (500, 365)
            self.rect.center = self.position

            if self.rect.collidepoint(mX, mY) == 1:
                if roundEnd == 0:
                    deck, deadDeck, roundEnd, funds, displayFont = handComparison(
                        deck, deadDeck, playerHand, dealerHand, funds, bet,
                        cards, cardSprite)

            return deck, deadDeck, roundEnd, funds, playerHand, deadDeck, pCardPos, displayFont
class doubleButton(pygame.sprite.Sprite):
        """ Button that allows player to double (double the bet, take one more card, then stand)."""

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image, self.rect = imageLoad("double-grey.png", 0)
            self.position = (735, 330)

        def update(self, mX, mY, deck, deadDeck, playerHand, dealerHand,
                   playerCards, cards, pCardPos, roundEnd, cardSprite, funds,
                   bet, displayFont):
            """ If the button is clicked and the round is NOT over, let the player stand (take no more cards). """

            if roundEnd == 0 and funds >= bet * 2 and len(playerHand) == 2:
                self.image, self.rect = imageLoad("double.png", 0)
            else:
                self.image, self.rect = imageLoad("double-grey.png", 0)

            self.position = (500, 330)
            self.rect.center = self.position

            if self.rect.collidepoint(mX, mY) == 1:
                if roundEnd == 0 and funds >= bet * 2 and len(playerHand) == 2:
                    bet = bet * 2
                    deck, deadDeck, playerHand = hit(deck, deadDeck,
                                                     playerHand)

                    currentCard = len(playerHand) - 1
                    card = cardSprite(playerHand[currentCard], pCardPos)
                    playerCards.add(card)
                    pCardPos = (pCardPos[0] - 80, pCardPos[1])

                    deck, deadDeck, roundEnd, funds, displayFont = compareHands(
                        deck, deadDeck, playerHand, dealerHand, funds, bet,
                        cards, cardSprite)

                    bet = bet / 2

            return deck, deadDeck, roundEnd, funds, playerHand, deadDeck, pCardPos, displayFont, bet

    class dealButton(pygame.sprite.Sprite):
        """ A button on the right hand side of the screen that can be clicked at the end of a round to deal a
        new hand of cards and continue the game. """

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image, self.rect = imageLoad("deal.png", 0)
            self.position = (500, 450)

        def update(self, mX, mY, deck, deadDeck, roundEnd, cardSprite, cards,
                   playerHand, dealerHand, dCardPos, pCardPos, displayFont,
                   playerCards, click, handsPlayed):
            """ If the mouse position collides with the button, and the mouse is clicking, and roundEnd does not = 0,
            then Calls deckDeal to deal a hand to the player and a hand to the dealer. It then
            takes the cards from the player's hand and the dealer's hand and creates sprites for them,
            placing them on the visible table. The deal button can only be pushed after the round has ended
            and a winner has been declared. """

            # Get rid of the in between-hands chatter
            textFont = pygame.font.Font(None, 28)

            if roundEnd == 1: self.image, self.rect = imageLoad("deal.png", 0)
            else: self.image, self.rect = imageLoad("deal-grey.png", 0)

            self.position = (500, 450)
            self.rect.center = self.position

            if self.rect.collidepoint(mX, mY) == 1:
                if roundEnd == 1 and click == 1:
                    displayFont = display(textFont, "")

                    cards.empty()
                    playerCards.empty()

                    deck, deadDeck, playerHand, dealerHand = deckDeal(
                        deck, deadDeck)

                    dCardPos = (50, 70)
                    pCardPos = (360, 340)

                    # Create player's card sprites
                    for x in playerHand:
                        card = cardSprite(x, pCardPos)
                        pCardPos = (pCardPos[0] - 80, pCardPos[1])
                        playerCards.add(card)

                    # Create dealer's card sprites
                    faceDownCard = cardSprite("back", dCardPos)
                    dCardPos = (dCardPos[0] + 80, dCardPos[1])
                    cards.add(faceDownCard)

                    card = cardSprite(dealerHand[0], dCardPos)
                    cards.add(card)
                    roundEnd = 0
                    click = 0
                    handsPlayed += 1

            return deck, deadDeck, playerHand, dealerHand, dCardPos, pCardPos, roundEnd, displayFont, click, handsPlayed                     