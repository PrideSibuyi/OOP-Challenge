class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        # Reduce hunger by 3 (minimum 0) and increase happiness by 1
        self .hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating. . . ")

    def sleep(self):
        # Increase energy by 5 (maximum 10)
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping. . . ")

    def play(self):
        # Decrease energy by 2, increase happiness by 2, and increase hunger by 1
        # Check if the pet is too tired to play
        if self.energy <= 0:
            print(f"{self.name} is too tired to play.")
            return
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} is playing. . . ")

    def train(self, trick):
        # Teach pet a new trick if it doesn't already know it
        if trick in self.tricks:
            print(f"{self.name} already knows '{trick} !' ")
            return
        else:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: '{trick} !' ")


    def show_tricks(self):
        # Display the tricks the pet knows
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet.")
        else:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")

    def get_status(self):
        # Print the current status of the pet
        status = (
            f"{self.name}'s current status:\n"
            f"Hunger: {self.hunger}\n"
            f"Energy: {self.energy}\n"
            f"Happiness: {self.happiness}\n"
        )
        if self.tricks:
            status += f"Tricks: {self.tricks}\n"
            print(status)