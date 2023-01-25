import random as rd


class World:
    # Définition du monde
    def __init__(self, lines_number, column_number, fish, shark) -> None:
        self.lines_number = lines_number
        self.column_number = column_number
        self.grille = []
        self.fish = fish
        self.shark = shark

    def create_world(self, lines_number, column_number):
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
            liste_thons.append([random_1, random_2])
            self.grille[random_1][random_2] = "🐡"
        for i in range(0, self.shark):
            random_1 = rd.randint(0, self.lines_number - 1)
            random_2 = rd.randint(0, self.column_number - 1)
            while self.grille[random_1][random_2] != "🌊":
                random_1 = rd.randint(0, self.lines_number - 1)
                random_2 = rd.randint(0, self.column_number - 1)
            liste_requins.append([random_1,random_2])
            self.grille[random_1][random_2] = "🦈"

    def display_world(self):
        for ligne in self.grille:
            for elt in ligne:
                print('|', elt, '|', end="")
            print("\n")




class Poisson:
    
    
    def __init__(self, compteur_reproduction):
        self.compteur_reproduction = compteur_reproduction
        
    
    def se_deplacer(self):
        pass        
            

class Requin(Poisson):
    
    def __init__(self,compteur_reproduction, energie):
        self.compteur_reproduction = compteur_reproduction
        self.energie = energie 
       
    
    def se_deplacer(self):
        pass
    

        




liste_thons = []
liste_requins = []
mon_monde = World(5,5,3,3)
mon_monde.create_world(5,5)
mon_monde.fill_world()
mon_monde.display_world()
print(liste_thons)
print(liste_requins)






        
    