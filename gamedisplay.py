from dataanalysis import DataAnalysis
from Particle import RandomParticle
from Board import RandomBoard
import os

#scipt file
#------------------------------------------------------------------------

#constant
NUM_ITERATIONS = 10000
NUM_PARTICLES = 1

board = RandomBoard(-100, -100, 100, 100)
particle1 = RandomParticle(0, 0, 1)
board.add_particle(particle1)


#simulation
index = 0
for particle in board.database:
    #creation of folder for the specific particle
    path = "DataFolder/particle%s" % index
    if not os.path.exists(path):
        os.makedirs(path)

    #temporarily recording the initial state
    x_temp = particle.get_x()
    y_temp = particle.get_y()

    #keeping data of the several iterations
    for i in range(NUM_ITERATIONS):
        filename = "iteration%s.txt" % i
        #particle returning to initial state
        particle.set_coordinates(x_temp, y_temp)
        board.move_particle(particle)
        board.save_data(filename, path)
    index += 1

#data analysis

#since we have only one particle, we will implement analysis
#of one particle

reader = DataAnalysis()
set_of_database = []

for i in range(NUM_ITERATIONS):
    path = "DataFolder/particle0/iteration%s.txt" % i
    database = reader.get_data(path)
    set_of_database.append(database)

[x_ave, y_ave] = DataAnalysis.average_displacement(set_of_database)


#saving the calculated average value
filename = "DataFolder/particle0/average.txt"
results = open(filename, "w") 
for i in range(RandomBoard.NUM_STEP):
    results.write("%s %s\n" % (x_ave[i], y_ave[i]))
results.close()
