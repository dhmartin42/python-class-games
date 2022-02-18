# template for "Stopwatch: The Game"
import simplegui

# define global variables

num_game = 0
num_win = 0

#canvas variables
width = 300
height = 200

# drawcanvas variables
time_counter = 0
time_font_color = "White"
time_font_size = 36
time_coords = [120, height/2]
score = "0 / 0"
score_font_color = "White"
score_font_size = 18
score_coords = [240,20]

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time_counter):
    minutes = time_counter / 600
    seconds = (time_counter /10) % 60
    tenths_seconds = time_counter % 10
    if seconds < 10:
        return str(minutes) + ":0" + str(seconds) + "." + str(tenths_seconds)
    return str(minutes) + ":" + str(seconds) + "." + str(tenths_seconds)
 
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global num_game, num_win, time_counter, score
    if timer.is_running() == True:
       timer.stop()
       
       num_game += 1
    
       score = str(num_win)+ " / " +str(num_game) 
    
       if time_counter % 10 == 0:
          num_win += 1    
       score = str(num_win)+ " / " +str(num_game) 
    else: 
       pass
            
def reset():
    global time_counter, score
    timer.stop()
    time_counter = 0
    score = "0 / 0"
    

# define event handler for timer with 0.1 sec interval
def tick():
    global time_counter
    time_counter += 1
    #print time_counter

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time_counter), time_coords, time_font_size, time_font_color)
    canvas.draw_text(score, score_coords, score_font_size, score_font_color)
    
# create frame
frame = simplegui.create_frame("Stopwatch!", width, height)

# register event handlers
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
#timer.start()

# Please remember to review the grading rubric

