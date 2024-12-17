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
    # Variables privées
    __nb_lignes = 0
    __nb_colonnes = 0

    # Getters
    def get_nb_lignes(self):
        return self.__nb_lignes

    def get_nb_colonne(self):
        return self.__nb_colonnes


    # Setters
    def set_nb_lignes(self, nb_lignes:int):
        if nb_lignes >= 10 :
            self.__nb_lignes = nb_lignes
        else :
            raise ValueError("Le nombre de lignes minimum est 10 !")

    def set_nb_colonnes(self, nb_colonnes:int):
        self.__nb_colonnes = nb_colonnes


    # Constructeur
    def __init__(self, nombre_lignes, nombre_colonnes):
        self.set_nb_lignes(nb_lignes=nombre_lignes)
        self.set_nb_colonnes(nb_colonnes=nombre_colonnes)

        self.grille = []

        self.creation_grille_de_jeu()


    # Créer une grille de jeu:
    def creation_grille_de_jeu(self):
        self.grille = []
        for i in range(self.__nb_lignes):
            self.grille.append([])
            for j in range(self.__nb_colonnes):
                self.grille[i].append("-")
        return True



# Fonction d'affichage
def afficher_grille(grille) :
    result = ""
    for ligne in grille:
        result += " ".join(ligne)+"\n"
        print(" ".join(ligne))
    #result+= "\n"
    return result

def afficher_couple_grilles(grille1, grille2):
    result = ""
    result += "     Vos navires :                      Champ de tir :\n"
    for index_ligne in range(len(grille1))  :
        result += "     "+" ".join(grille1[index_ligne])+"                "+" ".join(grille2[index_ligne])+"\n"
    #result += "\n"
    print(result)
    return(result)
