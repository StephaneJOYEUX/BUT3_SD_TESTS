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

    def get_plateau(self)-> list:
        return self.plateau


    # Setters
    def set_nb_lignes(self, nb_lignes:int):
        if nb_lignes < self.taille_min :
            self.__nb_lignes = None
            raise ValueError(f"Le nombre de lignes minimum est {self.taille_min} !")
        elif nb_lignes > self.taille_max :
            self.__nb_lignes = None
            raise ValueError(f"Le nombre de lignes maximum est {self.taille_max} !")
        else :
            self.__nb_lignes = nb_lignes

    def set_nb_colonnes(self, nb_colonnes:int):
        if nb_colonnes < self.taille_min:
            self.__nb_colonnes = None
            raise ValueError(f"Le nombre de colonnes minimum est {self.taille_min} !")
        elif nb_colonnes > self.taille_max:
            self.__nb_colonnes = None
            raise ValueError(f"Le nombre de colonnes maximum est {self.taille_max} !")
        else:
            self.__nb_colonnes = nb_colonnes


    # Constructeur
    def __init__(self, nombre_lignes, nombre_colonnes):
        self.taille_min : int = 2
        self.taille_max : int = 20
        self.nombre_colonnes = nombre_colonnes
        self.nombre_lignes = nombre_lignes

        self.plateau = []



    # Créer une grille de jeu:
    def create(self):
        # verifications de la validite du nb de lignes et de colonnes
        observateur = 0
        # Condition sur les lignes
        try :
            self.set_nb_lignes(nb_lignes=self.nombre_lignes)
        except :
            observateur = 1
        # Condition sur les colonnes
        try :
            self.set_nb_colonnes(nb_colonnes=self.nombre_colonnes)
        except :
            observateur = 1
        # Return False si l'une des valeurs est non-conforme.
        if observateur == 1 :
            raise ValueError("Impossible de créer la grille !")

        self.plateau = []
        for i in range(self.__nb_lignes):
            self.plateau.append([])
            for j in range(self.__nb_colonnes):
                self.plateau[i].append("-")
        return True



# Fonction d'affichage
def afficher_grille(grille) :
    result = ""
    for ligne in grille:
        result += " ".join(ligne)+"\n"
        print(" ".join(ligne))
    return result


def afficher_couple_grilles(plateau1, plateau2):
    if len(plateau1) != len(plateau2) or len(plateau1[0]) != len(plateau2[0]) :
        raise ValueError("Les deux grilles sont de tailles différentes !")
    result = ""
    result += "     Vos navires :                      Champ de tir :\n"
    for index_ligne in range(len(plateau1))  :
        result += "     "+" ".join(plateau1[index_ligne])+"                "+" ".join(plateau2[index_ligne])+"\n"
    print(result)
    return(result)
