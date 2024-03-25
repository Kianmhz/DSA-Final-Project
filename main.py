import sys
import math
class queue():
    def __init__(self):
        self.arr = []
        self.size = 0

    def enqueue(self, value):
        self.arr.append(value)
        self.size += 1

    def dequeue(self):
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

def war(warCardsP1, warCardsP2):
    for i in range(3):
        if deckP1.isEmpty() or deckP2.isEmpty():
            return -1
        else:
            warCardsP1.enqueue(deckP1.dequeue())
            warCardsP2.enqueue(deckP2.dequeue())

    battleCardP1 = deckP1.dequeue()
    battleCardP2 = deckP2.dequeue()

    warCardsP1.enqueue(battleCardP1)
    warCardsP2.enqueue(battleCardP2)

    if battleCardP1 == battleCardP2:
        return war(warCardsP1, warCardsP2)
    else:
        winnningDeck = deckP1 if battleCardP1 > battleCardP2 else deckP2

        for i in range(warCardsP1.get_size()):
            winnningDeck.enqueue(warCardsP1.dequeue())
        for i in range(warCardsP2.get_size()):
            winnningDeck.enqueue(warCardsP2.dequeue())
        
        return 1

def getGameResult(deckP1, deckP2):
    rounds = 0
    while True:
        if deckP1.isEmpty() and deckP2.isEmpty():
            return ["PAT"]
        if deckP1.isEmpty():
            return [2, rounds]
        if deckP2.isEmpty():
            return [1, rounds]

        rounds += 1
        battleCardP1 = deckP1.dequeue()
        battleCardP2 = deckP2.dequeue()

        if battleCardP1 == battleCardP2:
            warCardsP1 = queue()
            warCardsP1.enqueue(battleCardP1)

            warCardsP2 = queue()
            warCardsP2.enqueue(battleCardP2)

            result = war(warCardsP1, warCardsP2)

            if result == -1:
                return ["PAT"]
        else:
            winnningDeck = deckP1 if battleCardP1 > battleCardP2 else deckP2
            winnningDeck.enqueue(battleCardP1)
            winnningDeck.enqueue(battleCardP2)


deckP1 = queue()
deckP2 = queue()

n = int(input())
for i in range(n):
    cardp_1 = input()
    deckP1.enqueue(cardValues.index(cardp_1[:-1]))
m = int(input())
for i in range(m):
    cardp_2 = input()
    deckP2.enqueue(cardValues.index(cardp_2[:-1]))

result = getGameResult(deckP1, deckP2)

if result[0] == 'PAT':
    print("PAT")
else:
    print(str(result[0]) + ' ' + str(result[1]))
