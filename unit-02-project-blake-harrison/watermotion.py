import ode
import numpy as np
import matplotlib.pyplot as plt
from vpython import *

g = 9.87 #gravitational constant
m = 5 #projectile mass
r = 5
xpi = 0 #initial x position of the object
ypi = 0 #initial y position of the object
wlevel = 10 #water level
rho_h2o = 1000 #p of water kg/m^3
rho_air = 1.2 #p of air kg/m^3
C = 0.47 #drag coefficient
A = np.pi * r**2#cross-sectional area
V = 4/3 * np.pi * r **3 #volume of sphere
vx0 = 5 #k/h (initial x velocity)
vy0 = 0 #k/h (initial y velocity)

t = 0
h = 0.1
nSteps = 1000

ypos = 0
xpos = 0
vx = vx0
vy = vy0

xposarray = np.zeros(nSteps)
xposarray[0] = xpi
yposarray = np.zeros(nSteps)
yposarray[0] = ypi
tarray = np.zeros(nSteps)
tarray[0] = t

def getBuoyancy():
    return rho_h2o * g * V

def getGrav(m):
    return m * g

def getDrag(rho, v):
    return (1/2) * C * rho * A * v**2

for n in range(0, nSteps-1):
    if(ypos>wlevel):
        fg = getGrav(m)
        fd = getDrag(rho_air,vy)
        vx += fd * h
        vy += fg * h
    else:
        fg = getGrav(m)
        fd = getDrag(rho_h2o,vy)
        fb = getBuoyancy()
        fnety = fb * fg
        vx += fd * h
        vy += fnety * h    

    xposarray[n+1] = xpos+(vx*h)
    yposarray[n+1] = ypos+(vx*h)
    
    t = t+h
    
fig = plt.figure()
plt.title("Motion of Ball Underwater")
plt.plot(xposarray, yposarray, 'b-', label='Path of the Ball')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.show()

########################
#try 2##################
########################

import ode
import numpy as np
import matplotlib.pyplot as plt

g = 9.8 #N/kg
rho_air = 1.2 #kg/m^3
rho_water = 1e4 #kg/m^3
mu = 1.8e-5 #kg/m/s
r = 50e-3/2 #50 mm diameter
A = np.pi*r**2 #cross-sectional area
Cd = 0.5 #actually depends on speed
m = 0.15 #kg
V = 4/3 * np.pi * r **3 #volume of the sphere
draga = 1/2*Cd*rho_air*A
dragw = 1/2*Cd*rho_water*A
buoy = rho_water*g*V

thetadeg = 25 #deg
vmag0 = 70 #m/s
theta = thetadeg*np.pi/180 #convert deg to rad

x0 = 0
y0 = 0
vx0 = vmag0*np.cos(theta)
vy0 = vmag0*np.sin(theta)

data = np.array([x0,y0,vx0,vy0]) #initialize dep vars

t = 0
h = 0.01
Nsteps = 1000

traj = np.zeros((Nsteps,3)) #trajectory
traj[0,:] = np.array([t,x0,y0]) 

def drag(d, tn): #return value of derivatives at this t
    x = d[0]
    y = d[1]
    vx = d[2]
    vy = d[3]
    
    deriv = np.zeros(4) #contains derivatives of data
    deriv[0] = vx #dx/dt
    deriv[1] = vy #dy/dt
    speed = np.sqrt(vx**2+vy**2)
    deriv[2] = -draga*speed*vx/m #dvx/dt
    deriv[3] = (-draga*speed*vy - m*g)/m #dvy/dt

    return deriv
    
for n in range(0,Nsteps-1):
    
    #update data
    data = ode.rk4(drag,data,t,h) #4 arguments
    
    #update time
    t = t+h
    
    #store trajectory data
    if(data[0]>0 and data[1]>0):
        traj[n+1,:] = np.array([t,data[0],data[1]])
    else: 
        continue
    
plt.figure()
plt.title("Ball Motion Through Water")
plt.plot(traj[:,1], traj[:,2], 'b-')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()