#-------------------------------------------------------------------------------
# Name:        model_final_180204
# Purpose:
#
# Author:      Michael Iseli
#
# Created:     23/01/2018
# Copyright:   (c) iseli 2018
#-------------------------------------------------------------------------------


'''
Coding for GEOG5991M
Assessment1
Geographical Information Analysis
module for MSc GIS at University of Leeds
Tutor: Dr. Andy Evans
All code derived from practical handouts by Dr. Evans
'''


# Import of all modules required for the model
import matplotlib.pyplot
import matplotlib.animation
import agentframework_final_180204
import csv


# Creating two lists;
# 1. Environment within which the agents move
# 2. The shell to hold the agents inside the environment
environment = []
agents = []

# Model parameters for:
# - number of agents
# - number of iterations (moves)
# - size of neighbourhood
num_of_agents = 20
num_of_iterations = 250
neighbourhood = 20

# Definition of the models window size for the animation
fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1])

# Reading and displaying of raster img in csv format for the environment
f=open('in.txt', newline='')
reader=csv.reader (f, quoting = csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist = []
    for item in row:
        rowlist.append(item)
    environment.append(rowlist)
f.close()

# Importing the agents from "agentframework"
# Fusion of agents with the environment
for i in range(num_of_agents):
    agents.append(agentframework_final_180204.Agent(environment, agents, neighbourhood))

# Creating the animation of the agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
carry_on = True

def update (frame_number):
    fig.clear()
    global carry_on

for i in range(num_of_agents):
    agents[i].move()
    agents[i].eat()
    agents[i].share_with_neighbours(neighbourhood)
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    matplotlib.pyplot.imshow(environment)

