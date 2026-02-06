# curve as 10 (relative)
import turtle as tt 
tt.bgcolor('black')
tt.pensize(2)
tt.speed(10)

#iterate six times in total 
for i in range(6):
    
    #choose your color combination
    for color in ('red', 'magenta', 'blue', 'cyan', 'green', 'white', 'yellow'):
        tt.color(color)
        
        #Draw a cicle of chosen zine, 100 here
        tt.circle(100)
         
         # move 10 pixels left to draw another circle 
        tt.left(10)
tt.hideturtle