"""
La classe Navire permet d'instancier des objet 'navires' utilisé dans la partie.
Ils servent de cible aux différents joueurs, et sont placé sur le plateau à chaque partie.

Inputs :
    - nom : Le nom du navire.
    - taille : La taille du navire.
    - symbole : Le symbole d'un navire est une Lettre, qui sera affichée dans la grille lors de l'affichage.
                C'est un parametre optionnel, car le symbole est généralement défini à partir du nom.
                Il existe des cas particulier ou l'utilisateur peut choisir de definir le symbole d'un navire manuellement.

Cette classe n'a pas de méthode de classe particulière en plus des setters et getters.
"""


class Navire():
    # Getter
    def get_nom(self):
        return self._nom

    def get_symbole(self):
        return self._symbole

    def get_taille(self):
        return self._taille

    # Setter
    def set_nom(self, nom=None):
        # cas d'initialisation
        if nom is None:
            nom = self.nom

        # choix arbitraire de la longueur de la chaine de caractère (3).
        if len(nom) <= 3:
            raise ValueError("Le nom de ce navire est invalide - trop court.")
        elif len(nom) > 20:
            raise ValueError("Le nom de ce navire est invalide - trop long.")
        else:
            self._nom = nom

    def set_symbole(self, symbole=None):
        # cas d'initialisation
        if symbole is None:
            symbole = self.symbole

        # verification criteres symbole correct :
        #   - longueur == 1
        #   - est une lettre majuscule.
        if len(symbole) != 1 or not symbole.isalpha():
            self._symbole = None
            raise ValueError("Le symbole est invalide !")

        symbole = symbole.upper()
        self._symbole = symbole

    def set_taille(self, taille=None):
        if taille is None:
            taille = self.taille

        # choix arbitraire d'une taille minimale égale à 1 et maximale égale à 9.
        if taille < 2:
            raise ValueError("Taille non valide ! Elle doit être supérieure ou égale à 2 !")
        elif taille > 9:
            raise ValueError("Taille non valide ! Elle doit être inférieur à 10 !")
        else:
            self._taille = self.taille

    def __init__(self, nom: str, taille: int, symbole: str = None):
        self.nom = nom.lower()
        self.taille = taille
        if symbole is None:
            self.symbole = self.nom[0].upper()
        else:
            self.symbole = symbole

    # Les méthode __eq__ et __hash__ se doivent d'être définie car
    # les instances de Navires sont utlisées dans des sets et sont utilisées dans des tests d'égalité.
    def __eq__(self, other):
        try:
            if self.nom == other.nom and self.taille == other.taille:
                return True
            return False
        except:
            print("Vous ne comparez pas 2 instances de la classe Navire")

    def __hash__(self):
        return hash((self.nom, self.taille))


class FactoryNavire():
    def __init__(self, nom: str, taille: int, symbole: str = None):
        self.navire = Navire(nom, taille, symbole)
        self.navire.set_nom()
        self.navire.set_taille()
        self.navire.set_symbole()

    def get_navire(self):
        return self.navire
