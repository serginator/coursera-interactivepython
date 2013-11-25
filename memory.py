# implementation of card game - Memory

import simplegui
import random
import math

CARD_HEIGHT = 100
CARD_WIDTH = 50
NUM_OF_CARDS = 16 # Always an even number!!!!!

# "Prints" for debugging purpouse
print "############ Debug console ############"

# helper function to initialize globals
def new_game():
    global cards, exposed, state, turns
    print "New game"
    turns = 0
    state = 0
    cards = range(NUM_OF_CARDS / 2) + range(NUM_OF_CARDS / 2)
    random.shuffle(cards)
    print "List of cards:"
    print cards
    exposed = []
    for i in range(NUM_OF_CARDS):
        exposed.append(False)


# define event handlers
def mouseclick(pos):
    global exposed, state, cardA, cardB, valA, valB, turns
    card = int(math.floor(pos[0] / 50))
    value = cards[card]
    print "Click on card=" + str(card) + ", value=" + str(value) 
    if state == 0:
        if not exposed[card]:
            exposed[card] = True
            state = 1
            cardA = card
            valA = value
    elif state == 1:
        if not exposed[card]:
            exposed[card] = True
            state = 2
            cardB = card
            valB = value
            turns += 1
    elif state == 2:
        if not exposed[card]:
            exposed[card] = True
            state = 1
            if valA <> valB:
                exposed[cardA] = False
                exposed[cardB] = False
            cardA = card
            valA = value
        

# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(NUM_OF_CARDS):
            if exposed[i]:
                canvas.draw_polygon([(CARD_WIDTH * i, 0),
                                     (CARD_WIDTH * (i + 1), 0),
                                     (CARD_WIDTH * (i + 1), CARD_HEIGHT),
                                     (CARD_WIDTH * i, CARD_HEIGHT)],
                                    1,
                                    'Green',
                                    'White')
                canvas.draw_text(str(cards[i]), (CARD_WIDTH * i + 10, 70), 50, "Red")
            else:
                canvas.draw_polygon([(CARD_WIDTH * i, 0),
                                     (CARD_WIDTH * (i + 1), 0),
                                     (CARD_WIDTH * (i + 1), CARD_HEIGHT),
                                     (CARD_WIDTH * i, CARD_HEIGHT)],
                                    1,
                                    'White',
                                    'Green')
    label.set_text("Turns = " + str(turns))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", CARD_WIDTH * NUM_OF_CARDS, CARD_HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
