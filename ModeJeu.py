from Grille import Grille

class ModeJeu():
    # Getters
    def get_nom(self):
        return self._nom

    def get_navire(self):
        return self._navires

    def get_taille_grille(self):
        return self._taille_grille

    def get_nb_navires(self):
        return len(self._navires)

    # Setters
    def set_nom(self, nom=None):
        if nom == None:
            nom = self.nom
        if len(nom) > 20:
            raise ValueError("Nom du mode de jeu trop long !")
        elif len(nom) < 2:
            raise ValueError("Nom du mode de jeu trop court !")
        else:
            self._nom = nom

    def set_navires(self, navires=None):
        if navires == None:
            navires = self.navires

        # appel de la méthode de vérification de la conformité de l'ensemble de navires par rapport à la grille.
        self.verifier_validiter_navires()
        self._navires = navires

    def set_taille_grille(self, taille_grille=None):
        if taille_grille == None:
            taille_grille = self.taille_grille

        # on vérifie que le mode de jeu peut être créé => taille de la grille valide
        try:
            self.grille = Grille(taille_grille[0], taille_grille[1])
            self.grille.create()
        except:
            raise ValueError('La taille de la grille est invalide !')

        self._taille_grille = taille_grille


    # Constructeur
    def __init__(self, nom :str, navires : set, taille_grille :list[int]):
        self._nom = None
        self._navires = None
        self._taille_grille = None

        self.nom = nom
        self.navires = navires
        self.taille_grille = taille_grille


    # Cette méthode de classe permet de vérifier que l'ensemble de navire fourni en paramètre respecte bien
    # les contraintes liées à la taille de la grille.
    # Elle est appelée par le self.set_navires()
    def verifier_validiter_navires(self) -> bool:
        # definir ici les critère de conformité.
        return True





class FactoryModeJeu():
    def get_mode_jeu(self):
        return self.mode_jeu

    def __init__(self, nom :str, navires : set, taille_grille :list[int]):
        self.mode_jeu = ModeJeu(nom=nom, navires=navires, taille_grille=taille_grille)
        self.mode_jeu.set_nom()
        self.mode_jeu.set_navires()
        self.mode_jeu.set_taille_grille()