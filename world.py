import random as rd


class World:
    # Définition du monde
    def __init__(self, lines_number, column_number, grille, fish, shark) -> None:
        self.lines_number = lines_number
        self.column_number = column_number
        self.grille = grille
        self.fish = fish
        self.shark = shark

    def create_world(self):
        self.grille = []
        for i in range(0, self.lines_number):
            une_ligne = []
            self.grille.append(une_ligne)
            for j in range(0, self.column_number):
                une_ligne.append("🌊")
        return self.grille

    def fill_world(self):
        for i in range(0, self.fish):
            random_1 = rd.randint(0, self.lines_number - 1)
            random_2 = rd.randint(0, self.column_number - 1)
            while self.grille[random_1][random_2] != "🌊":
                random_1 = rd.randint(0, self.lines_number - 1)
                random_2 = rd.randint(0, self.column_number - 1)
            self.grille[random_1][random_2] = "🐡"
        for i in range(0, self.shark):
            random_1 = rd.randint(0, self.lines_number - 1)
            random_2 = rd.randint(0, self.column_number - 1)
            while self.grille[random_1][random_2] != "🌊":
                random_1 = rd.randint(0, self.lines_number - 1)
                random_2 = rd.randint(0, self.column_number - 1)
            self.grille[random_1][random_2] = "🦈"

    def display_world(self):
        for ligne in self.grille:
            for elt in ligne:
                print('|', elt, '|', end="")
            print("\n")


mon_monde = World(5, 5, "", 3, 3)
mon_monde.create_world()
mon_monde.fill_world()
mon_monde.display_world()


class Animals:

    def __init__(self, ):