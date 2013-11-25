import math
import simplegui
import random

num_range = 100
attempts = 7
random_choice = 0

def get_random_number(range):
    return random.randint(0, range - 1)

def new_game():
    global num_range, attempts, random_choice
    
    random_choice = get_random_number(num_range)
    
    if num_range == 100:
        attempts = 7
    else:
        attempts = 10
        
    print "New game started. The range is from 0 to " + str(num_range)
    print "You have " + str(attempts) + " attempts"
    
def range100():
    global num_range
    num_range = 100
    print "\n"
    new_game()

def range1000():
    global num_range
    num_range = 1000
    print "\n"
    new_game()
    
def input_guess(guess):
    global attempts
    int_guess = int(guess)
    print "\nYour guess is " + guess
    
    if int_guess > random_choice:
        print "Lower!"
    elif int_guess < random_choice:
        print "Higher!"
    else:
        print "You are awesome! Number found!\n"
        return new_game()
    
    attempts = attempts - 1
    if attempts < 1:
        print "You've failed. Start again.\n"
        return new_game()
    else:
        print "You have " + str(attempts) + " attempts left."

f = simplegui.create_frame("Guess the number", 200, 200)
f.add_button("Range [0, 10)", range100, 200)
f.add_button("Range [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

new_game()
