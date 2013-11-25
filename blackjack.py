# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

in_play = False
outcome = ""
score = 0

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

soundWin0 = simplegui.load_sound('https://dl.dropbox.com/s/8xk74sqp84gjdoe/FlawessVictory%21.mp3')
soundWin1 = simplegui.load_sound('https://dl.dropbox.com/s/zfhr56kgy3iofhp/WellDone.mp3')
soundLose0 = simplegui.load_sound('https://dl.dropbox.com/s/lmb0kodttey421o/Jajajaja%2CyouSuck%21%21%21.mp3')
soundLose1 = simplegui.load_sound('https://dl.dropbox.com/s/av48jorq4d2b8kq/OhNoo%21%21%21.mp3')

SOUND_WIN = {0: soundWin0,
             1: soundWin1}

SOUND_LOSE = {0: soundLose0,
              1: soundLose1}

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
        
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        text = "HAND: "
        for card in self.cards:
            text += str(card) + " "
        return text

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        ace = False
        for card in self.cards:
            rank = card.get_rank()
            value += VALUES[rank]
            if not ace and rank == 'A':
                ace = True
        if ace and (value + 10) <= 21:
            return value + 10
        else:
            return value
   
    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas,
                      [pos[0] + 80 * self.cards.index(card),
                       pos[1]])

class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        text = "DECK: "
        for card in self.cards:
            text += str(card) + " "
        return text

def deal():
    global in_play, deck, player, dealer, score, outcome
    
    if in_play:
        outcome = "You lose."
        SOUND_LOSE[random.randint(0,1)].play()
        score -= 1

    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    
    in_play = True

def hit():
    global in_play, outcome, score
    if in_play:
        player.add_card(deck.deal_card())
        if player.get_value() <= 21:
            outcome = "Hit or stand?"
        else:
            outcome = "You have busted. New deal?"
            SOUND_LOSE[random.randint(0,1)].play()
            score -= 1
            in_play = False

def stand():
    global in_play, outcome, score
    if in_play:
        in_play = False
        if player.get_value() > 21:
            outcome = "You have busted. New deal?"
            SOUND_LOSE[random.randint(0,1)].play()
            score -= 1
        else:
            while dealer.get_value() < 17:
                dealer.add_card(deck.deal_card())
            if dealer.get_value() > 21:
                outcome = "You win. New deal?"
                SOUND_WIN[random.randint(0,1)].play()
                score += 1
            elif dealer.get_value() > player.get_value():
                outcome = "You have busted. New deal?"
                SOUND_LOSE[random.randint(0,1)].play()
                score -= 1
            else:
                outcome = "You win. New deal?"
                SOUND_WIN[random.randint(0,1)].play()
                score += 1

def draw(canvas):
    canvas.draw_text("Blackjack", [30, 570], 50, "White")
    canvas.draw_text("Score: " + str(score), [450, 50], 30, "White")
    canvas.draw_text(outcome, [50, 50], 30, "White")
    
    dealer.draw(canvas, [50, 150])
    player.draw(canvas, [50, 250])
    
    if in_play:
        canvas.draw_image(card_back,
                          CARD_BACK_CENTER,
                          CARD_BACK_SIZE,
                          [86, 200],
                          CARD_SIZE)

frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

deal()
frame.start()
