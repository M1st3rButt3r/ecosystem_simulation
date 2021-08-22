class Species:
    def __init__(self, name, birth_rate, mortality_rate):
        self.name = name
        self.birth_rate = birth_rate  # New organism per individual
        # Mortality might be replaced with age (e.g. age 80 means every 1/80th individual should die)
        self.mortality_rate = mortality_rate  # Probability of dying through natural causes
        self.predators = []
        self.prey = []

    def add_prey(self, species):
        self.prey.append(species)
        species.add_predator(self)

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

    def save_for_graph(self):
        self.count_over_time.append(self.count)

    def apply_development(self):
        self.count += self.development

        if self.count < 2:
            self.go_extinct()

    def go_extinct(self):
        self.count = 0

    def calculate_available_food_herbivores(self, total_food_needed):
        if total_food_needed == 0:
            self.available_food = 0
            return
        percentage_of_food = min(1, self.tile.plant_food / total_food_needed)
        self.available_food = 1 * percentage_of_food

    def calculate_available_food_carnivores(self):
        # TODO: Get all the possible prey.count and calculate how many of them could be consumed
        # Do this for all predators in the end share all the values and if 2 or more species are competing,
        # let them fight for overlapping prey. Then sum up all they've got, don't let them kill what they can't eat and
        # give back the food amount

        food = self.available_food_count()
        if food > 0 and self.count > 0:
            self.available_food = (food * 0.01) / self.count
            self.available_food = min(self.available_food, 1)
        else:
            self.available_food = 0

    def available_food_count(self):
        count = 0
        for population in self.tile.populations:
            if population.species in self.species.prey:
                count += population.count
        return count

    def calculate_incline(self):
        self.development = self.count * self.species.birth_rate

    def calculate_decline(self):
        if self.available_food <= 0:
            self.development = -self.count
            return
        decline = 0
        decline += self.calculate_decline_from_predators()
        decline += self.calculate_decline_from_natural_deaths()
        decline += (self.count - decline) * (1 - self.available_food)
        self.development = -decline

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
        # TODO: Unify with prey taken for food
        return predator.count * 2 #* self.count * 0.002

    def calculate_decline_from_natural_deaths(self):
        return self.count * self.species.mortality_rate
