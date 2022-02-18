# implementation of card game - Memory

# you are working on step 5

import simplegui
import random

#global constants
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 100

# global mutables
numslist = []
exposed = []
coords = {}
cards = []
turns = 0
turns_str = ""

# helper function to initialize globals
def new_game():
    """initializes necessary stuff for game"""
    global numslist, exposed, coords, flipped, turns, turns_str
    numslist = [0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7]
    exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    coords = {0:(0,48),1:(51,98),2:(101,148),3:(151,198),4:(201,248),5:(251,298),6:(301,348),7:(351,398),8:(401,448),9:(451,498),10:(501,548),11:(551,598),12:(601,648),13:(651,698),14:(701,748),15:(751,799)}
    """ makes the game random. """
    random.shuffle(numslist)
    turns = 0
    turns_str = "Turn: " + str(turns)
    label.set_text(turns_str)
 
# define event handlers
def mouseclick(pos):
    # the goal is to flip 2 cards over, compare them and
    # if they match they stay, if not they flip back over
    global numslist, exposed, coords, cards, turns, turns_str, label
        
    for key,value in coords.items():
       if pos[0] >= value[0] and pos[0] <= value[1]:
          if exposed[key] == False:
             if len(cards) < 2:
                print 'exposekey'
                exposed[key] = True
                cards.append(key)
                print cards
             else: 
                if numslist[cards[0]] == numslist[cards[1]]:
                    print 'Match'
                    cards = []
                    turns += 1
                    print turns
                    turns_str = "Turn: " + str(turns)
                    label.set_text(turns_str)
                else:
                    print 'Not a match'
                    for i in cards:
                       exposed[i] = False
                    cards = []
                    turns += 1
                    print turns
                    turns_str = "Turn: " + str(turns)
                    label.set_text(turns_str)
  
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global numslist, exposed
    width = 19
    for i in range(0,800,50):
        canvas.draw_line((i, 0), (i, 100), 2, 'Red')
 
    for j in range(len(numslist)): 
        if exposed[j]:
            canvas.draw_text(str(numslist[j]), (width, 56), 20, 'White', 'monospace')
        else: 
            pass
        width+=50
        
# create frame and add a button and labels

frame = simplegui.create_frame("Memory", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label(turns_str)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
