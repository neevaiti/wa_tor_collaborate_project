import random as rd


class World:
    # Définition du monde
    def __init__(self, lines_number, column_number, fish, shark) -> None:
        self.lines_number = lines_number
        self.column_number = column_number
        self.grille = []
        self.fish = fish
        self.shark = shark

    def empty_world(self):
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
            liste_thons.append(Poisson(random_1, random_2))
            self.grille[random_1][random_2] = "🐡"
        for i in range(0, self.shark):
            random_1 = rd.randint(0, self.lines_number - 1)
            random_2 = rd.randint(0, self.column_number - 1)
            while self.grille[random_1][random_2] != "🌊":
                random_1 = rd.randint(0, self.lines_number - 1)
                random_2 = rd.randint(0, self.column_number - 1)
            liste_requins.append(Requin(random_1,random_2))
            self.grille[random_1][random_2] = "🦈"
            
    def display_world(self):
        for ligne in self.grille:
            for elt in ligne:
                print('|', elt, '|', end="")
            print("\n")



class Poisson:
    
    
    def __init__(self, coordonnees_x ,coordonnees_y):
        self.compteur_reproduction = 0
        self.coordonnees_x = coordonnees_x
        self.coordonnees_y = coordonnees_y
        
        
    
    def se_deplacer(self):
        ancien_x = self.coordonnees_x
        ancien_y = self.coordonnees_y
        print(f'Avant : {ancien_x} {ancien_y}')
        while mon_monde.grille[self.coordonnees_x][self.coordonnees_y] != "🌊":
            thon.coordonnees_x = ancien_x + (rd.randint(-1,1))
            if thon.coordonnees_x < 0 :
                thon.coordonnees_x = mon_monde.lines_number-1
            if thon.coordonnees_x > mon_monde.lines_number-1 :
                thon.coordonnees_x = 0
            thon.coordonnees_y = ancien_y + (rd.randint(-1,1))
            if thon.coordonnees_y > mon_monde.column_number-1 :
                thon.coordonnees_y = 0
            if thon.coordonnees_y < 0 :
                thon.coordonnees_y = mon_monde.column_number-1    
        print(f'Après : {self.coordonnees_x} {self.coordonnees_y}')
        mon_monde.grille[ancien_x][ancien_y] = "🌊"  
        mon_monde.grille[self.coordonnees_x][self.coordonnees_y] = "🐡"
        
        
        
    def se_reproduire(self):   
        self.compteur_reproduction += 1
        if self.compteur_reproduction == 3 : 
            while mon_monde.grille[self.coordonnees_x][self.coordonnees_y] != "🌊":
                self.coordonnees_y -= 1
                if self.coordonnees_y < 0 :
                    self.coordonnees_y = mon_monde.column_number-1
            mon_monde.grille[self.coordonnees_x][self.coordonnees_y] = "🐡"
            liste_thons.append(Poisson(self.coordonnees_x, self.coordonnees_y))
            
            

class Requin(Poisson):
    
    def __init__(self, coordonnees_x, coordonnees_y):
        self.compteur_reproduction = 0
        self.energie = 10
        self.coordonnees_x = coordonnees_x
        self.coordonnees_y = coordonnees_y
        
       
    
    def se_deplacer(self):
        pass
    

        


liste_thons = []
liste_requins = []
mon_monde = World(10,10,3,3)
mon_monde.empty_world()
mon_monde.fill_world()
mon_monde.display_world()
print('------------------------')
for thon in liste_thons:
    print([thon.coordonnees_x, thon.coordonnees_y])
for thon in liste_thons:
    thon.se_deplacer()
mon_monde.display_world()
print('------------------------')
for thon in liste_thons:
    thon.se_reproduire()
mon_monde.display_world()
print('------------------------')
for thon in liste_thons:
    print([thon.coordonnees_x, thon.coordonnees_y])
for thon in liste_thons:
    thon.se_deplacer()
mon_monde.display_world()
print('------------------------')
for thon in liste_thons:
    thon.se_reproduire()
mon_monde.display_world()
print('------------------------')
for thon in liste_thons:
    print([thon.coordonnees_x, thon.coordonnees_y])
for thon in liste_thons:
    thon.se_deplacer()
mon_monde.display_world()
print('------------------------')
for thon in liste_thons:
    thon.se_reproduire()
mon_monde.display_world()
print('------------------------')
for thon in liste_thons:
    print([thon.coordonnees_x, thon.coordonnees_y])
for thon in liste_thons:
    thon.se_deplacer()
mon_monde.display_world()













        
    