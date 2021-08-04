class Species:
    def __init__(self, birth_rate, death_rate):
        self.birth_rate = birth_rate
        self.death_rate = death_rate
        self.predators = []
        self.food = []

    def add_food(self, species):
        self.food.append(species)

    def add_predator(self, predator):
        self.predators.append(predator)


class Population:
    def __init__(self, species, count):
        self.tile = None
        self.species = species
        self.count = count
        self.development = 0
        self.available_food = 0
        self.count_over_time = []

    def apply_development(self):
        self.count += self.development
        self.count_over_time.append(self.count)
        if self.count < 1:
            self.count = 0

    def calculate_development(self):
        self.calculate_available_food()
        self.development = self.calculate_incline() - self.calculate_decline()

    def calculate_available_food(self):
        if len(self.species.food) == 0 or self.count <= 0:
            self.available_food = 1
            return
        food = self.available_food_count()
        if food > 0:
            self.available_food = food / self.count * 0.01
            self.available_food = max(0, min(self.available_food, 1))
        else:
            self.available_food = 0

    def available_food_count(self):
        count = 0
        for population in self.tile.populations:
            if population.species in self.species.food:
                count += population.count
        return count

    def calculate_incline(self):
        return self.count * self.species.birth_rate * self.available_food

    def calculate_decline(self):
        decline = 0
        decline += self.calculate_decline_from_predators()
        decline += self.calculate_decline_from_deaths()
        return decline

    def get_predators(self):
        predators = []
        for population in self.tile.populations:
            if population.species in self.species.predators:
                predators.append(population)
        return predators

    def calculate_decline_from_predators(self):
        decline = 0
        predators = self.get_predators()
        for predator in predators:
            decline += self.calculate_decline_from_predator(predator)
        return decline

    def calculate_decline_from_predator(self, predator):
        return predator.count * self.count * 0.002

    def calculate_decline_from_deaths(self):
        return self.count * self.species.death_rate
