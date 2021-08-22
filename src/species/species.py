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
