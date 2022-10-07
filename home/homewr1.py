class Hero:
    def __init__(self, name, hp, damage, nickname):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.nickname = nickname

    def Heal(self,kjhg):
        print(self.hp + 100)

    def Two_damage(self, damage):
        print(self.damage * 2)

    def Dreetings(self, t):
        print('my name is ',self.name)

    def Brand_phrase(self, ug):
        print('Good will win')


Spider_Man = Hero("Peter", 200, 50, 'spider_man')
print(Spider_Man.name, Spider_Man.damage, Spider_Man.hp, Spider_Man.nickname)
Spider_Man.Heal(Hero)
Wonder_woman = Hero("Diana", 300, 100, 'wonder_woman')
print(Wonder_woman.nickname, Wonder_woman.name, Wonder_woman.hp, Wonder_woman.damage)
Wonder_woman.Two_damage(Hero)
Super_Snoop_dog = Hero("Calvin_Cordozar_Broadus_Jr", 80, 100000000, 'Super_Snoop_dog')
print(Super_Snoop_dog.nickname, Super_Snoop_dog.hp, Super_Snoop_dog.damage, Super_Snoop_dog.name)
Super_Snoop_dog.Dreetings(Hero)
Doctor_Doom = Hero("Arsen", 400, 500, "doctor_doom")
print(Doctor_Doom.nickname, Doctor_Doom.name, Doctor_Doom.damage, Doctor_Doom.hp)
Doctor_Doom.Two_damage(Hero)
