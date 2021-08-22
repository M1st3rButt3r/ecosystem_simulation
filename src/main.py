from matplotlib import pyplot as plt
from world import Tile
from species import Species, Population


def main():
    tile = Tile(50000)

    foxes = Species("Fox", 0.5, 0.1)
    fox_population = Population(foxes, 5)
    tile.add_population(fox_population)

    rabbits = Species("Rabbit", 6, 0.3)
    rabbit_population = Population(rabbits, 500)
    tile.add_population(rabbit_population)

    bunnies = Species("Bunnies", 5, 0.1)
    bunny_population = Population(bunnies, 50)
    tile.add_population(bunny_population)

    # Predator/prey assignment
    foxes.add_prey(rabbits)
    # foxes.add_prey(bunnies)

    iterations = 78

    time_steps = list(range(iterations))

    for _ in range(iterations):
        tile.calculate_development()

    for population in tile.populations:
        plt.plot(time_steps, population.count_over_time, label=population.species.name)
    plt.legend()
    plt.show()

    print(tile.populations[0].count_over_time[-1])
    print(tile.populations[1].count_over_time[-1])
    print(tile.populations[2].count_over_time[-1])


if __name__ == "__main__":
    main()
