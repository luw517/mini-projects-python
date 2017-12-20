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
outcome = ""
score = 0
dealer = []
player = []
deck = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
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
        
        self.cards=[]
        pass	# create Hand object

    def __str__(self):
        result=""
        for card in self.cards:
            result+=card.__str__()
        return result
        pass	# return a string representation of a hand

    def add_card(self, card):
        self.card=card
        self.cards.append(card)
        pass	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
            # compute the value of the hand, see Blackjack video
        value = 0
        
        for card in self.cards:
            rank=card.get_rank()
            value += VALUES[rank]

            if rank == 'A':
                if value<=11:
                    value+=10
                
      
        return value

      
    def draw(self, canvas, pos):
        i=0
        for card in self.cards:
            card.draw(canvas, pos)
            pos[0] += 100
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck=[]
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit,rank))
        pass	# create a Deck object

    def shuffle(self):
        random.shuffle(self.deck)
        
        # shuffle the deck 
        
        pass    # use random.shuffle()

    def deal_card(self):
        
        return self.deck.pop()
       
        pass	# deal a card object from the deck
    
    def __str__(self):
        return self.suit + self.rank
        pass	# return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, score, in_play, deck, player, dealer
    deck=Deck()
    deck.shuffle()
    player=Hand()
    dealer=Hand()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    outcome=""
    
    in_play = True

def hit():
    global outcome, score, in_play, Hand, player
    
    if in_play:
        player.add_card(deck.deal_card())
        
    if player.get_value()<=21:
        outcome="Hit or stand?"
    else:
        
        outcome="You have busted"
    
    
   
    
    # replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, score, in_play, Hand, player, dealer
    if player.get_value()>21:
        outcome="You have busted"
        score-=1
    else:
        while dealer.get_value()<17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
                score += 1
                outcome = "You won! New deal?"
        elif dealer.get_value() >= player.get_value():
                
                score -= 1
                outcome = "You lose. New deal?"
        else:
                score += 1
                outcome = "You won! New deal?"
    in_play=False
   
    
    pass	# replace with your code below
    
                    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global in_play
    
    canvas.draw_text("Dealer", (10, 150), 26, "black")
    canvas.draw_text("Player", (10, 260), 26, "black")
    canvas.draw_text("Blackjack",[100,50],28,"black")
    canvas.draw_text(outcome, [10,100],28,"yellow")
    player.draw(canvas, [100,250])
    dealer.draw(canvas, [100,150])
    canvas.draw_text("Score:"+str(score), (400, 80), 28, "yellow")
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (136,198), CARD_BACK_SIZE)
    

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
