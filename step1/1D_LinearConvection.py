# Step1: 1D Linear Convection

import numpy as np
import pylab as pl
pl.ion() # all functions will be plot on the same graph (Matlab hold on)

D = 2.0 # lenght of the domain
T = 0.625 # total amount of time for the analysis

nx = 41 # number of grid points
dx = D/(nx-1) # distance between any pair of adjacent grid points

nt = 25 # number of time iterations
dt = T/nt # amount of time each timestep covers

c = 1.0 # consider a wave speed of c = 1 m/s

grid = np.linspace(0,2,nx) # creating the initial grid

u = np.ones(nx) # creating the initial conditions
u[0.5/dx:1/dx+1] = 2 # initial velocity is 2 between 0.5-1 and 1 in the rest
# print the initial conditions; to print them, remove the hashtag
#print u

# plot the initial conditions; you can save the plot afterwards
#pl.plot(grid,u)

un  = np.ones(nx) # used only to initialize a temporary array

for n in range(nt): # loop for time iteration
    un = u.copy() # copy the existing values of u into un
    for i in range(1,nx): # looping through the grid
        u[i] = un[i]-c*dt/dx*(un[i]-un[i-1]) # the scheme
    pl.plot(grid,u) # this will plot u for every time step

# Discussion:
# the wave has moved to the right and changed the shape
# the hight of the curve represents the velocity of the wave
# that is the velocity decrease with the pass of time
# increasing the total time we will make the scheme unstable
# therefore the correct selection of time-step and space-step is critical
