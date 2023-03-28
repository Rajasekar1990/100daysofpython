class WildAnimal:
    def __init__(self):
        self.eyes = 2
        self.legs = 4

    def run(self):
        print("running")


class Omnivores(WildAnimal):
    def __init__(self):
        super().__init__()

    def prey(self):
        super().run()
        print("run while Hunting")


lion = Omnivores()
lion.prey()
# lion.breathe()
print(f"eyes = {lion.eyes}, legs = {lion.legs}")
