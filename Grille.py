"""
La classe Grille est appelée par à peu près toutes les classes du jeu,
autant pour l'initialisation de la partie que pour la partie elle-même.

Cette classe définie les attributs d'une grille de jeu et des méthode qui lui sont propres.

Elle prend en input :
    - nombre_lignes : le nombre de ligne de la grille
    - nombre_colonnes : le nombre de colonne de la grille

Il faut retenir qu'une grille de jeu est une matrice (= liste de liste).
Le nombre_lignes défini la longueur de la liste principale.
Le nombre_colonnes défini la longueur des listes secondaires.

Cette classe contient aussi deux méthodes d'affichage très utile notamment
pour la classe BatailleNavale() et pour la classe ChoixStrategie().
"""


class Grille():
    
    #Variables privées
    __nb_lignes = 0
    __nb_colonnes = 0
    
    # Getter :
    def getNbLignes(self):
        return self.__nb_lignes
    
    def getNbColonnes(self):
        return self.__nb_colonnes
    
    def setNbLignes(self, nb_lignes : int):
        if ((nb_lignes < 2 and self.__nb_colonnes == 1) or (self.__nb_colonnes < 2 and nb_lignes == 1) or (nb_lignes < 1 and self.__nb_colonnes < 1)):
            raise ValueError('Votre grille ne respecte pas les normes')
        else:
            self.__nb_lignes = nb_lignes
        
    def setNbColonnes(self, nb_colonnes : int):
        if ((self.__nb_lignes < 2 and nb_colonnes == 1) or (nb_colonnes < 2 and self.__nb_lignes == 1) or (self.__nb_lignes < 1 and nb_colonnes < 1)):
            raise ValueError('Votre grille ne respecte pas les normes')
        else:
            self.__nb_colonnes = nb_colonnes

    def __init__(self, nombre_lignes, nombre_colonnes):
        self.__nb_lignes = nombre_lignes
        self.__nb_colonnes = nombre_colonnes

        self.plateau = []


    # Créer une grille de jeu:
    def creation_grille(self):
        try:
            self.setNbLignes(self.__nb_lignes)
            self.setNbColonnes(self.__nb_colonnes)
        except:
            #raise ValueError('Votre grille ne respecte pas les normes')
            return False

        self.plateau = []
        #if self.getNbColonnes() >= 10 and self.getNbLignes() >= 10:
        for i in range(self.getNbLignes()):
            self.plateau.append([])
            for j in range(self.getNbColonnes()):
                self.plateau[i].append("-")
        return True
        #else:
            #raise ValueError('Votre grille doit avoir au moins 10 lignes et 10 colonnes')
            #return False



# Fonction d'affichage
def afficher_grille(plateau) :
    result = ""
    for ligne in plateau:
        result += " ".join(ligne) + "\n"
        print(" ".join(ligne))
    return result

def afficher_couple_grilles(grille1, grille2):
    result = "     Vos navires :                      Champ de tir :\n"
    print("     Vos navires :                      Champ de tir :")
    for index_ligne in range(len(grille1))  :
        result += "     "+" ".join(grille1[index_ligne])+"                "+" ".join(grille2[index_ligne]) + "\n"
        print("     "+" ".join(grille1[index_ligne])+"                "+" ".join(grille2[index_ligne]))
    return result