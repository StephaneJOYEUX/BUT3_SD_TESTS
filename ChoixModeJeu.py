import pandas as pd
from Grille import Grille, afficher_grille
from Navire import Navire, FactoryNavire
from ast import literal_eval
from CreationModeJeu import FactoryCreationModeJeu
from ModeJeu import ModeJeu, FactoryModeJeu
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
        self._mode_jeu : ModeJeu
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

        choix_confirmation_valide = False
        while not choix_confirmation_valide:
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

                # lisibilité pour le joueur.
                print("")
                match choix_mode_jeu :
                    case 1 :
                        # grille
                        grille = Grille(10,10)
                        grille.create()
                        self.set_grille(grille)

                        # navires
                        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}
                        self.set_navires(navires)

                        # mode_jeu
                        nom_mode_jeu = "Normal"
                        mode_jeu = FactoryModeJeu(nom=nom_mode_jeu,
                                                  navires=self.get_navires(),
                                                  taille_grille=[self.get_grille().get_nb_lignes(),
                                                                 self.get_grille().get_nb_colonnes()]
                                                  ).get_mode_jeu()
                        self.set_mode_jeu(mode_jeu)

                    case 2 :
                        # grille
                        grille = Grille(5, 5)
                        grille.create()
                        self.set_grille(grille)

                        # navires
                        navires = {self.cuirasse, self.sous_marin, self.torpilleur}
                        self.set_navires(navires)

                        # mode_jeu
                        nom_mode_jeu = "Blitz"
                        mode_jeu = FactoryModeJeu(nom=nom_mode_jeu,
                                                  navires=self.get_navires(),
                                                  taille_grille=[self.get_grille().get_nb_lignes(),
                                                                 self.get_grille().get_nb_colonnes()]
                                                  ).get_mode_jeu()
                        self.set_mode_jeu(mode_jeu)
                    case 3 :
                        print("Vous avez choisi : Personnalisé.")

                        liste_choix = self.choisir_mode_jeu_personnalise()
                        choix_mode_jeu_personnalise = liste_choix[0]
                        nom_mode_jeu = liste_choix[1]
                        dict_navires = liste_choix[2]

                        # grille
                        grille = Grille(self.save["taille_grille_x"][choix_mode_jeu_personnalise],
                                              self.save["taille_grille_y"][choix_mode_jeu_personnalise])
                        grille.create()
                        self.set_grille(grille)

                        # navires
                        navires = set()
                        for nom_navire, taille_navire in dict_navires.items():
                            navires.add(FactoryNavire(nom=nom_navire, taille=taille_navire).get_navire())
                        self.set_navires(navires)

                        # mode_jeu
                        mode_jeu = FactoryModeJeu(nom=nom_mode_jeu,
                                                  navires=self.get_navires(),
                                                  taille_grille=[self.get_grille().get_nb_lignes(),
                                                                 self.get_grille().get_nb_colonnes()]
                                                  ).get_mode_jeu()
                        self.set_mode_jeu(mode_jeu)




            elif choix_creation == "creer" :
                # input sur le nom du mode de jeu
                # assertion sur les noms des modes de jeu existant.
                choix_nom_valide = False
                while not choix_nom_valide :
                    try :
                        choix_nom = input("\nChoisissez un nom pour ce mode de jeu :\n")
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


                choix_enregistrement_valide = False

                while not choix_enregistrement_valide :
                    choix_enregistrement = input("Voulez vous enrigistrer le mode de jeu créé ? (o/n)\n")
                    try :
                        assert choix_enregistrement == 'o' or choix_enregistrement == 'n'
                        choix_enregistrement_valide = True
                    except :
                        print("Saisie invalide !")

                if choix_enregistrement == 'o' :
                    liste_navires = {}
                    for navire in self._navires :
                        liste_navires[navire.get_nom()] = navire.get_taille()

                    # enregistrement du mode de jeu :
                    new_data = [self.get_mode_jeu().get_nom(), self.get_mode_jeu().get_taille_grille()[0], self.get_mode_jeu().get_taille_grille()[1], liste_navires, self.get_mode_jeu().get_nb_navires() ]
                    self.save.loc[len(self.save)] = new_data


            # présentation du mode de jeu créé :
            os.system('cls')
            print(f"Vous avez choisi le mode de jeu : {self.get_mode_jeu().get_nom()}")
            print(f"La grille fait : {self.get_grille().get_nb_lignes()}x{self.get_grille().get_nb_colonnes()}")
            afficher_grille(self.get_grille().get_plateau())
            print(f"\nDans ce mode de jeu, il y a {len(self.get_navires())} navires :\n")
            # Afficher un df pandas présentant les différents navires.
            self.afficher_navires(self.get_navires())

            # confirmation du choix du mode de jeu
            try:
                choix_confirmation = input("\nConfirmez-vous le choix de ce mode de jeu ? (o/n)\n")
                print("")
                assert choix_confirmation == "o" or choix_confirmation == "n"
                if choix_confirmation == 'o' :
                    choix_confirmation_valide = True
            except:
                print("\nSaisie non valide ! Choisissez l'un des choix proposé !\n")

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


        nom_mode_jeu = self.save["nom"][choix_mode_jeu_personnalise]
        dict_navires = literal_eval(self.save["liste_navires"][choix_mode_jeu_personnalise])

        return [choix_mode_jeu_personnalise, nom_mode_jeu, dict_navires]


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

