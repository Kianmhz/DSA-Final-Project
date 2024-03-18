import sys
import math


class queque():

    def __init__(self):
        self.arr = []
        self.size = 0

    def enqueque(self, value):
        self.arr.append(value)
        self.size += 1

    def dequeque(self):
        self.size -= 1
        return self.arr.pop(0)

    def isEmpty(self):
        return self.size == 0

    def first(self):
        return self.arr[0]

    def get_size(self):
        return self.size

    def __str__(self):
        return str(self.arr)


cardValues = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def war():
    warCardsP1 = queque()
    warCardsP2 = queque()

    winsP1 = 0
    winsP2 = 0

    cardsP1 = queque()
    for i in range(3):
        if deckP1.isEmpty():
            return [-1, warCardsP1, warCardsP2]
        else:
            card = deckP1.dequeque()
            cardsP1.enqueque(card)
            warCardsP1.enqueque(card)

    cardsP2 = queque()
    for i in range(3):
        if deckP2.isEmpty():
            return [-1, warCardsP1, warCardsP2]
        else:
            card = deckP2.dequeque()
            cardsP2.enqueque(card)
            warCardsP2.enqueque(card)

    for i in range(3):
        cardP1 = cardsP1.first()
        cardP2 = cardsP2.first()

        if cardP1 > cardP2:
            winsP1 += 1
            cardsP1.dequeque()
            cardsP2.dequeque()

        elif cardP1 < cardP2:
            winsP2 += 1
            cardsP1.dequeque()
            cardsP2.dequeque()

        else:
            warResult = war()

            if warResult[0] == -1:
                return [-1, warCardsP1, warCardsP2]
            elif warResult[0] == 1:
                winsP1 += 1
            else:
                winsP2 += 1

            for i in range(warResult[1].get_size()):
                warCardsP1.enqueque(warResult[1].dequeque())

            for i in range(warResult[2].get_size()):
                warCardsP2.enqueque(warResult[2].dequeque())

    if winsP1 > winsP2:
        return [1, warCardsP1, warCardsP2]
    else:
        return [2, warCardsP1, warCardsP2]


def getGameResult(deckP1, deckP2):
    round = 0
    while True:
        if deckP1.isEmpty() and deckP2.isEmpty(): return ['PAT']
        if deckP1.isEmpty(): return [2, round]
        if deckP2.isEmpty(): return [1, round]

        round += 1
        cardP1 = deckP1.first()
        cardP2 = deckP2.first()

        print(round)
        print(deckP1)
        print(deckP2)

        if cardP1 > cardP2:
            deckP1.enqueque(deckP1.dequeque())
            deckP1.enqueque(deckP2.dequeque())
        elif cardP1 < cardP2:
            deckP2.enqueque(deckP1.dequeque())
            deckP2.enqueque(deckP2.dequeque())
        else:
            warCards = queque()
            cardP1 = deckP1.dequeque()
            cardP2 = deckP2.dequeque()

            warResult = war()

            warCards.enqueque(cardP1)
            for i in range(warResult[1].get_size()):
                warCards.enqueque(warResult[1].dequeque())
            
            warCards.enqueque(cardP2)
            for i in range(warResult[2].get_size()):
                warCards.enqueque(warResult[2].dequeque())

            if warResult[0] == -1:
                return ['PAT']
            else:
                for i in range(warCards.get_size()):
                    if warResult[0] == 1:
                        deckP1.enqueque(warCards.dequeque())
                    else:
                        deckP2.enqueque(warCards.dequeque())


deckP1 = queque()
deckP2 = queque()

n = int(input())
for i in range(n):
    cardp_1 = input() 
    deckP1.enqueque(cardValues.index(cardp_1[:len(cardp_1)-1]))
m = int(input()) 
for i in range(m):
    cardp_2 = input()
    deckP2.enqueque(cardValues.index(cardp_2[:len(cardp_2)-1]))

result = getGameResult(deckP1, deckP2)

if result[0] == 'PAT':
    print("PAT")
else:
    print(str(result[0]) + ' ' + str(result[1]))