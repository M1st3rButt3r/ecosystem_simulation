from matplotlib import pyplot as plt
from src.world import Tile
from src.species import Species, Population


tile = Tile(400)

foxes = Species(1, 0.1)
fox_population = Population(foxes, 50)
tile.add_population(fox_population)

rabbits = Species(0.6, 0.3)
rabbit_population = Population(rabbits, 200)
tile.add_population(rabbit_population)
rabbits.add_predator(foxes)
foxes.add_food(rabbits)

iterations = 500
current_iteration = 0

time_steps = []

while iterations >= current_iteration:
    time_steps.append(current_iteration)
    tile.calculate_development()
    current_iteration += 1

for population in tile.populations:
    plt.plot(time_steps, population.count_over_time)
plt.show()
