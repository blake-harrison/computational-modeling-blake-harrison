import numpy as np
import random as rand
from vpython import *

scene1 = canvas(title="Breakout")


#uses constants and wall objects from the gas collision as a base
m = 1.7e-27
R = 0.5e-10
L = 40 * R
thick = L/100
cols = 6
boxes = []

#creates walls
Lwall = box(pos = vec(-L/2,0,0), size = vec(thick, L, 0), color = color.white)
Rwall = box(pos = vec(L/2,0,0), size = vec(thick, L, 0), color = color.white)
Bwall = box(pos = vec(0,-L/2,0), size = vec(L, thick, 0), color = color.white)
Twall = box(pos = vec(0, L/2, 0), size = vec(L, thick, 0), color=color.white)

#creates boxes
for x in range(0,cols):
    newbox0 = box(pos = vec((-L/2)+(x*(L/6))+L/12,(0+(0*L/10)),0), size = vec(L/6,L/10,0), color = color.cyan)
    newbox1 = box(pos = vec((-L/2)+(x*(L/6))+L/12,(0+(1*L/10)),0), size = vec(L/6,L/10,0), color = color.green)
    newbox2 = box(pos = vec((-L/2)+(x*(L/6))+L/12,(0+(2*L/10)),0), size = vec(L/6,L/10,0), color = color.yellow)
    newbox3 = box(pos = vec((-L/2)+(x*(L/6))+L/12,(0+(3*L/10)),0), size = vec(L/6,L/10,0), color = color.orange)
    newbox4 = box(pos = vec((-L/2)+(x*(L/6))+L/12,(0+(4*L/10)),0), size = vec(L/6,L/10,0), color = color.red)
    boxes.append(newbox0)
    boxes.append(newbox1)
    boxes.append(newbox2)
    boxes.append(newbox3)
    boxes.append(newbox4)

#ball
ball = sphere(pos = vec(0,-L/4,0), radius = R, color = color.red)

#initial velocity
s = 3000
ball.v = s*hat(vec(2*rand.random()-1, 2*rand.random()-1, 0))

#time
t = 0
dt = R/mag(ball.v)/10

still_left = True

scene1.pause()

#starts scene
while still_left:
    rate(250)

    #sets the loop control variable
    #if an iteration of the loop completes with this set to false, the program ends
    #this should only occur if all the boxes have been removed
    still_left = False
    
    #updates ball's position, using the current velocity    
    ball.pos = ball.pos + ball.v*dt
    
    if (abs(ball.pos.x) > L/2): #reflect in x-direction
        ball.v.x = -ball.v.x
    if (ball.pos.y > L/2): #reflect in y-direction
        ball.v.y = -ball.v.y
    if (ball.pos.y < - L/2): #reflects w/ random direction off the bottom
        ball.v = s*hat(vec(2*rand.random()-1, abs(2*rand.random()-1),0))
        
    #handles collisions    
    for b in boxes:
        #if the ball collides with the right side of the box
        if (ball.pos.x-R <= b.pos.x+L/12) and (ball.pos.x+R >= b.pos.x+L/12) and (ball.pos.y > b.pos.y-L/20) and (ball.pos.y < b.pos.y+L/20) and b.visible == True:
            b.visible = False
            ball.v.x = -ball.v.x
        #if the ball collides with the left side of the box    
        elif (ball.pos.x-R <= b.pos.x-L/12) and (ball.pos.x+R >= b.pos.x-L/12) and (ball.pos.y > b.pos.y-L/20) and (ball.pos.y < b.pos.y+L/20) and b.visible == True:
            b.visible = False
            ball.v.x = -ball.v.x  
        #if the ball collides with the top/bottom of the box
        elif ((ball.pos.y+R) >= (b.pos.y-L/20)) and ((ball.pos.x) <= (L/12+b.pos.x) and (ball.pos.x) >= (b.pos.x-L/12)) and b.visible == True:
            b.visible = False
            ball.v.y = -ball.v.y    
        
        if b.visible == True:
            still_left = True

    #updates time step
    t = t + dt
