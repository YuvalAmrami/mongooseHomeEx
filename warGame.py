import random

def deal2DeacksOf10(usedCards):
    deckA = dealCards(10,usedCards)
    deckB = dealCards(10,usedCards)
    return deckA, deckB, usedCards
    
def dealCards(numOfCards2Deal,usedCardsInDeck):
    DeltCards=[]
    i = 0
    while (i <numOfCards2Deal):
        cardNum = random.randint(2,14) # an ase is represented by 14
        cardColor = random.randint(1,4) # Heart, Diamonds, Clubs, Spades
        card = {cardNum,cardColor}
        if not(card in usedCardsInDeck):
            DeltCards.append(card)
            usedCardsInDeck.append(card)
            i=i+1
    return DeltCards

def winChancePercentage(card,sortedKnownCards):
    numberOfPlayableCards = 52 -len(sortedKnownCards)
    cardNum = card[0]
    numOfCrdsLosingToCrd = (cardNum-2)*4 # the num of cards in a normal deck that has a lower value 
                        # ex: 2 will never win, ace with the value of 14 will win against all cards that are not aces: 14-2 = 12 values of cards(2 to 13) *4 colors 
    LosingCardsUsed = findNumberOfUsedLosingCards(card,sortedKnownCards)

    return ((numOfCrdsLosingToCrd-LosingCardsUsed)/numberOfPlayableCards)*100


def findNumberOfUsedLosingCards(card, sortedKnownCards): # all the cards that are losing to the next card in the deck and were already known
    indexOfCard = sortedKnownCards.index(card) # must be in because init part
    while ((indexOfCard>0) and sortedKnownCards[indexOfCard-1][0]==card[0]): # in case there were other cards with the same value and other colors
        indexOfCard = indexOfCard-1
    return indexOfCard # because it is sorted all smaller that crd will be to the left of it

usedCards =[]
deckA, deckB, usedCards = deal2DeacksOf10(usedCards)
playerAPoints = 0 
playerBPoints = 0 
knownCards = deckA.sort()
print("deckA ", deckA)
print("deckB ", deckB)
print("usedCardsInDeck ", usedCards)
print("knownCards ", knownCards)

for i in range(len(deckA)):
    card = deckA.pop()
    print("card: ", card)
    print("win percentage for current card: ", winChancePercentage(card,knownCards))
    BCard = deckB.pop()
    print("B card: ", BCard)
    if (card[0]>BCard[0]):
        playerAPoints = playerAPoints +1
        print("player A win this round")
    elif (card[0]<BCard[0]):
        playerBPoints = playerBPoints +1
        print("player B win this round")
if (playerAPoints>playerBPoints):
    print("player A win this round")
elif (playerAPoints<playerBPoints):
    print("player B win this round")
else:    
    print("it's a tie")
