import numpy as np
import os
from Board import RandomBoard
import matplotlib.pyplot as plt

class DataAnalysis:
    
    #empty constructor
    def __init__(self):
        self.data_size = RandomBoard.NUM_STEP
        self.database = np.zeros((self.data_size, 2), dtype = "float64")

    #file data import
    def get_data(self, directory):
        #opening file to read
        data = open(directory, "r")
        content = data.read()

        #parsing contained string into single numbers
        list = content.split()

        #keeping data in the storage
        for i in range(len(list)):
            #if index is even, we are stopped at x_pos
            #if index is even, we are stopped at y_pos
            if i % 2 == 0:
                x_pos = float(list[i])
                self.database[i // 2, 0] = x_pos
            else:
                y_pos = float(list[i])
                self.database[i // 2, 1] = y_pos

        #returning the database
        return self.database

    #static method
    #finds average displacement for every given moment
    def average_displacement(set_of_database):
        
        #defining the averaged displacement
        x_ave = np.zeros(RandomBoard.NUM_STEP, dtype = "float64")
        y_ave = np.zeros(RandomBoard.NUM_STEP, dtype = "float64")

        #counts number of database in the set
        counter = 0
        for database in set_of_database:
            x_ave += database[:, 0]
            y_ave += database[:, 1]
            counter += 1

        #calculates the average value
        x_ave = x_ave / counter
        y_ave = y_ave / counter

        #returning the average value
        return x_ave, y_ave

    

