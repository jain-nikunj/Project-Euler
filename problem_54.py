from ex import *

all_cards = {"A":14, "2":2, '3':3, '4':4,'5':5,'6':6, '7':7, '8':8, '9':9,'T':10, "K":13, "Q":12, "J":11}

class Card:
    
    def __repr__(self):
        return self.number+self.suit

    def __init__(self, value):
        self.suit = value[1]
        self.number = value[0]

def has_straight(hand):
    cards = sorted(hand.cards, key=lambda card: all_cards[card.number])
    if cards[-1].number == 'A':
        a = has_straight(Hand(cards[:len(cards)-1]))
        if a and a[1][0].number=='2' : return True, tuple([cards[-1]] + cards[:len(cards)-1])
        elif a and a[1][-1].number == 'K': return True, tuple(cards)
        return False
    for i in range(len(cards) - 1):
        if not all_cards[cards[i+1].number] - all_cards[cards[i].number] == 1: return False
    return True, tuple(cards)

def has_flush(hand):
    for i in range(len(hand.cards)-1):
        if not hand.cards[i].suit == hand.cards[i+1].suit: return False
    return True, hand.cards[0].suit

def has_straight_flush(hand):
    a,b = has_flush(hand), has_straight(hand)
    if a and b:
        return True, a[1], b[1]
    return False

def has_three_of_a_kind(hand):
    for i in range(len(hand.cards)):
        for j in range(i+1, len(hand.cards)):
            for k in range(j+1, len(hand.cards)):
                card1, card2, card3 = [hand.cards[l] for l in (i,j,k)]
                if card1.number == card2.number and card2.number == card3.number:
                    return True, (card1, card2, card3)
    return False

def has_pair(hand):
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

def has_full_house(hand):
    a,b = has_pair(hand), has_three_of_a_kind(hand)
    if a and b and not a[1][0].number == b[1][0].number:
        return (a[1], b[1])
    return False

def has_four_of_a_kind(hand):
    a = has_two_pair(hand)
    if a:
        if a[1][1].number == a[0][0].number:
            return a[1] + a[0]
    return False

def has_royal_flush(hand):
    a = has_straight_flush(hand)
    if a and a[-1][-1].number == 'A': return a
    return False

def highest_card(hand):
    return True, (max(hand.cards, key=lambda x:all_cards[x.number]),)

functions = (highest_card, has_pair, has_two_pair, has_three_of_a_kind, has_straight, has_flush, has_full_house, has_four_of_a_kind, has_straight_flush, has_royal_flush)

class Hand:
    
    def __repr__(self):
        string = ""
        for card in self.cards:
            string += (str(card)) + " "
        return string

    def __init__(self, cards):
        self.cards = cards[:]

    def value(self):
        value = []
        for i in range(len(functions)-1, -1,-1):
            a = functions[i](self)
            if a: 
                value.append(i)
                break
        value.append(a)
        return value
        

def main(filename = "problem_54_data"):
    f = open(filename)
    lines = list(f)
    games = [[Hand(cards[:5]), Hand(cards[5:10])] for cards in [[Card(word[:2]) for word in line.split(" ")] for line in lines]]
    games_copy = games[:]
    count1, ecount = (0,0)
    for game in games_copy:
        hand1, hand2 = game
        value1, value2 = hand1.value(), hand2.value()
        if value1[0] > value2[0]: count1 +=1 
        elif value1[0] == value2[0]: 
            win1, win2 = value1[1][1][0], value2[1][1][0]
            if win1.number == win2.number:
                print(hand1, hand2)
                ecount +=1
            elif win1.number > win2.number:
                count1+=1

    print(count1, ecount)
