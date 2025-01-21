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

    # Constructeur
    def __init__(self, nombre_lignes, nombre_colonnes):
        self.__nb_lignes = nombre_lignes
        self.__nb_colonnes = nombre_colonnes
        self.grille = []
        
        
        
        
    # Getters
    def get_nb_lignes(self):
        return self.__nb_lignes

    def get_nb_colonne(self):
        return self.__nb_colonnes


    # Setters
    def set_nb_lignes(self, nb_lignes:int):
        if nb_lignes >= 2 :
            self.__nb_lignes = nb_lignes
        else :
            raise ValueError("Le nombre de lignes minimum est 2 !")

    def set_nb_colonnes(self, nb_colonnes:int):
        if nb_colonnes >=2 :
            self.__nb_colonnes = nb_colonnes
        else :
            raise ValueError("Le nombre minimum de colonne est 2 !")


    def creation_grille_de_jeu(self):
        try: 
            self.set_nb_lignes(self.__nb_lignes)
            self.set_nb_colonnes(self.__nb_colonnes)
        except ValueError:
            raise ValueError("Les valeurs saisies sont trop petites, veuillez saisir de nouvelles valeurs.")
        
        self.grille = []  
        for i in range(self.__nb_lignes):
            ligne = []
            for j in range(self.__nb_colonnes):
                ligne.append("-")
            self.grille.append(ligne) 
        return True



# Fonction d'affichage
def afficher_grille(grille) :
    result = ""
    for ligne in grille:
        result += " ".join(ligne)+"\n"
        print(" ".join(ligne))
    return result

def afficher_couple_grilles(grille1, grille2):
    result = "     Vos navires :                      Champ de tir :\n"
    print("     Vos navires :                      Champ de tir :")
    for index_ligne in range(len(grille1))  :
        result += "     "+" ".join(grille1[index_ligne])+"                "+" ".join(grille2[index_ligne]) + "\n"
        print("     "+" ".join(grille1[index_ligne])+"                "+" ".join(grille2[index_ligne]))
    return result
