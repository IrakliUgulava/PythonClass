from dataanalysis import DataAnalysis
import matplotlib.pyplot as plt
import numpy as np
import os
import pygame

reader = DataAnalysis()
data = reader.get_data("DataFolder/particle0/average.txt")

x_size = 400
y_size = 400

plt.plot(data[:, 0], data[:, 1])
plt.axis([-100, 100, -100, 100])
plt.show()

pygame.init()
screen = pygame.display.set_mode((x_size, y_size))

for i in range(1000):
    screen.fill((0, 0, 0))
    x_pos = x_size/2 + 2*data[i, 0]
    y_pos = y_size/2 + 2*data[i, 1]
    
    pygame.draw.circle(screen, (0, 250, 0), (x_pos, y_pos), 10)
    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()


