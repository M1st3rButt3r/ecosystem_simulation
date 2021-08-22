from matplotlib import pyplot as plt
from src.world import Tile
from src.species import Species, Population


tile = Tile()

foxes = Species("Fox", 0.5, 0.1)
fox_population = Population(foxes, 5)
tile.add_population(fox_population)

rabbits = Species("Rabbit", 0.6, 0.3)
rabbit_population = Population(rabbits, 200)
tile.add_population(rabbit_population)

# Predator/prey assignment
foxes.add_prey(rabbits)

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

print(tile.populations[0].count_over_time[iterations - 1])
print(tile.populations[1].count_over_time[iterations - 1])
