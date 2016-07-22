# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui

number=0
count = 0

# helper function to start and restart the game
def new_game():
    global number
    number = 0
    global count 
    count =0
    print "select your choice of range"
    
    # initialize global variables used in your code here
    
    # remove this when you add your code    
    


# define event handlers for control panel
def range100():
    global number
    global count
    count =7
    number =  random.randrange(0,100)
   
  
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global number
    number = random.randrange(0,1000)
    global count 
    count = 10
    
    
    
def input_guess(guess):
    global number
    global count
    count =  int(count)
    guess = int(guess)
    number = int(number)
    if number > guess:
        print "Higher"
        count = count-1
        if count== 0:
            print "guesses finished"
            new_game()
            
        print "Number of guesses left are " +str(count)
    elif number < guess:
        print "Lower"
        count = count -1
        print "Number of guesses left are " +str(count)
        if count== 0:
            print "guesses finished"
            new_game()    
    else:
        print "correct"
        new_game()
    # main game logic goes here	
    
    # remove this when you add your code
  

    
# create frame
frame = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
frame.add_button("Range 0-100", range100, 200)

frame.add_button("Range 0-1000", range1000, 200)
frame.add_input("What is your guess?", input_guess,100)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
