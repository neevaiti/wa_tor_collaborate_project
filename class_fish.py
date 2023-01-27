import random as rd
# rd.seed(11)


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
        
    
    def __eq__(self, other):
        if other.coordonnees_x == self.coordonnees_x and other.coordonnees_y == self.coordonnees_y:
            return True 
        else : 
            return False
        
        
    
    def se_deplacer(self):
        ancien_x = self.coordonnees_x
        ancien_y = self.coordonnees_y
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
        mon_monde.grille[ancien_x][ancien_y] = "🌊"  
        mon_monde.grille[self.coordonnees_x][self.coordonnees_y] = "🐡"
        print(f'tona move from {ancien_x},{ancien_y} to {self.coordonnees_x, self.coordonnees_y}')
        
        
        
    def se_reproduire(self):  
        self.compteur_reproduction += 1
        if self.compteur_reproduction == 3 : 
            print('parent :')
            print(self.coordonnees_x, self.coordonnees_y)
            bebe_poisson_y = self.coordonnees_y-1
            if bebe_poisson_y < 0 :
                bebe_poisson_y = mon_monde.column_number-1
            bebe_poisson_x = self.coordonnees_x
            while mon_monde.grille[self.coordonnees_x][bebe_poisson_y] != "🌊":
                bebe_poisson_y -= 1
                bebe_poisson_x -= 1
                if bebe_poisson_y < 0 :
                    bebe_poisson_y = mon_monde.column_number-1
                if bebe_poisson_x < 0 :
                    bebe_poisson_x = mon_monde.lines_number-1
            print(bebe_poisson_x, bebe_poisson_y)
            mon_monde.grille[bebe_poisson_x][bebe_poisson_y] = "🐡"
            liste_bebe_thons.append(Poisson(bebe_poisson_x, bebe_poisson_y))
            self.compteur_reproduction = 0
            
    def bebe_devient_grand(self):
        liste_thons.append(bebe_thon)
    
            
            

class Requin:
    
    def __init__(self, coordonnees_x, coordonnees_y):
        self.compteur_reproduction = 0
        self.energie = 5
        self.coordonnees_x = coordonnees_x
        self.coordonnees_y = coordonnees_y
    
    
    def __eq__(self, other):
        if other.coordonnees_x == self.coordonnees_x and other.coordonnees_y == self.coordonnees_y:
            return True 
        else : 
            return False
       
    
    def se_deplacer(self):
        ancien_x = self.coordonnees_x
        ancien_y = self.coordonnees_y
        while True :
            self.coordonnees_x = ancien_x - 1
            self.coordonnees_y = ancien_y
            if self.coordonnees_x < 0 :
                self.coordonnees_x = mon_monde.lines_number-1
            if mon_monde.grille[self.coordonnees_x][ancien_y] == "🐡":
                mon_monde.grille[self.coordonnees_x][ancien_y] = "🦈"
                liste_thons.remove(Poisson(self.coordonnees_x,self.coordonnees_y))
                self.energie += 1
                break
            self.coordonnees_x = ancien_x + 1
            self.coordonnees_y = ancien_y
            if self.coordonnees_x > mon_monde.lines_number-1 :
                self.coordonnees_x = 0
            if mon_monde.grille[self.coordonnees_x][ancien_y] == "🐡":
                mon_monde.grille[self.coordonnees_x][ancien_y] = "🦈"
                liste_thons.remove(Poisson(self.coordonnees_x,self.coordonnees_y))
                self.energie += 1
                break
            self.coordonnees_y = ancien_y + 1
            self.coordonnees_x = ancien_x
            if self.coordonnees_y > mon_monde.lines_number-1 :
                self.coordonnees_y = 0
            if mon_monde.grille[ancien_x][self.coordonnees_y] == "🐡":
                mon_monde.grille[ancien_x][self.coordonnees_y] = "🦈"
                liste_thons.remove(Poisson(self.coordonnees_x,self.coordonnees_y))
                self.energie += 1
                break
            self.coordonnees_y = ancien_y - 1
            self.coordonnees_x = ancien_x
            if self.coordonnees_y < 0 :
                self.coordonnees_y = mon_monde.lines_number-1
            if mon_monde.grille[ancien_x][self.coordonnees_y] == "🐡":
                mon_monde.grille[ancien_x][self.coordonnees_y] = "🦈"
                liste_thons.remove(Poisson(self.coordonnees_x,self.coordonnees_y))
                self.energie += 1
                break
            else :
                self.coordonnees_x = ancien_x
                self.coordonnees_y = ancien_y
                possibilites = []
                self.coordonnees_x = ancien_x + 1
                self.coordonnees_y = ancien_y
                if self.coordonnees_x > mon_monde.lines_number-1 :
                    self.coordonnees_x = 0
                possibilites.append([self.coordonnees_x, ancien_y])
                self.coordonnees_y = ancien_y + 1
                self.coordonnees_x = ancien_x
                if self.coordonnees_y > mon_monde.column_number-1 :
                    self.coordonnees_y = 0
                possibilites.append([ancien_x, self.coordonnees_y]) 
                self.coordonnees_x = ancien_x - 1
                self.coordonnees_y = ancien_y
                if self.coordonnees_x < 0 :
                    self.coordonnees_x = mon_monde.lines_number-1
                possibilites.append([self.coordonnees_x, ancien_y]) 
                self.coordonnees_y = ancien_y -1
                self.coordonnees_x = ancien_x
                if self.coordonnees_y < 0 :
                    self.coordonnees_y = mon_monde.column_number-1 
                possibilites.append([ancien_x, self.coordonnees_y])
                self.coordonnees_x = ancien_x
                self.coordonnees_y = ancien_y
                tour = 0
                print(possibilites)
                while mon_monde.grille[self.coordonnees_x][self.coordonnees_y] != "🌊" :
                    nouvelles_coordonnees = possibilites[0]
                    self.coordonnees_x = nouvelles_coordonnees[0]
                    self.coordonnees_y = nouvelles_coordonnees[1]
                    print(self.coordonnees_x)
                    print(self.coordonnees_y)
                    possibilites.remove(nouvelles_coordonnees)
                    print(possibilites)
                    tour += 1
                    if tour == 4 :
                        print('je peux pas bouger')
                        self.coordonnees_x = ancien_x
                        self.coordonnees_y = ancien_y
                        break
                mon_monde.grille[self.coordonnees_x][self.coordonnees_y] = "🦈"
                self.energie -= 1
                break
        print(f'shark move from {ancien_x},{ancien_y} to {self.coordonnees_x, self.coordonnees_y}')
        mon_monde.grille[ancien_x][ancien_y] = "🌊" 
        
    
    def se_reproduire(self):   
        self.compteur_reproduction += 1
        
        if self.compteur_reproduction == 3 : 
            print('parent :')
            print(self.coordonnees_x, self.coordonnees_y)
            bebe_requin_y = self.coordonnees_y
            bebe_requin_x = self.coordonnees_x
            while mon_monde.grille[bebe_requin_x][bebe_requin_y] != "🌊":
                bebe_requin_y -= 1
                if bebe_requin_y < 0 :
                    bebe_requin_y = rd.randint(0, mon_monde.column_number-1)
            print(bebe_requin_x, bebe_requin_y)
            mon_monde.grille[bebe_requin_x][bebe_requin_y] = "🦈"
            liste_bebe_requins.append(Requin(bebe_requin_x, bebe_requin_y))
            self.compteur_reproduction = 0
    
    def bebe_devient_grand(self):
        liste_requins.append(bebe_requin)
        
    
    def is_dead(self):
        if self.energie <1:
            print(f'le requin {self.coordonnees_x}, {self.coordonnees_y} doit mourir.')
            liste_requins_morts.append(Requin(self.coordonnees_x,self.coordonnees_y))
            mon_monde.grille[self.coordonnees_x][self.coordonnees_y] = "🌊"
    
    
            

            
            
    

        


liste_thons = []
liste_bebe_thons = []
liste_requins = []
liste_requins_morts = []
liste_bebe_requins = []
mon_monde = World(10,10,5,5)
mon_monde.empty_world()
mon_monde.fill_world()
mon_monde.display_world()
while len(liste_thons) > 0 and len(liste_requins) > 0 :
    print('------------------------')
    print('les thons se déplacent')
    for thon in liste_thons:
        thon.se_deplacer()
    mon_monde.display_world()
    print('------------------------')
    print('les thons se reproduisent')
    for thon in liste_thons:
        thon.se_reproduire()
    for bebe_thon in liste_bebe_thons:
        bebe_thon.bebe_devient_grand()
    liste_bebe_thons = []
    mon_monde.display_world()
    print('------------------------')
    print('les requins se déplacent')
    for requin in liste_requins:
        requin.se_deplacer()
    mon_monde.display_world()
    print('------------------------')
    print('les requins meurent')
    for requin in liste_requins:
        requin.is_dead()
    for requin in liste_requins_morts:
        if requin in liste_requins:
            liste_requins.remove(requin)
    liste_requins_morts = []
    mon_monde.display_world()
    print('------------------------')
    print('les requins se reproduisent')
    for requin in liste_requins:
        requin.se_reproduire()
    for bebe_requin in liste_bebe_requins:
        bebe_requin.bebe_devient_grand()
    liste_bebe_requins = []
    mon_monde.display_world()
