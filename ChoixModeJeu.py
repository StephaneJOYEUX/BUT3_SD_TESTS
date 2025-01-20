import pandas as pd
from Grille import Grille, afficher_grille
from Navire import Navire, FactoryNavire
from ast import literal_eval
from CreationModeJeu import FactoryCreationModeJeu
from ModeJeu import ModeJeu
import os
import pandas as pd

class ChoixModeJeu() :
    # Getters
    def get_navires(self):
        return self._navires

    def get_grille(self):
        return self._grille

    def get_mode_jeu(self):
        return self._mode_jeu

    # Setters
    def set_mode_jeu(self, mode_jeu : ModeJeu):
        self._mode_jeu = mode_jeu

    def set_grille(self, grille : Grille):
        self._grille = grille

    def set_navires(self, navires : set):
        self._navires = navires

    # Constructeur
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
                    self._grille.create()
                    self._navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}
                case 2 :
                    print("Vous avez choisi le mode de jeu : Blitz.\n")
                    self._mode_jeu = "Blitz"
                    self._grille = Grille(5,5)
                    self._grille.create()
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
                            self._grille.create()
                            for nom_navire, taille_navire in dict_navires.items() :
                                self._navires.add(FactoryNavire(nom=nom_navire, taille=taille_navire))
                            break


        elif choix_creation == "creer" :
            # input sur le nom du mode de jeu
            # assertion sur les noms des modes de jeu existant.
            choix_nom_valide = False
            while not choix_nom_valide :
                try :
                    choix_nom = input("Choisissez un nom pour ce mode de jeu :\n")
                    assert choix_nom not in (set(self.save["nom"]))
                    choix_nom_valide = True
                except :
                    print("\nSaisie non-valide !")
                    print("Le nom que vous avez choisi existe déjà.\n")

            # Faire appel ensuite a la classe CreationModeJeu et au Setters.
            creation_mode_jeu = FactoryCreationModeJeu(choix_nom).get_creation_mode_jeu()
            self.set_mode_jeu(creation_mode_jeu.get_mode_jeu())
            self.set_navires(creation_mode_jeu.get_navires())
            self.set_grille(creation_mode_jeu.get_grille())

        # présentation du mode de jeu créé :
        os.system('cls')
        print("Voici le mode de jeu créé :")
        print(f"La grille fait : {self.get_grille().get_nb_lignes()}x{self.get_grille().get_nb_colonnes()}")
        afficher_grille(self.get_grille().get_plateau())
        print(f"\nDans ce mode de jeu, il y a {len(self.get_navires())} navires.")
        print("Voici les navires de ce mode de jeu :")
        # Afficher un df pandas présentant les différents navires.
        self.afficher_navires(self.get_navires())

        input("Tapez 'entrer' pour continuer  \n")
        os.system('cls')


    # Methode de classe utilisé dans le main si le choix est 'choisir'
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


    # objectif de la méthode de classe :
    # afficher un df.pandas à partir d'un set d'instance de la classe 'Navire'
    def afficher_navires(self, navires : set):
        list_noms = []
        list_symboles = []
        list_tailles = []

        for navire in navires :
            list_noms.append(navire.get_nom())
            list_symboles.append(navire.get_symbole())
            list_tailles.append(navire.get_taille())

        df = pd.DataFrame({"noms" : list_noms, "symboles" : list_symboles, 'tailles' : list_tailles})
        print(df)


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

