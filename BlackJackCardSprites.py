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