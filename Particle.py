import random
import numpy as np

#free particle
class Particle():
    
    #constructor
    def __init__(self, x_init, y_init, mass):
        self.x_pos = x_init
        self.y_pos = y_init
        self.mass = mass

    #move controll functions
    def move_up(self):
        self.y_pos += 1

    def move_down(self):
        self.y_pos -= 1

    def move_right(self):
        self.x_pos += 1

    def move_left(self):
        self.x_pos -= 1

    #move by given direction
    def move_by_order(self, order):
        if(order == "up"):
            self.move_up()
        elif(order == "down"):
            self.move_down()
        elif(order == "right"):
            self.move_right()
        elif(order == "left"):
            self.move_left()
            
    #setting coordinates
    def set_coordinates(self, x, y):
        self.x_pos = x
        self.y_pos = y
    
    #getter methods
    def get_x(self):
        return(self.x_pos)
    def get_y(self):
        return(self.y_pos)
    
    #current position show
    def current_position(self):
        print(self.x_pos)
        print(self.y_pos)

    #print particle info
    def print_particle_info(self):
        info = "%s %s %s\n" % (self.x_pos, self.y_pos, self.mass)
        print(info)







        
#----------------------------------------------------------
#randomly moving particle
class RandomParticle(Particle):

    # boarder of the board
    x_start = 0
    y_start = 0
    x_end = 100
    y_end = 100

    # check if particle encounters the walls
    def check_wall(self, order):
        if self.x_pos == RandomParticle.x_start and order == "left":
            order = "right"
        elif self.x_pos == RandomParticle.x_end and order == "right":
            order = "left"
        elif self.y_pos == RandomParticle.y_start and order == "down":
            order = "up"
        elif self.y_pos == RandomParticle.y_end and order == "up":
            order = "down"
        return order

    # random motion of the particle
    def random_motion(self):
        directions = ["up", "down", "right", "left"]
        order = random.choice(directions)
        order = self.check_wall(order)
        self.move_by_order(order)
        
    #print particle info
    def print_particle_info(self):
        info = "X position: %s, Y position %s, mass: %s\n" % (self.x_pos,self.y_pos,self.mass)
        print(info)






