from unittest import TestCase

import numpy as np

from Strategie import Strategie, FactoryStrategie
from Navire import Navire, FactoryNavire
from Grille import Grille
from ChoixStrategie import ChoixStrategie
from ModeJeu import FactoryModeJeu
import pandas as pd
from pandas.testing import assert_frame_equal
from copy import deepcopy
import numpy as np


class TestChoixStrategie(TestCase):
    def setUp(self):
        self.cuirasse = FactoryNavire(nom="cuirassé", taille=4).get_navire()
        self.fregate = FactoryNavire(nom="frégate", taille=3).get_navire()
        self.sous_marin = FactoryNavire(nom="sous-marin", taille=3).get_navire()
        self.torpilleur = FactoryNavire(nom="torpilleur", taille=2).get_navire()
        self.porte_avions = FactoryNavire(nom="porte-avions", taille=5).get_navire()

        self.navires = {self.torpilleur, self.sous_marin, self.fregate, self.cuirasse, self.porte_avions}
        self.grille = Grille(10, 10)
        self.grille.create()
        self.mode_jeu = FactoryModeJeu(navires=self.navires, taille_grille=[10, 10], nom="Normal")

    ## Getters
    def test_get_referentiel(self):
        # Initialisation
        self.choix_strategie = ChoixStrategie("mon_pseudo", navires=self.navires, test=True, grille=self.grille,
                                              mode_jeu=self.mode_jeu)

        # creation d'un tableau numpy vide pour le test
        df_values_empty_test = np.empty((0, 7))
        self.assertTrue(np.array_equal(df_values_empty_test, self.choix_strategie.get_referentiel().values))

    def test_get_strategie(self):
        # Initialisation
        self.choix_strategie = ChoixStrategie("mon_pseudo", navires=self.navires, test=True, grille=self.grille,
                                              mode_jeu=self.mode_jeu)
        # test
        self.assertIs(None, self.choix_strategie.get_strategie())

    ## Methodes de classe
    def test_lecture_fichier_sauvegarde(self):
        # Initialisation
        self.choix_strategie = ChoixStrategie("mon_pseudo", navires=self.navires, test=True, grille=self.grille,
                                              mode_jeu=self.mode_jeu)
        self.choix_strategie.lire_fichier_sauvegarde()

        # test sur les entêtes
        self.assertEqual(['mode_jeu', 'index_strategie', 'nom', 'taille', 'coord_x', 'coord_y', 'orientation'],
                         list(self.choix_strategie.get_referentiel().columns))

    def test_ecriture_fichier_sauvegarde(self):
        # Initialisation
        self.choix_strategie = ChoixStrategie("mon_pseudo", navires=self.navires, test=True, grille=self.grille,
                                              mode_jeu=self.mode_jeu)
        # afin de tester la fonction d'ecriture :
        # recuperer le contenu du fichier de sauvegarde, le stocker dans une variable locale.
        # ajouter une nouvelle strategie, puis tester l'ecriture en verifiant avec la lecture que la ligne a bien ete ecrite.
        # réécrire la sauvegarde en enlevant la ligne artificielle ajoutee pour le test.
        self.choix_strategie.lire_fichier_sauvegarde()
        # recuperation de la sauvegarde :
        # passage par deepcopy essentiel pour que l'objet soit copié en profondeur et ne soit ainsi pas affecté
        # par les changements apportés au referentiel de l'instance ChoixStrategie.
        sauvegarde = deepcopy(self.choix_strategie.get_referentiel())
        index_test = max(sauvegarde.index_strategie) + 1
        new_data = [["Normal", index_test, "sous-marin", 3, 1, 1, "S"],
                    ["Normal", index_test, "cuirassé", 4, 2, 2, "S"],
                    ["Normal", index_test, "torpilleur", 2, 3, 3, "S"],
                    ["Normal", index_test, "porte-avions", 5, 4, 4, "S"],
                    ["Normal", index_test, "frégate", 3, 5, 5, "S"]]
        df_new_data = pd.DataFrame(new_data,
                                   columns=["mode_jeu", "index_strategie", "nom", "taille", "coord_x", "coord_y",
                                            "orientation"])

        # modification du referentiel avant ecriture : ajout des données pour le test
        for data_line in new_data:
            self.choix_strategie.referentiel.loc[len(self.choix_strategie.referentiel.index)] = data_line
        # ecriture dans le fichier de sauvegarde
        self.choix_strategie.ecrire_fichier_sauvegarde()

        # on instancie un autre objet de la classe ChoixStrategie afin d'avoir un referentiel vierge,
        # dont le remplissage est significatif pour le test (comparatif)
        self.choix_strategie_2 = ChoixStrategie("mon_pseudo_2", navires=self.navires, test=True, grille=self.grille,
                                                mode_jeu=self.mode_jeu)

        self.choix_strategie_2.lire_fichier_sauvegarde()

        # recuperation par lecture du fichier de sauvegarde des lignes ecrites exclusivement pour le test.
        df_ligne_ecrite_test = self.choix_strategie_2.get_referentiel()[
            self.choix_strategie_2.get_referentiel().index_strategie == index_test]

        # Nt : 'df.values' d'un df pandas est de type <class 'numpy.ndarray'>,
        # il faut donc utiliser une methode specifique pour realiser un test
        self.assertTrue(np.array_equal(df_new_data.values, df_ligne_ecrite_test.values))

        # retablissement du fichier de sauvegarde avec les sauvegardes initiales - passage par une nouvelle instance de ChoixStrategie
        # on utilise la methode d'ecriture testée.
        self.choix_strategie_3 = ChoixStrategie("mon_pseudo_3", navires=self.navires, test=True, grille=self.grille,
                                                mode_jeu=self.mode_jeu)
        self.choix_strategie_3.referentiel = sauvegarde
        self.choix_strategie_3.ecrire_fichier_sauvegarde()
