# template for "Stopwatch: The Game"
import simplegui
# define global variables
integer = 0
interval =100
is_running= False
success = 0
stops = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(integer): 
        min = integer//600        
        wsec = int(integer)//10
        a = wsec%60
        ttens = a//10    
        otens = a%10
        tenths = int(integer)%10    
        counter= str(min) +":" +str(ttens)+ str(otens)+"." +str(tenths)
        return counter  
# define event handlers for buttons; "Start", "Stop", "Reset"
def reset():
    timer.stop()
    global integer, success, stops
    success = 0
    stops = 0
    integer = 0
    
def stop():
    global is_running, stops, success
    
    if is_running == True :
        timer.stop()
        stops = stops+ 1
        is_running= False 
        if integer%10==0:
            success= success+1
      
    
def start():
    global is_running
    is_running = True
    timer.start()

# define event handler for timer with 0.1 sec interval
def tick():
    global integer
    integer= integer +1
    

# define draw handler
def draw(canvas):     
    canvas.draw_text((format(integer)),[100,100], 36, "white")
    canvas.draw_text((str(success)+" / " +str(stops)),[230,40], 34, "red")
    
    

# create frame
frame = simplegui.create_frame("My stopwatch", 300, 200)
timer = simplegui.create_timer(interval,tick)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)

# start frame
frame.start()


