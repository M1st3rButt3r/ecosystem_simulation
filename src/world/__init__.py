class Tile:
    def __init__(self):
        self.populations = []

    def add_population(self, population):
        population.tile = self
        self.populations.append(population)

    def calculate_development(self):
        self.calculate_population_development()

    def calculate_population_development(self):
        for population in self.populations:
            population.calculate_development()
        for population in self.populations:
            population.calculate_decline()
        for population in self.populations:
            population.apply_development()
        for population in self.populations:
            population.calculate_incline()
        for population in self.populations:
            population.apply_development()
            population.save_for_graph()
