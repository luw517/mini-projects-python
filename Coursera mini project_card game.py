# implementation of card game - Memory

import simplegui
import random


# helper function to initialize globals
def new_game():
    global card, exposecard, expose, state, i
    card=[0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7]
    random.shuffle(card)
    exposecard=[]
    expose=[False for i in range(16)]
    state=0
    i=0
    turns=0
    
     

     
# define event handlers
def mouseclick(pos):
    global turns, i, card, exposecard, expose, state
    
    if state==0:
        expose[pos[0]//50]=True
        exposecard.append(pos[0]//50)
        state=1
        turns=1
            
    elif state==1:
         if not (pos[0]//50 in exposecard):
                expose[pos[0]/50]=True
                exposecard.append(pos[0]//50)
                state=2
                turns+=1
    elif not (pos[0]//50 in exposecard):
            if card[exposecard[-1]]!=card[exposecard[-2]]:
                expose[exposecard[-1]]=False
                expose[exposecard[-2]]=False
                exposecard.pop()
                exposecard.pop()
            exposecard.append(pos[0]/50)
            expose[pos[0]//50]=True
            state=1
            turns+=1
                    
       
    
    # add game state logic here
    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
  
   for i in range(16):
        
        if expose[i]:
            canvas.draw_text(str(card[i]), (i*50+25, 50), 36, "red")
        else:
                canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 3, "red", "green")
    
    
   


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game) 
label=frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric
