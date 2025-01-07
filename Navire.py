class Navire():
    # Getter
    def get_nom(self):
        return self._nom

    def get_symbole(self):
        return self._symbole

    def get_taille(self):
        return self._taille

    # Setter
    def set_nom(self, nom):
        # choix arbitraire de la longueur de la chaine de caractère (3).
        if len(nom) > 3:
            self._nom = nom
        else:
            raise ValueError("Le nom de ce navire est invalide - trop court.")

    def set_symbole(self, symbole):
        self._symbole = symbole

    def set_taille(self, taille):
        if taille > 1:
            self._taille = taille
        else:
            raise ValueError("Taille non valide ! Elle doit être supérieure à 2 !")

    def __init__(self, nom: str, taille: int):
        self.nom = nom.lower()
        self.taille = taille
        self.symbole = self.nom[0].upper()
        print(self.nom)
        print(self.symbole)


cuirassé = Navire(nom="cuirassé", taille=2)