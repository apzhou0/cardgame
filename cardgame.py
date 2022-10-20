import itertools, random, time

class Card: 
    def __init__(self, suit, value, valid): 
        self.suit = suit
        self.value = value
        self.valid = valid

    def __lt__(self, other):
        if self.suit == other.suit:
            return self.value < other.value
        else:
            return self.suit < other.suit

    def print_card(self):
        print('[', self.convert_suit(), self.convert_value(), ']', sep = '', end = ' ')

    def convert_suit(self):
        if self.valid == 0:
            return '--'
        else:
            return self.suit
    
    def convert_value(self):
        if self.valid == 0:
            return ''
        if self.value < 10:
            return self.value
        elif self.value == 10:
            return 'T'
        elif self.value == 11:
            return 'J'
        elif self.value == 12:
            return 'Q'
        else:
            return 'K'
    
    def card_to_string(self):
        return self.convert_suit() + str(self.convert_value())

class Player:
    def __init__(self, id): 
        self.id = id
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def name(self):
        if self.id == 0:
            return 'You'
        else:
            return 'Bot ' + str(self.id)

    def victory(self):
        if len(self.hand) == 0:
            return 1
        else:
            return 0

    def in_hand(self, cardstring):
        for card in self.hand:
            if card.card_to_string() == cardstring:
                return card
        return 0

    def can_play(self, cardstring):
        obj = self.in_hand(cardstring)
        if obj == 0:
            return 0
        for card in display:
                if card.valid == 1 and obj.suit == card.suit and obj.value == card.value + 1:
                    i = display.index(card)
                    j = self.hand.index(obj)
                    display[i+1] = self.hand[j]
                    print()
                    print(self.name(), 'placed down card', end = ' ')
                    obj.print_card()
                    print()
                    self.hand.pop(j)
                    print_display(display)
                    return 1
                elif card.valid == 1 and obj.suit == card.suit and obj.value == card.value - 1:
                    i = display.index(card)
                    j = self.hand.index(obj)
                    display[i-1] = self.hand[j]
                    print()
                    print(self.name(), 'placed down card', end = ' ')
                    obj.print_card()
                    print()
                    self.hand.pop(j)
                    print_display(display)
                    return 1
        return 0

    def play_turn(self, display):
        if (self.victory() == 1):
            return 0
        for obj in self.hand:
            for card in display:
                if card.valid == 1 and obj.suit == card.suit and obj.value == card.value + 1:
                    i = display.index(card)
                    j = self.hand.index(obj)
                    display[i+1] = self.hand[j]
                    print()
                    print(self.name(), 'placed down card', end = ' ')
                    obj.print_card()
                    print()
                    self.hand.pop(j)
                    print_display(display)
                    return 1
                elif card.valid == 1 and obj.suit == card.suit and obj.value == card.value - 1:
                    i = display.index(card)
                    j = self.hand.index(obj)
                    display[i-1] = self.hand[j]
                    print()
                    print(self.name(), 'placed down card', end = ' ')
                    obj.print_card()
                    print()
                    self.hand.pop(j)
                    print_display(display)
                    return 1
        print()
        print(self.name(), 'did not place down a card.')
        return 0
    
def print_list(list):
    for obj in list:
        obj.print_card()
    print()

def print_display(display):
    count = 0
    for obj in display:
        obj.print_card()
        count = count + 1
        if count == 13:
            print()
            count = 0

userplayer = Player(0)
bot1 = Player(1)
bot2 = Player(2)
bot3 = Player(3)

# populating deck with cards
deck = [] 
for i in range(1,7):
    deck.append( Card('c', i, 1) )
    deck.append( Card('d', i, 1) )
    deck.append( Card('h', i, 1) )
    deck.append( Card('s', i, 1) )
for i in range(8,14):
    deck.append( Card('c', i, 1) )
    deck.append( Card('d', i, 1) )
    deck.append( Card('h', i, 1) )
    deck.append( Card('s', i, 1) )
random.shuffle(deck)

# distributing cards to each player
for i in range(12):
    movecard = deck.pop()
    userplayer.add_card(movecard)
    movecard = deck.pop()
    bot1.add_card(movecard)
    movecard = deck.pop()
    bot2.add_card(movecard)
    movecard = deck.pop()
    bot3.add_card(movecard)
userplayer.hand = sorted(userplayer.hand)

# filling display with placeholders
display = []
for i in range(1,7):
    display.append( Card('c', i, 0) )
display.append( Card('c', 7, 1) )
for i in range(8,14):
    display.append( Card('c', i, 0) )
for i in range(1,7):
    display.append( Card('d', i, 0) )
display.append( Card('d', 7, 1) )
for i in range(8,14):
    display.append( Card('d', i, 0) )
for i in range(1,7):
    display.append( Card('h', i, 0) )
display.append( Card('h', 7, 1) )
for i in range(8,14):
    display.append( Card('h', i, 0) )
for i in range(1,7):
    display.append( Card('s', i, 0) )
display.append( Card('s', 7, 1) )
for i in range(8,14):
    display.append( Card('s', i, 0) )

# making intro display
intro = []
for i in range(1,14):
    intro.append( Card('c', i, 1) )
for i in range(1,14):
    intro.append( Card('d', i, 1) )
for i in range(1,14):
    intro.append( Card('h', i, 1) )
for i in range(1,14):
    intro.append( Card('s', i, 1) )

def play_game(): 
    ranking = []
    completed = 4
    while completed < 52:
        if userplayer.victory() == 0:
            time.sleep(1)
            completed += user_turn()
            if userplayer.victory() == 1 and userplayer.name() not in ranking:
                print()
                print('YOU HAVE PLACED ALL YOUR CARDS!')
                ranking.append(userplayer.name())
        if bot1.victory() == 0:
            time.sleep(1)
            completed += bot1.play_turn(display)
            if bot1.victory() == 1 and bot1.name() not in ranking:
                print()
                print(bot1.name(), 'HAS PLACED ALL THEIR CARDS!')
                ranking.append(bot1.name())
        if bot2.victory() == 0:
            time.sleep(1)
            completed += bot2.play_turn(display)
            if bot2.victory() == 1 and bot2.name() not in ranking:
                print()
                print(bot2.name(), 'HAS PLACED ALL THEIR CARDS!')
                ranking.append(bot2.name())
        if bot3.victory() == 0:
            time.sleep(1)
            completed += bot3.play_turn(display)
            if bot3.victory() == 1 and bot3.name() not in ranking:
                print()
                print(bot3.name(), 'HAS PLACED ALL THEIR CARDS!')
                ranking.append(bot3.name())

    print()
    print('All suits have been completed.')
    print('FINAL RANKING:')
    print(ranking[0], 'placed 1st.')
    print(ranking[1], 'placed 2nd.')
    print(ranking[2], 'placed 3rd.')
    print(ranking[3], 'placed 4th.')

def user_turn():
    print()
    print('YOUR HAND:')
    print_list(userplayer.hand)
    valid = 0
    print('Enter card you would like to place (e.g. hJ)')
    val = input('If you are unable or do not want to place a card, enter n : ')
    while valid == 0:
        if val == 'n':
            print()
            print('You did not place down a card.')
            valid = 1
            return 0
        elif userplayer.can_play(val):
            valid = 1
            return 1
        else: 
            val = input('Please double check your input and try again : ')
    return 0

print('----------------- COMPLETE-THE-SUIT CARD GAME -----------------')
print_display(intro)
print()
print('INSTRUCTIONS:')
print('The first player to place down all their cards wins.')
print('Only cards adjacent to already-placed cards can be discarded.')
input('Enter to begin. ')
print()
print_display(display)
play_game()