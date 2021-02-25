class Vet:
    animals = []
    space = 5
    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal):
        if self.space <= len(self.animals):
            return f"Not enough space"

        self.animals.append(animal)
        Vet.animals.append(animal)
        return f"{animal} registered in the clinic"

    def unregister_animal(self, animal):
        if animal not in self.animals:
            return f"{animal} not in the clinic"

        self.animals.remove(animal)
        Vet.animals.remove(animal)
        return f"{animal} unregistered successfully"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space left in the clinic"
