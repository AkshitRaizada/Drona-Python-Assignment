import turtle
import os


drone = turtle.Turtle()                        #Defining turtle object as drone

screen = turtle.Screen()                       #Defining screen
screen.title("Drone Simulation")
screen.bgpic("sky1.gif")                       #turtle module only accepts .gif format
screen.setup(width=1920, height=1040)          #Nearly full-screen to give closing option to user
screen.tracer(0)                               #Speeds up the algorithm
screen.register_shape("drone1.gif")            #Drone cannot be resized in .gif form

drone.speed(0)                                 #Special case ensuring fastest movement of drone
drone.shape("drone1.gif")
drone.showturtle()
height = screen.window_height()/ 2             #Used to ensure that drone doesn't leave the screen
width = screen.window_width() / 2
size_factor = 1.5                              #To simulate the appearance of faraway drones travelling slower(apparent speed)
drone_speed = 15                               #Default speed

def move_forward():
    size = drone.turtlesize()
    drone.setheading(90)  
    if (drone.ycor() < height):
        drone.forward(drone_speed/size_factor*size[0])  
    screen.update()

def move_backward():
    size = drone.turtlesize()
    drone.setheading(270)  
    if (drone.ycor() > -height):
        drone.forward(drone_speed/size_factor*size[0])  
    screen.update()

def move_left():
    size = drone.turtlesize()
    drone.setheading(180)  
    if (drone.xcor() > -width):
        drone.forward(drone_speed/size_factor*size[0])  
    screen.update()

def move_right():
    size = drone.turtlesize()
    drone.setheading(0) 
    if (drone.xcor() < width):
        drone.forward(drone_speed/size_factor*size[0])  
    screen.update()
    
def move_forward_left():
    size = drone.turtlesize()
    drone.setheading(135) 
    if (drone.ycor() < height and drone.xcor() > -width):
        drone.forward(drone_speed/size_factor*size[0])  
    screen.update()
    
def move_forward_right():
    size = drone.turtlesize()
    drone.setheading(45) 
    if (drone.ycor() < height and drone.xcor() < width):
        drone.forward(drone_speed/size_factor*size[0])  
    screen.update()
    
def move_backward_left():
    size = drone.turtlesize()
    drone.setheading(225) 
    if (drone.ycor() > -height and drone.xcor() > -width):
        drone.forward(drone_speed/size_factor*size[0])  
    screen.update()

def move_backward_right():
    size = drone.turtlesize()
    drone.setheading(315) 
    if (drone.ycor() > -height and drone.xcor() < width):
        drone.forward(drone_speed/size_factor*size[0])  
    screen.update()

def move_up():
    size = drone.turtlesize()
    increase = (num * 1.1 for num in size)
    drone.turtlesize(*increase) 
    screen.update()    

def move_down():
    size = drone.turtlesize()
    increase = (num / 1.1 for num in size)
    drone.turtlesize(*increase)
    screen.update()

print("Moving around:")
print("q    w    e")
print("a    *    d")
print("z    x    c")

print("Up/Down")
print("2 - UP")
print("s - DOWN")
print("\nClick on screen to exit")
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "x")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

screen.onkeypress(move_forward_left, "q")
screen.onkeypress(move_forward_right, "e")
screen.onkeypress(move_backward_left, "z")
screen.onkeypress(move_backward_right, "c")

screen.onkeypress(move_up, "2")
screen.onkeypress(move_down, "s")

screen.listen()
turtle.exitonclick()


