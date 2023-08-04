import random

class Hero:
    def __init__(self, name, hp, attack, armor):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.armor = armor

    def serang(self, lawan):
        print(
            self.name,
            f"({self.attack}.str)",
            "menyerang =>>",
            lawan.name,
            f"({lawan.armor}.deff)",
        )
        print(self.hp, f"/{self.max_hp} \t\t {lawan.hp}/", lawan.max_hp)
        att = self.attack / lawan.armor
        lawan.hp -= att
        print("=>>#_<\n\n")

    def menang(self):
        print(f"Horee! {self.name} menang!")


hp1 = random.randint(100, 110)
hp2 = random.randint(105, 120)
ravi = Hero("Ravi", hp1, 20, 10)
vira = Hero("Vira", hp2, 10, 10)
while True:
    her = [ravi, vira]
    hero = random.choice(her)
    if hero.name == "Ravi":
        hero.attack = random.randint(20, 30)
        vira.armor = random.randint(20, 30)
        hero.serang(vira)
        if vira.hp < 0:
            hero.menang()
            break
    else:
        hero.serang(ravi)
        if ravi.hp < 0:
            hero.menang()
            break
