#-------------------------------------------------------------------------------
# Name:        agentframework_final_180204
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


# Import radom module for creation of agents
import random


# Creating Agent class and the relevant environment
class Agent():
    def __init__(self, environment, agents, neighbourhood):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.neighbourhood = neighbourhood

# Movment of agents withing the defined environment
# Limiting movement to the "environment" perimeter
# If an agents "leaves" environment it will reappear on the oposite side
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y +1) % len(self.environment)
        else:
            self.y = (self.y -1) % len(self.environment)

        if random.random() < 0.5:
            self.x = (self.x +1) % len(self.environment)
        else:
            self.x = (self.x -1) % len(self.environment)

# Nibbling away the current location
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10

# Defining the distance between the agent and its sibblings
# a2+b2=c2... Pythagoras - Ellada kai pali Ellada!
    def distance_between(self, agent):
        return(((self.x - agent.x)**2)+((self.y - agent.y)**2))**0.5

# if within neigbourhood eat only an "average" portion
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                avg = sum/2
                self.store = avg
                agent.store = avg
            #print("sharing" + str(dist) + " " + str(avg))





