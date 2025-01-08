class ChoixModeJeu() :
    # Getters
    def get_nom(self):
        return self._nom

    def get_navire(self):
        return self._navires

    def get_taille_grille(self):
        return self._taille_grille


    # Setters
    def set_nom(self, nom = None):
        if nom == None :
            nom = self.nom
        self._nom = nom


    def set_navires(self, navires = None):
        if navires == None :
            navires = self.navires
        self._navires = navires

    def set_taille_grille(self, taille_grille = None):
        if taille_grille == None :
            taille_grille = self.taille_grille
        self._taille_grille = taille_grille


    def __init__(self):
        self._nom : str
        self._navires :set
        self._taille_grille : list[int]



    def lecture_sauvegarde(self):
        pass

    def ecriture_sauvegarde(self):
        pass

    def main(self):
        choix_valide = False

        while not choix_valide :
            print("Choississez le mode de jeu : 1.Normal / 2.Blitz / 3.Personnalisé")
            try :
                choix_utilisateur = int(input("Entrez 1,2 ou 3\n"))
                assert choix_utilisateur == 1 or choix_utilisateur == 2 or choix_utilisateur == 3
                choix_valide = True
            except :
                print("Mauvaise saisie !")
                print("Entrez un nombre figurant parmis les choix proposés.")


class FactoryChoixModeJeu() :
    def __init__(self):
        self.choix_mode_jeu = ChoixModeJeu()
        self.choix_mode_jeu.lecture_sauvegarde()
        self.choix_mode_jeu.main()
        self.choix_mode_jeu.ecriture_sauvegarde()


test = FactoryChoixModeJeu()