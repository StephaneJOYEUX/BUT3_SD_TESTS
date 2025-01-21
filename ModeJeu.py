import os

from Grille import Grille


class ModeJeu():
    # Getters
    def get_nom(self):
        return self._nom

    def get_navires(self):
        return self._navires

    def get_taille_grille(self):
        return self._taille_grille

    def get_nb_navires(self):
        return len(self._navires)

    # Setters
    def set_nom(self, nom=None):
        if nom is None:
            nom = self.nom
        if len(nom) > 20:
            raise ValueError("Nom du mode de jeu trop long !")
        elif len(nom) < 2:
            raise ValueError("Nom du mode de jeu trop court !")
        else:
            self._nom = nom

    def set_navires(self, navires : set = None):
        if navires is None:
            navires = self.navires

        # appel de la méthode de vérification de la conformité de l'ensemble de navires par rapport à la grille.
        self._navires = navires

    def set_taille_grille(self, taille_grille=None):
        if taille_grille is None:
            taille_grille = self.taille_grille

        # on vérifie que le mode de jeu peut être créé => taille de la grille valide
        try:
            self.grille = Grille(taille_grille[0], taille_grille[1])
            self.grille.create()
        except:
            raise ValueError('La taille de la grille est invalide !')

        self._taille_grille = taille_grille

    # Constructeur
    def __init__(self, nom: str, navires: set, taille_grille: list[int]):
        self._nom = None
        self._navires = None
        self._taille_grille = None

        self.nom = nom
        self.navires = navires
        self.taille_grille = taille_grille

    # Cette méthode de classe permet de vérifier que l'ensemble de navire fourni en paramètre respecte bien
    # les contraintes liées à la taille de la grille.
    # Elle est appelée par le self.set_navires()
    def verifier_validiter_navires(self, navires: set = None, taille_grille: list = None):
        # definir ici les critères de conformité d''un mode de jeu.
        if navires is None:
            navires = self.get_navires()

        if taille_grille is None:
            taille_grille = self.get_taille_grille()

        numero_critere = 0

        # Critère n°1 :
        # Limiter artificiellement et individuellement la taille des navires
        # max(taille_navires) < max(taille_grille)
        for navire in navires:
            if navire.get_taille() >= min(taille_grille):
                os.system('cls')
                print("\nCritère de validité non respecté !")
                print("Strategie invalide !")
                print(
                    "La longueur des navires ne peut pas être supérieure ou égale au nombre minimum de ligne/colonne.\n")
                numero_critere = 1
                return [False, numero_critere]

        # Critère n°2 :
        # Eviter un remplissage trop important de la grille tout en evitant des potentiels problemes de placement
        # sum(taille_navires)/(nb_lignes*nb_colonnes) <= 0.6
        somme = 0
        for navire in navires:
            somme += navire.get_taille()
        if somme / (taille_grille[0] * taille_grille[1]) > 0.6:
            os.system('cls')
            print("\nCritère de validité non respecté !")
            print(
                "Le nombre de cases occupées par vos navires est trop important par rapport à la taille de la grille.")
            print("Cela peut être causé par un nombre trop important de navires trop grand.\n")
            print("Vous devez modifier les caractéristiques de l'ensemble de vos navires.")
            numero_critere = 2
            return [False, numero_critere]

        return [True, numero_critere]


class FactoryModeJeu():
    def get_mode_jeu(self):
        return self.mode_jeu

    def __init__(self, nom: str, navires: set, taille_grille: list[int]):
        self.mode_jeu = ModeJeu(nom=nom, navires=navires, taille_grille=taille_grille)
        self.mode_jeu.set_nom()
        self.mode_jeu.set_navires()
        self.mode_jeu.set_taille_grille()
