from Grille import Grille
from Navire import Navire, FactoryNavire

class ChoixModeJeu() :
    # Getters
    def get_navires(self):
        return self._navires

    def get_grille(self):
        return self._grille

    def get_mode_jeu(self):
        return self._mode_jeu


    def __init__(self):
        self._grille : Grille
        self._navires : Navire
        self._mode_jeu : str

        # construction des navires "classiques" présents dans les modes : "Normal" & "Blitz"
        self.cuirasse = FactoryNavire(nom="cuirassé", taille=4).get_navire()
        self.fregate = FactoryNavire(nom="frégate", taille=3).get_navire()
        self.sous_marin = FactoryNavire(nom="sous-marin", taille=3).get_navire()
        self.torpilleur = FactoryNavire(nom="torpilleur", taille=2).get_navire()
        self.porte_avions = FactoryNavire(nom="porte-avions", taille=5).get_navire()

    # Lecture du fichier de sauvegarde csv
    def lecture_sauvegarde(self):
        pass

    # Ecriture dans le fichier csv
    def ecriture_sauvegarde(self):
        pass

    def main(self):
        choix_creation_valide = False

        while not choix_creation_valide:
            try:
                choix_creation = input("Choississez si vous souhaitez choisir un mode de jeu existant ou en créer un nouveau. (choisir/creer)\n")
                assert choix_creation == "choisir" or choix_creation == "creer"
                choix_creation_valide = True
            except:
                print("Mauvaise saisie !")
                print("Entrez l'un des choix proposés.")


        if choix_creation == "choisir" :
            choix_mode_jeu_valide = False

            while not choix_mode_jeu_valide:
                print("\nChoississez le mode de jeu : 1.Normal / 2.Blitz / 3.Personnalisé")
                try:
                    choix_mode_jeu = int(input("Entrez 1,2 ou 3\n"))
                    assert choix_mode_jeu == 1 or choix_mode_jeu == 2 or choix_mode_jeu == 3
                    choix_mode_jeu_valide = True
                except:
                    print("Mauvaise saisie !")
                    print("Entrez un nombre figurant parmis les choix proposés.")

            match choix_mode_jeu :
                case 1 :
                    print("Vous avez choisi le mode de jeu : Normal.\n")
                    self._mode_jeu = "Normal"
                    self._grille = Grille(10,10)
                    self._navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}
                case 2 :
                    print("Vous avez choisi le mode de jeu : Blitz.\n")
                    self._mode_jeu = "Blitz"
                    self._grille = Grille(5,5)
                    self._navires = {self.cuirasse, self.sous_marin, self.torpilleur}
                case 3 :
                    print("vous avez choisi 3")

        elif choix_creation == "creer" :
            pass

class FactoryChoixModeJeu() :
    # Getters
    def get_navires(self):
        return self.choix_mode_jeu.get_navires()

    def get_grille(self):
        return self.choix_mode_jeu.get_grille()

    def get_mode_jeu(self):
        return self.choix_mode_jeu.get_mode_jeu()

    def __init__(self):
        self.choix_mode_jeu = ChoixModeJeu()
        self.choix_mode_jeu.lecture_sauvegarde()
        self.choix_mode_jeu.main()
        self.choix_mode_jeu.ecriture_sauvegarde()

