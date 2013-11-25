# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

# Method to convert a number into a name
def number_to_name(number):
    name = ''
    
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print "wrong number entered, will return 'rock'"
        return 0
        
    return name
    
# Method to convert a name into a number
def name_to_number(name):
    number = 0
    
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print "wrong name entered, will return 0"
        return 0
        
    return number

# Method to retrieve a name, generate a random name, and compare both to
# know which one wins
import random
def rpsls(name):
    print ""
    print "Player chooses " + name
    player_guess = name_to_number(name)
    computer_guess = random.randrange(0, 4)
    print "Computer chooses " + number_to_name(computer_guess)
    result = (player_guess - computer_guess) % 5
    if (result == 1) or (result == 2):
        print "Player wins!"
    elif (result == 3) or (result == 4):
        print "Computer wins!"
    else:
        print "Player and computer tie!"
        

# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
