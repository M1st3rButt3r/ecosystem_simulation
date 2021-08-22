class Tile:
    def __init__(self, plant_food):
        self.plant_food = plant_food
        self.populations = []

    def add_population(self, population):
        population.tile = self
        self.populations.append(population)

    def calculate_development(self):
        self.calculate_population_development()

    def calculate_population_development(self):
        self.calculate_available_food()
        for population in self.populations:
            population.calculate_decline()
        for population in self.populations:
            population.apply_development()
            population.save_for_graph()
        for population in self.populations:
            population.calculate_incline()
        for population in self.populations:
            population.apply_development()

    def calculate_available_food(self):
        total_food_needed = 0
        for population in self.populations:
            if len(population.species.prey) > 0:
                continue
            total_food_needed += population.count

        for population in self.populations:
            if len(population.species.prey) > 0:
                population.calculate_available_food_carnivores()
                continue
            population.calculate_available_food_herbivores(total_food_needed)
