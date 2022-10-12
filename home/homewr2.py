from homewr1 import Hero


class Air(Hero):
    head = 1

    def __init__(self, name, hp, damage, nickname, fly = False):
        super().__init__(name, hp, damage, nickname)
        self.fly = fly

    def Brand_phrase(self):
        self.fly = True
        print(f"fly in the {self.fly}_phrase")

    def __Gen_x(self):
        pass


class Space(Hero):
    head = 1

    def __init__(self, name, hp, damage, nickname, fly = False):
        super().__init__(name, hp, damage, nickname)
        self.fly = fly

    def Brand_phrase(self):
        self.fly = True
        print(f"fly in the {self.fly}_phrase")

    def __Gen_x(self):
        pass


class Earth(Hero):
    head = 1

    def __init__(self, name, hp, damage, nickname, fly = False):
        super().__init__(name, hp, damage, nickname)
        self.fly = fly

    def Brand_phrase(self):
        self.fly = True
        print(f"fly in the {self.fly}_phrase")

    def __Gen_x(self):
        pass


Earth = Earth("Dan", 150, 100, "Earthman")
Air = Air("Alan", 160, 100, "Airman")
Space = Space("Lake", 140, 100, "Spaceman")
Space.Brand_phrase()

