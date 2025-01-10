import unittest

import pandas as pd

from Strategie import Strategie, Strategie_2
from Navire import Navire, FactoryNavire


class TestStrategie(unittest.TestCase) :
    def setUp(self) -> None:
        self.cuirasse = Navire(nom="cuirassé", taille=4)
        self.fregate = Navire(nom="frégate", taille=3)
        self.sous_marin = Navire(nom="sous-marin", taille=3)
        self.torpilleur = Navire(nom="torpilleur", taille=2)
        self.porte_avions = Navire(nom="porte-avions", taille=5)

        self.navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

    def test_set_navires_cas_nominal(self)->None:
        navires = {'Torpilleur': [2, 'T'], 'Sous-marin': [3, 'S'], 'Frégate': [3, 'F'], 'Cuirassé': [4, 'C'],
                   'Porte-avions': [5, 'P']}
        inputs_strategie = {'Torpilleur': [2, 1, 1, 'S'],
                                  'Sous-marin': [3, 5, 1, 'S'],
                                  'Frégate': [3, 3, 5, 'E'],
                                  'Cuirassé': [4, 5, 6, 'O'],
                                  'Porte-avions': [5, 9, 9, 'N']}
        self.strategie = Strategie(inputs_strategie=inputs_strategie, navires=navires)

        self.strategie.set_navires(navires=self.strategie.navires)
        self.strategie.set_informations(self.strategie.informations)

        self.assertEqual({'Torpilleur': [2, 'T'], 'Sous-marin': [3, 'S'], 'Frégate': [3, 'F'], 'Cuirassé': [4, 'C'],
                   'Porte-avions': [5, 'P']}, self.strategie.get_navires())
        self.assertEqual({'Torpilleur': [2, 1, 1, 'S'],
                                  'Sous-marin': [3, 5, 1, 'S'],
                                  'Frégate': [3, 3, 5, 'E'],
                                  'Cuirassé': [4, 5, 6, 'O'],
                                  'Porte-avions': [5, 9, 9, 'N']}, self.strategie.get_informations())


    def test_set_navires_cas_navires_similaires(self)->None:
        navires = {'Torpilleur': [2, 'T'], 'Sous-marin': [3, 'S'], 'Frégate': [3, 'F'], 'Cuirassé': [4, 'C'],
                   'Porte-avions': [5, 'P'], 'Sous-marin': [4, 'S']}
        inputs_strategie = {'Torpilleur': [2, 1, 1, 'S'],
                                  'Sous-marin': [3, 5, 1, 'S'],
                                  'Frégate': [3, 3, 5, 'E'],
                                  'Cuirassé': [4, 5, 6, 'O'],
                                  'Porte-avions': [5, 9, 9, 'N']}
        self.strategie = Strategie(inputs_strategie=inputs_strategie, navires=navires)

        self.strategie.set_navires(navires=self.strategie.navires)
        self.strategie.set_informations(self.strategie.informations)

        self.assertEqual({'Torpilleur': [2, 'T'], 'Sous-marin': [3, 'S'], 'Frégate': [3, 'F'], 'Cuirassé': [4, 'C'],
                   'Porte-avions': [5, 'P'], 'Sous-marin': [4, 'S']}, self.strategie.get_navires())
        self.assertEqual({'Torpilleur': [2, 1, 1, 'S'],
                                  'Sous-marin': [3, 5, 1, 'S'],
                                  'Frégate': [3, 3, 5, 'E'],
                                  'Cuirassé': [4, 5, 6, 'O'],
                                  'Porte-avions': [5, 9, 9, 'N']}, self.strategie.get_informations())



class TestStrategie_2(unittest.TestCase) :
    def setUp(self) -> None:
        self.cuirasse = FactoryNavire(nom="cuirassé", taille=4).get_navire()
        self.fregate = FactoryNavire(nom="frégate", taille=3).get_navire()
        self.sous_marin = FactoryNavire(nom="sous-marin", taille=3).get_navire()
        self.torpilleur = FactoryNavire(nom="torpilleur", taille=2).get_navire()
        self.porte_avions = FactoryNavire(nom="porte-avions", taille=5).get_navire()
        self.chaloupe = FactoryNavire(nom="chaloupe", taille=2).get_navire()


    def test_set_navires_cas_nominal(self)->None:
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avion"],
                                "taille": [2, 3, 3, 4, 5], "coord_x": [1, 5, 3, 5, 9],
                                "coord_y": [1, 1, 5, 6, 9], "orientation": ["S", "S", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
        self.strategie.set_navires()
        self.strategie.set_informations()
        self.strategie.set_grille()

        ## Tests
        self.assertEqual(navires, self.strategie.get_navires())
        # test de l'assertion d'égalité de Dataframe avec le module pandas.
        pd.testing.assert_frame_equal(inputs_strategie, self.strategie.get_informations())


    def test_set_navires_nb_navires_differents_1(self) -> None:
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avion", "chaloupe"],
                                 "taille": [2, 3, 3, 4, 5, 2], "coord_x": [1, 5, 3, 5, 9, 1],
                                 "coord_y": [1, 1, 5, 6, 9, 1], "orientation": ["S", "S", "E", "O", "N", "S"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        try:
            self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
            raise ValueError("Test non passé !")
        except ValueError as current_error:
            self.assertEqual(
                "Strategie non valide !\nLe nombre de navires de la stratégie diffère du nombre de navires attendus dans le mode de jeu associé.",
                str(current_error))


    def test_set_navires_nb_navires_differents_2(self)->None:
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions, self.chaloupe}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avion"],
                                "taille": [2, 3, 3, 4, 5], "coord_x": [1, 5, 3, 5, 9],
                                "coord_y": [1, 1, 5, 6, 9], "orientation": ["S", "S", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        try :
            self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
            raise ValueError("Test non passé !")
        except ValueError as current_error :
            self.assertEqual("Strategie non valide !\nLe nombre de navires de la stratégie diffère du nombre de navires attendus dans le mode de jeu associé.",
                             str(current_error))


    # Fonction : placement_navires
    def test_placement_navires_cas_nominal(self):
        # Initialisation
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avion"],
                                 "taille": [2, 3, 3, 4, 5], "coord_x": [1, 5, 3, 5, 9],
                                 "coord_y": [1, 1, 5, 6, 9], "orientation": ["S", "S", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
        self.strategie.set_navires()
        self.strategie.set_informations()
        self.strategie.set_grille()

        self.strategie.placement_navires(plateau=self.strategie.get_grille().get_plateau(),
                                                informations=self.strategie.get_informations())
        self.assertEqual([['T', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['T', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', 'F', 'F', 'F', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['S', '-', 'C', 'C', 'C', 'C', '-', '-', '-', '-'],
                          ['S', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['S', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']], self.strategie.get_grille().get_plateau())


    def test_navigation_set(self):
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions, self.chaloupe}
        for navire in navires :
            print(navire.get_nom())

        print(navires)
