# define global variables
import simplegui

interval=100
position=[50,50]
total=0
score=0
time=0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
        A=int(t/600)
        B=int((t%600)/100)
        C=int(((t%600)%100)/10)
        D=int(((t%600)%100)%10)
        return str(A)+":"+str(B)+str(C)+"."+str(D)
    
            
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    
    
    timer.start()
    
def stop():
    timer.stop()
    
    global total
    global score
    
    total=total+1
    if int(((time%600)%100)%10)==0:
        score=score+1     
        
    timer.stop()
def reset():
    global time, score, total
    timer.stop()
    time=0
    score=0
    total=0

# define event handler for timer with 0.1 sec interval
def timer():
    global time
    time=time+1
    
   
# define draw handler
def draw(canvas):
    text=format(time)
    canvas.draw_text(text, position, 24, "blue")
    canvas.draw_text(str(score)+"/"+str(total), (170,20),20,"yellow")
    
# create frame
frame = simplegui.create_frame("Stopwatch game", 250, 250)
frame.set_canvas_background('black')


# register event handlers

timer=simplegui.create_timer(interval,timer)
frame.set_draw_handler(draw)
frame.add_button("start",start,200)
frame.add_button("stop",stop,200)
frame.add_button("reset", reset,200)


# start frame.
frame.start()
