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

    def __init__(self, nombre_lignes, nombre_colonnes):
        self.nb_lignes = nombre_lignes
        self.nb_colonnes = nombre_colonnes

        self.grille = []

        self.creation_grille_de_jeu()


    # Créer une grille de jeu:
    def creation_grille_de_jeu(self):
        self.grille = []
        for i in range(self.nb_lignes):
            self.grille.append([])
            for j in range(self.nb_colonnes):
                self.grille[i].append("-")
        return True



# Fonction d'affichage
def afficher_grille(grille) :
    reslt = ""
    for ligne in grille:
        reslt += ("".join(ligne))
        print(" ".join(ligne))
    print("")
    return reslt

def afficher_couple_grilles(grille1, grille2):
    print("     Vos navires :                      Champ de tir :")
    for index_ligne in range(len(grille1))  :
        print("     "+" ".join(grille1[index_ligne])+"                "+" ".join(grille2[index_ligne]))
    print("")
