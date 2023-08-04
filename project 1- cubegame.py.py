#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint
import time


class Cube(object):
    suits = ["", "", "", "", "", "", "", ""]
    values = [0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self):
        self.endgame_points = 0

    def fill_suits(self):
        su = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for i in range(8):
            self.suits[i] = su[i]

    def fill_values(self):
        for i in range(8):
            self.values[i] = randint(1, 10)

    def show_cubes(self):
        for i in range(8):
            print(f"[{self.suits[i]}]", end="")

    def show_value(self, i, name):
        print(f"{name} has reveled cube [{self.suits[i]}] with a value of {self.values[i]}")
        self.suits[i] = str(self.values[i])

    def update_endgame_points(self):
        self.endgame_points = self.endgame_points + 1

    def check_if_already_chosen(self, cube):
        chosen = True
        for i in range(8):
            if cube == self.suits[i] and cube != str(self.values[i]):
                chosen = False
                break
            elif cube == self.suits[i] and cube == str(self.values[i]):
                chosen = True
                break
            else:
                chosen = True

        return chosen


class User(object):
    def __init__(self):
        self.name = "CPU"
        self.score = 0

    def update_score(self, i):
        self.score = self.score + Cube.values[i]

    def show_score(self):
        print(f"{self.name} your score is: {self.score} ")

    def choose_cube(self):
        print("Please enter the letter of your cube: ")
        cube = input().upper()
        chosen = Cube.check_if_already_chosen(Cube(), cube)
        while chosen is True:
            print("This cube was already chosen. Please select another one: ")
            cube = input().upper()
            chosen = Cube.check_if_already_chosen(Cube(), cube)
        for i in range(8):
            if cube == Cube().suits[i]:
                self.update_score(i)
                Cube.show_value(Cube(), i, self.name)
                self.show_score()

    def check_winner(self, other_score):
        if self.score > other_score:
            print(f"\nCONGRATULATIONS {self.name} you have won!")
        elif self.score < other_score:
            print(f"\nSorry, {self.name} you have lost. Good luck next time!")
        else:
            print(f"\nThere's a tie. Both of you won!")


class Cpu(User):
    def __init__(self):
        super(User).__init__()
        self.name = "CPU"
        self.score = 0

    def show_score(self):
        print(f"CPU's score is: {self.score}")

    def choose_cube(self):
        cube = Cube().suits[randint(0, 7)]
        chosen = Cube.check_if_already_chosen(Cube(), cube)
        while chosen is True:
            cube = Cube.suits[randint(0, 7)]
            chosen = Cube.check_if_already_chosen(Cube(), cube)
        for i in range(8):
            if cube == Cube().suits[i]:
                self.update_score(i)
                Cube.show_value(Cube(), i, self.name)
                self.show_score()


class Player(User):
    def __init__(self):
        super(User).__init__()
        self.set_name()
        self.score = 0

    def set_name(self):
        print("\nWhat's your name? ")
        self.name = input()


def menu():
    print("\n---------WELCOME TO THE [CUBE] GAME----------"
          "\n\t1) Player Vs. CPU"
          "\n\t2) Multiplayer"
          "\n\t0) EXIT")
    print("\n\nSelect a game mode: ")
    option = input()

    return option


if __name__ == "__main__":
    opt = ""
    while opt != "0":
        cubes1 = Cube()
        opt = menu()
        if opt == "1":
            print("\n\n[  P L A Y E R    V S.   C P U  ]")
            cubes1.fill_suits()
            cubes1.fill_values()
            player = Player()
            cpu = Cpu()
            while cubes1.endgame_points < 8:
                time.sleep(2)
                cubes1.show_cubes()
                print(f"\n\n{player.name} it's your turn...")
                player.choose_cube()
                cubes1.update_endgame_points()

                time.sleep(4)
                cubes1.show_cubes()
                print("\n\nIt's the CPU'S turn...")
                cpu.choose_cube()
                cubes1.update_endgame_points()

            print("\nFinal Score: "
                  f"\n{player.name}: {player.score}"
                  f"\n{cpu.name}: {cpu.score}")
            player.check_winner(cpu.score)
            input()
        elif opt == "2":
            print("\n\n[  M U L T I P L A Y E R  ]")
            cubes1.fill_suits()
            cubes1.fill_values()
            player1 = Player()
            player2 = Player()
            while cubes1.endgame_points < 8:
                time.sleep(2)
                cubes1.show_cubes()
                print(f"\n\n{player1.name} it's your turn...")
                player1.choose_cube()
                cubes1.update_endgame_points()

                time.sleep(2)
                cubes1.show_cubes()
                print(f"\n\n{player2.name} it's your turn...")
                player2.choose_cube()
                cubes1.update_endgame_points()

            print("\nFinal Score: "
                  f"\n{player1.name}: {player1.score}"
                  f"\n{player2.name}: {player2.score}")
            player1.check_winner(player2.score)
            player2.check_winner(player1.score)
            input()

