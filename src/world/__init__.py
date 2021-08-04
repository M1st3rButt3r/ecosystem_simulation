class Tile:
    def __init__(self, size):
        self.populations = []
        self.size = size
        self.space = size

    def add_population(self, population):
        population.tile = self
        self.populations.append(population)

    def calculate_development(self):
        self.calculate_population_development()

    def calculate_population_development(self):
        for population in self.populations:
            population.calculate_development()
        for population in self.populations:
            population.apply_development()
