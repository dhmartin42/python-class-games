# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ''
dealer_score = 0
player_score = 0
play_deck = None
player_hand = None
dealer_hand = None
player_busted = False
dealer_busted = False
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
# Card class verified functional using test case
# http://www.codeskulptor.org/#examples-card_template.py
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        s = "Hand Contains: " 
        for i in self.hand:
            s+= " " + str(self.hand[self.hand.index(i)]) # return a string representation of a hand
        return str(s)
    
    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        value = 0
        aces = 0
        for i in self.hand:
            if i.rank in VALUES.keys():
                value += VALUES.get(i.rank)
            if i.rank == 'A':
                aces += 1
        if aces == 1:
            if (value+10) < 22:
                value +=10
        if aces == 2: 
            if (value + 10) < 22:
                value+=10
        if aces == 3: 
            if (value + 10) < 22:
                value+=10
        return value
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        # draws the hand on the canvas using the draw mathod of the card
        j = 0
        for i in self.hand:
            i.draw(canvas, [(pos[0]+83*j),pos[1]])
            j+=1
     
  
        
# define deck class 
class Deck:
    def __init__(self):
        self.deckofcards = []
        for i in SUITS:
            for j in RANKS:
                self.deckofcards.append(Card(i,j))
        # create a Deck object

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deckofcards)    # use random.shuffle()

    def deal_card(self):
        return self.deckofcards.pop() #eal a card object from the deck
    
    def __str__(self):
        s = "Deck contains: "
        for i in self.deckofcards:
            s+= str(i) + " "
        return s# return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, play_deck, dealer_busted, player_busted, dealer_score
    
    #if you click deal while in play, you lose
    print "In play: " + str(in_play)
    if in_play: 
        dealer_score += 1
        in_play = False
        
    # card sharks, start your engines
    in_play = True
    outcome = ''
    dealer_busted = False
    player_busted = False
    
    #initializing all the values
    play_deck = Deck()
    play_deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    
    # adding the cards
    player_hand.add_card(play_deck.deal_card())
    player_hand.add_card(play_deck.deal_card())
    dealer_hand.add_card(play_deck.deal_card())
    dealer_hand.add_card(play_deck.deal_card())
    print "Player's hand: " + str(player_hand)
    print "Hand Value: " + str(player_hand.get_value())
    print "Dealer's Hand: " + str(dealer_hand)
    print "Hand Value: " + str(dealer_hand.get_value())
    

def hit():
    global player_hand, in_play, outcome, play_deck, dealer_score, player_busted
    
 
    # if the hand is in play, hit the player
    if in_play:
        player_hand.add_card(play_deck.deal_card())
        print player_hand.get_value()                     
        if (player_hand.get_value() > 21):
            outcome = False
            in_play = False
            dealer_score +=1
            outcome = 'dealer'
            player_busted = True
            print 'BUSTED! Dealer Wins!'
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global play_deck, player_hand, dealer_hand, in_play, outcome, dealer_score, player_score, dealer_busted
    
    print "Dealer hand Value: "+str(dealer_hand.get_value())
    print dealer_hand.get_value <= 17
    if in_play: 
        while (dealer_hand.get_value() <= 17):
            
            print "Dealer hand Value: " + str(dealer_hand.get_value())
            dealer_hand.add_card(play_deck.deal_card())
            print str(dealer_hand)
            
        if dealer_hand.get_value() > 21:
            print "Dealer busted!"
            outcome = 'player'
            dealer_busted = True
            in_play = False
        else:
            if dealer_hand.get_value() >= player_hand.get_value():
               print "Dealer wins!"
               dealer_score += 1
               print "Score: Dealer: " + str(dealer_score) + " Player: " + str(player_score) 
               in_play = False
               outcome = 'dealer'
            else:
               print "Player wins!"
               player_score += 1
               print "Score: Dealer: " + str(dealer_score) + " Player: " + str(player_score) 
               in_play = False
               outcome = 'player'
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global card_back, CARD_SIZE, CARD_CENTER, dealer_score, player_score, player_busted, dealer_busted, player_hand, dealer_hand
    # test to make sure that card.draw works, replace with your code below
    
    dealer_hand.draw(canvas, [134,150])          
    player_hand.draw(canvas, [134,300])
    
    if in_play:
        canvas.draw_image(card_back, (36, 48), (72,96), (253,198), (72,96))
        canvas.draw_text('Hit or Stand?', (134,450), 36, 'White')
    else: 
        dealer_hand.draw(canvas, [134,150])
        
        if player_busted:
            canvas.draw_text('You busted. Deal new hand?', (134,550), 36, 'White')
        elif dealer_busted:
            canvas.draw_text('Dealer busted. Deal new hand?', (134,550), 36, 'White')
        else: 
            canvas.draw_text('Deal new hand?', (134,550), 36, 'White')
   
    if (outcome == 'dealer'):
        canvas.draw_text('Dealer Wins', (134, 500), 36, 'White')
    if (outcome == 'player'):
        canvas.draw_text('Player Wins', (134, 500), 36, 'White')
    
    tot = "Dealer: " + str(dealer_score) + " Player: " + str(player_score)
    canvas.draw_text('BlackJack', (20, 30), 36, 'White')
    canvas.draw_text(tot, (450, 30), 18, 'White')

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
