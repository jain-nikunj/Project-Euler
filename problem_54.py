from ex import *

all_cards = {"A":1, "2":2, '3':3, '4':4,'5':5,'6':6, '7':7, '8':8, '9':9,'T':10, "K":13, "Q":12, "J":10}

class Card:

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

def has_pair(hand):
    """Takes in a hand and evaluates whether that hand has a pair. If it does, it returns the pair of cards as well."""

    for i in range(len(hand.cards)):
        for j in range(i+1, len(hand.cards)):
            if hand.cards[i].number == hand.cards[j].number: return True, (hand.cards[i], hand.cards[j])
    return False

def has_two_pair(hand):
    a = has_pair(hand)
    if a:
        card1, card2 = a[1]
        b = has_pair(Hand([card for card in hand.cards if not card==card1 and not card==card2]))
        if b:
            return (a[1], b[1])
        return b
    return False


class Hand:

    def __init__(self, cards):
        self.cards = cards[:]

    def highest_card(self):
        return max([card.number for card in self.cards], key=lambda x:all_cards[x])

    
