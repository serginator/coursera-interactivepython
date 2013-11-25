# Stopwatch: The Game

import simplegui

#Global vars
time = 0
text = ''
total_games = 0
won_games = 0
STOPPED = True

# Method that returns a string A:BC.D. A,C,D are 0-9 digits
# B is 0-5 digit.
def format(t):
    global text
    
    D = str(t % 10)
    
    A = str(int(t/600))
    if int(A) < 10:
        A = '0' + A
    
    BC = str(int((t/10)%60))
    if int(BC) < 10:
        BC = '0' + BC
    
    text = A + ':' + BC + '.' + D
    return text

def start():
    global STOPPED
    if STOPPED:
        timer.start()
        STOPPED = False

def stop():
    global total_games, won_games, STOPPED
    if not STOPPED:
        STOPPED = True
        timer.stop()
        total_games = total_games + 1
        if (time % 10) == 0:
            won_games = won_games + 1

def reset():
    global time, total_games, won_games, STOPPED
    STOPPED = True
    timer.stop()
    time = 0
    total_games = 0
    won_games = 0

def timer():
    global time
    time = time + 1
    
def draw(canvas):
    canvas.draw_text(format(time), [60, 115], 25, "white")
    canvas.draw_text(str(won_games) +
                     '/' + str(total_games), [150, 30],
                     25, "blue")
    
frame = simplegui.create_frame("Stopwatch", 200, 200)
frame.add_button("Start", start, 50)
frame.add_button("Stop", stop, 50)
frame.add_button("Reset", reset, 50)

frame.set_draw_handler(draw)

timer = simplegui.create_timer(100, timer)

frame.start()
