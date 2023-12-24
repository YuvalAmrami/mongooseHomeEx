import random

def deal2DeacksOf10(usedCards):
    deckA = dealCards(10,usedCards)
    deckB = dealCards(10,usedCards)
    return deckA, deckB, usedCards
    
def dealCards(numOfCards2Deal,usedCardsInDeck):
    DeltCards=[]
    i = 0
    while (i <numOfCards2Deal):
        cardNum = random.randint(2,14) # an ace is represented by 14
        cardColor = random.randint(1,4) # Heart, Diamonds, Clubs, Spades
        card = [cardNum,cardColor]
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
    return indexOfCard # because it is sorted all smaller cards will be to the left of it and the number of them will be this index


# full game:
usedCards =[]
deckA, deckB, usedCards = deal2DeacksOf10(usedCards)
playerAPoints = 0 
playerBPoints = 0 
knownCards = list(deckA)
knownCards.sort()
print("deckA ", deckA)
# print("deckB ", deckB)
# print("usedCardsInDeck ", usedCards)

for i in range(len(deckA)):
    card = deckA.pop()
    print("card: ", card)
    print("win chances for current card: ", round(winChancePercentage(card,knownCards),2),"%")
    BCard = deckB.pop()
    print("B card: ", BCard)
    knownCards.append(BCard)
    knownCards.sort()
    # print("knownCards ", knownCards)
    if (card[0]>BCard[0]):
        playerAPoints = playerAPoints +1
        print("player A win this round")
    elif (card[0]<BCard[0]):
        playerBPoints = playerBPoints +1
        print("player B win this round")
if (playerAPoints>playerBPoints):
    print("player A win the game")
elif (playerAPoints<playerBPoints):
    print("player B win the game")
else:    
    print("it's a tie")



########################################################################################  tests  ####################################################################

# def test1():
#     knownCards =[[14,1]]
#     return (round(winChancePercentage([14,1],knownCards),2)==94.12)

# def test2():
#     knownCards =[[2,1]]
#     return (round(winChancePercentage([2,1],knownCards),2)==0)

# def test3():
#     knownCards =[[14,3]]
#     return (round(winChancePercentage([14,3],knownCards),2)==94.12)

# def test4():
#     knownCards =[[14,2],[14,3]]
#     return (round(winChancePercentage([14,2],knownCards),2)==96)

# def test5():
#     knownCards =[[14,1],[14,2],[14,3],[14,4]]
#     return (round(winChancePercentage([14,2],knownCards),2)==100)

# def test6():
#     knownCards =[[14,1],[14,2],[14,3]]
#     return (round(winChancePercentage([14,2],knownCards),2)==97.96)

# def test7():
#     knownCards =[[13,2],[14,3]] # unknown Card:50 out of them 47 will lose to ace of Clubs
#     return (round(winChancePercentage([14,3],knownCards),2)==94)


# print(test1())
# print(test2())
# print(test3())
# print(test4())
# print(test5())
# print(test6())
# print(test7())