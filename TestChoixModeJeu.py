from copy import deepcopy
from unittest import TestCase
from ChoixModeJeu import ChoixModeJeu
from Navire import FactoryNavire
from ModeJeu import FactoryModeJeu
from Grille import Grille
import numpy as np
import pandas as pd


class TestChoixModeJeu(TestCase):
    def setUp(self):
        # navires
        self.cuirasse = FactoryNavire(nom="cuirassé", taille=4).get_navire()
        self.fregate = FactoryNavire(nom="frégate", taille=3).get_navire()
        self.sous_marin = FactoryNavire(nom="sous-marin", taille=3).get_navire()
        self.torpilleur = FactoryNavire(nom="torpilleur", taille=2).get_navire()
        self.porte_avions = FactoryNavire(nom="porte-avions", taille=5).get_navire()

        self.navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        # grille
        self.grille = Grille(10, 10)
        self.grille.create()
        self.taille_grille = [self.grille.get_nb_lignes(), self.grille.get_nb_colonnes()]

        # mode_jeu
        self.mode_jeu = FactoryModeJeu(nom="Normal", navires=self.navires,
                                       taille_grille=self.taille_grille).get_mode_jeu()

    ## Setters & Getters
    # navires
    def test_set_get_navires_cas_nominal(self):
        self.choix_mode_jeu = ChoixModeJeu()
        self.choix_mode_jeu.set_navires(self.navires)

        self.assertEqual(self.navires, self.choix_mode_jeu.get_navires())

    # grille
    # il n'existe pas de cas où la grille est de taille incorrecte car l'instance de Grille est déjà créée
    # => les tests sur la taille sont déjà effectué.
    def test_set_get_grille_cas_nominal(self):
        self.choix_mode_jeu = ChoixModeJeu()
        self.choix_mode_jeu.set_grille(self.grille)

        self.assertEqual(self.grille, self.choix_mode_jeu.get_grille())

    # mode_jeu
    def test_set_get_mode_jeu_cas_nominal(self):
        self.choix_mode_jeu = ChoixModeJeu()
        self.choix_mode_jeu.set_mode_jeu(self.mode_jeu)

        self.assertEqual(self.mode_jeu, self.choix_mode_jeu.get_mode_jeu())

    # attributes
    def test_set_attributes_cas_nominal(self):
        self.choix_mode_jeu = ChoixModeJeu()
        self.choix_mode_jeu.set_attributes(nb_lignes=self.taille_grille[0], nb_colonnes=self.taille_grille[1],
                                           navires=self.navires, nom_mode_jeu="Normal")

        self.assertEqual(self.grille, self.choix_mode_jeu.get_grille())
        self.assertEqual(self.navires, self.choix_mode_jeu.get_navires())
        self.assertEqual(self.mode_jeu, self.choix_mode_jeu.get_mode_jeu())

    def test_set_attributes_cas_incorrect(self):
        self.choix_mode_jeu = ChoixModeJeu()
        taille_grille_test = [1, 1]
        try:
            self.choix_mode_jeu.set_attributes(nb_lignes=taille_grille_test[0], nb_colonnes=taille_grille_test[1],
                                               navires=self.navires, nom_mode_jeu="Normal")
        except ValueError as current_error:
            self.assertEqual("Impossible de créer la grille !", str(current_error)[0:31])

    # save
    def test_get_save_cas_nominal(self):
        self.choix_mode_jeu = ChoixModeJeu()
        # test sur les entêtes
        self.assertEqual(['nom', 'taille_grille_x', 'taille_grille_y', 'liste_navires', 'nombre_navires'],
                         list(self.choix_mode_jeu.get_save().columns))

    ## Methodes de classes
    # lecture fichier sauvegarde
    def test_lecture_sauvegarde(self):
        self.choix_mode_jeu = ChoixModeJeu()
        self.choix_mode_jeu.lecture_sauvegarde()

        # test sur le mode de jeu 'Normal' enregistré en 1er.
        self.assertEqual(['Normal', np.int64(10), np.int64(10),
                          "{'torpilleur': 2, 'sous-marin': 3, 'frégate': 3, 'cuirassé': 4, 'porte-avion': 5}",
                          np.int64(5)],
                         list(self.choix_mode_jeu.get_save().loc[0]))

    # ecriture fichier sauvegarde
    def test_ecriture_sauvegarde(self):
        # initialisation
        self.choix_mode_jeu = ChoixModeJeu()
        self.choix_mode_jeu.lecture_sauvegarde()

        # afin de tester la fonction d'ecriture :
        # recuperer le contenu du fichier de sauvegarde, le stocker dans une variable locale.
        # ajouter une nouvelle strategie, puis tester l'ecriture en verifiant avec la lecture que la ligne a bien ete ecrite.
        # réécrire la sauvegarde en enlevant la ligne artificielle ajoutee pour le test.

        # recuperation de la sauvegarde :
        # passage par deepcopy essentiel pour que l'objet soit copié en profondeur et ne soit ainsi pas affecté
        # par les changements apportés au referentiel de l'instance ChoixStrategie.
        sauvegarde = deepcopy(self.choix_mode_jeu.get_save())
        new_data = [["_test", 3, 3, "{'nav_test': 2}", 1]]
        df_new_data = pd.DataFrame(new_data,
                                   columns=['nom', 'taille_grille_x', 'taille_grille_y', 'liste_navires',
                                            'nombre_navires'])

        # modification de la variable 'save' artificiellement avec la nouvelle ligne de test
        self.choix_mode_jeu.save = pd.concat([self.choix_mode_jeu.save, df_new_data], ignore_index=True)
        # ecriture dans le fichier de sauvegarde
        self.choix_mode_jeu.ecriture_sauvegarde()

        # on instancie un autre objet de la classe ChoixModeJeu afin d'avoir un referentiel vierge,
        # dont le remplissage est significatif pour le test (comparatif)
        self.choix_mode_jeu_2 = ChoixModeJeu()

        self.choix_mode_jeu_2.lecture_sauvegarde()

        # recuperation par lecture du fichier de sauvegarde des lignes ecrites exclusivement pour le test.
        df_ligne_ecrite_test = self.choix_mode_jeu_2.get_save()[
            self.choix_mode_jeu_2.get_save().nom == "_test"]

        # Nt : 'df.values' d'un df pandas est de type <class 'numpy.ndarray'>,
        # il faut donc utiliser une methode specifique pour realiser un test
        self.assertTrue(np.array_equal(df_new_data.values, df_ligne_ecrite_test.values))

        # retablissement du fichier de sauvegarde avec les sauvegardes initiales - passage par une nouvelle instance de ChoixModeJeu
        # on utilise la methode d'ecriture testée.
        self.choix_mode_jeu_3 = ChoixModeJeu()
        self.choix_mode_jeu_3.save = sauvegarde
        self.choix_mode_jeu_3.ecriture_sauvegarde()

    # afficher_navires
    def test_afficher_navires_cas_nominal(self):
        self.choix_mode_jeu = ChoixModeJeu()
        self.choix_mode_jeu.set_attributes(nb_lignes=self.taille_grille[0], nb_colonnes=self.taille_grille[1],
                                           navires=self.navires, nom_mode_jeu="Normal")
        self.assertEqual(True, self.choix_mode_jeu.afficher_navires(self.choix_mode_jeu.get_navires()))
