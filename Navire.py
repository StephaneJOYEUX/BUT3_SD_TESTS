class Navire():
    # Getter
    def get_nom(self):
        return self._nom

    def get_symbole(self):
        return self._symbole

    def get_taille(self):
        return self._taille

    # Setter
    def set_nom(self, nom = None):
        # cas d'initialisation
        if nom == None :
            nom = self.nom

        # choix arbitraire de la longueur de la chaine de caractère (3).
        if len(nom) <= 3:
            raise ValueError("Le nom de ce navire est invalide - trop court.")
        elif len(nom) > 20 :
            raise ValueError("Le nom de ce navire est invalide - trop long.")
        else:
            self._nom = nom


    def set_symbole(self, symbole = None):
        # cas d'initialisation
        if symbole == None :
            symbole = self.symbole

        self._symbole = symbole

    def set_taille(self, taille = None):
        if taille == None :
            taille = self.taille

        # choix arbitraire d'une taille minimale égale à 1.
        if taille < 2:
            raise ValueError("Taille non valide ! Elle doit être supérieure à 2 !")
        elif taille > 9 :
            raise ValueError("Taille non valide ! Elle doit être inférieur à 10 !")
        else:
            self._taille = self.taille


    def __init__(self, nom: str, taille: int):
        self.nom = nom.lower()
        self.taille = taille
        self.symbole = self.nom[0].upper()
        # Affichage utile pour tester simplement (a supprimer quand le module de tests sera prêt).


class FactoryNavire():
    def __init__(self, nom: str, taille: int):
        self.navire = Navire(nom, taille)
        self.navire.set_nom()
        self.navire.set_taille()
        self.navire.set_symbole()

cuirassé = Navire(nom="cuirassé", taille=2)