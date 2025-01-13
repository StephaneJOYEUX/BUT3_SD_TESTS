import pandas as pd
from Grille import Grille
from Navire import Navire, FactoryNavire
from ast import literal_eval

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
        self._navires : set = set()
        self._mode_jeu : str = ""
        self.save :pd.DataFrame = pd.DataFrame({
            "nom":[],
            "taille_grille_x":[],
            "taille_grille_y": [],
            "liste_navires": [],
            "nombre_navires": []
        })

        # construction des navires "classiques" présents dans les modes : "Normal" & "Blitz"
        self.cuirasse = FactoryNavire(nom="cuirassé", taille=4).get_navire()
        self.fregate = FactoryNavire(nom="frégate", taille=3).get_navire()
        self.sous_marin = FactoryNavire(nom="sous-marin", taille=3).get_navire()
        self.torpilleur = FactoryNavire(nom="torpilleur", taille=2).get_navire()
        self.porte_avions = FactoryNavire(nom="porte-avions", taille=5).get_navire()

    # Lecture du fichier de sauvegarde csv
    def lecture_sauvegarde(self):
        self.save = pd.read_csv('sauvegardes_mode_jeux.csv', encoding="UTF-8")

    # Ecriture dans le fichier csv
    def ecriture_sauvegarde(self):
        self.save.to_csv('sauvegardes_mode_jeux.csv', index = False, encoding="UTF-8")


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
                    print("Vous avez choisi : Personnalisé.")

                    choix_validation = 'n'
                    while not choix_validation == "o" :

                        liste_choix = self.choisir_mode_jeu_personnalise()
                        choix_mode_jeu_personnalise = liste_choix[0]
                        dict_navires = liste_choix[1]


                        # confirmation du choix du mode de jeu
                        choix_validation_valide = False
                        while not choix_validation_valide:
                            try :
                                choix_validation = input("\nConfirmez-vous le choix de ce mode de jeu ? (o/n)\n")
                                print("")
                                assert choix_validation == "o" or choix_validation == "n"
                                choix_validation_valide = True
                            except :
                                print("\nSaisie non valide ! Choisissez l'un des choix proposé !\n")

                        if choix_validation == "o":
                            # refaire la boucle de choix de strategie => passer par une fonction ?
                            self._grille = Grille(self.save["taille_grille_x"][choix_mode_jeu_personnalise], self.save["taille_grille_y"][choix_mode_jeu_personnalise])
                            for nom_navire, taille_navire in dict_navires.items() :
                                self._navires.add(FactoryNavire(nom=nom_navire, taille=taille_navire))
                            break


        elif choix_creation == "creer" :
            # input sur le nom du mode de jeu
            # assertion sur les noms des modes de jeu existant.
            self.ecriture_sauvegarde()


    def choisir_mode_jeu_personnalise(self):
        print("Pour obtenir plus d'information sur une stratégie, choississez la.")
        print(self.save[["nom", "taille_grille_x", "taille_grille_y", "nombre_navires"]])
        print("")

        choix_mode_jeu_personnalise_valide = False
        while not choix_mode_jeu_personnalise_valide:
            try:
                choix_mode_jeu_personnalise = int(input("Choisissez un mode de jeu parmis la liste proposée :\n"))
                assert (choix_mode_jeu_personnalise in set(self.save.index))
                choix_mode_jeu_personnalise_valide = True
            except:
                print("\nSaisie invalide !")
                print("Choississez un nombre correspondant à l'un des mode de jeu.\n")

        print(f"\nVous avez choisi le mode de jeu : {self.save["nom"][choix_mode_jeu_personnalise]}")
        print("Voici la liste des navires de ce mode de jeu :")

        dict_navires = literal_eval(self.save["liste_navires"][choix_mode_jeu_personnalise])
        # Conversion du dictionnaire en DataFrame
        df_navires = pd.DataFrame(list(dict_navires.items()), columns=['Navire', 'Taille'])
        print(df_navires)

        return [choix_mode_jeu_personnalise, dict_navires]

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

