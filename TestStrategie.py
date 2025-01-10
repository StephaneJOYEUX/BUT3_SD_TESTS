import unittest

import pandas as pd

from Strategie import Strategie, Strategie_2
from Navire import Navire, FactoryNavire
from Grille import Grille


class TestStrategie(unittest.TestCase) :
    def setUp(self) -> None:
        self.cuirasse = Navire(nom="cuirassé", taille=4)
        self.fregate = Navire(nom="frégate", taille=3)
        self.sous_marin = Navire(nom="sous-marin", taille=3)
        self.torpilleur = Navire(nom="torpilleur", taille=2)
        self.porte_avions = Navire(nom="porte-avions", taille=5)

        self.navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

    # Setters & Getters
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


    ## getters & setters
    # set_navires
    def test_set_navires_cas_nominal(self)->None:
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avion"],
                                "taille": [2, 3, 3, 4, 5], "coord_x": [1, 5, 3, 5, 9],
                                "coord_y": [1, 1, 5, 6, 9], "orientation": ["S", "S", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
        self.strategie.set_navires()

        ## Tests
        self.assertEqual(navires, self.strategie.get_navires())


    def test_set_navires_nb_navires_differents_1(self) -> None:
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avions", "chaloupe"],
                                 "taille": [2, 3, 3, 4, 5, 2], "coord_x": [1, 5, 3, 5, 9, 1],
                                 "coord_y": [1, 1, 5, 6, 9, 1], "orientation": ["S", "S", "E", "O", "N", "S"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        try:
            self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
            self.strategie.set_navires()
            raise ValueError("Test non passé !")
        except ValueError as current_error:
            self.assertEqual(
                "Strategie non valide !\nLe nombre de navires de la stratégie diffère du nombre de navires attendus dans le mode de jeu associé.",
                str(current_error))


    def test_set_navires_nb_navires_differents_2(self)->None:
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions, self.chaloupe}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avions"],
                                "taille": [2, 3, 3, 4, 5], "coord_x": [1, 5, 3, 5, 9],
                                "coord_y": [1, 1, 5, 6, 9], "orientation": ["S", "S", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        try :
            self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
            self.strategie.set_navires()
            raise ValueError("Test non passé !")
        except ValueError as current_error :
            self.assertEqual("Strategie non valide !\nLe nombre de navires de la stratégie diffère du nombre de navires attendus dans le mode de jeu associé.",
                             str(current_error))


    # set_informations
    # Nt : il n'existe pas de cas d'echec pour cette fonction (en chercher 1)
    def test_set_informations_cas_nominal(self):
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avion"],
                                 "taille": [2, 3, 3, 4, 5], "coord_x": [1, 5, 3, 5, 9],
                                 "coord_y": [1, 1, 5, 6, 9], "orientation": ["S", "S", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
        self.strategie.set_informations()
        # test de l'assertion d'égalité de Dataframe avec le module pandas.
        pd.testing.assert_frame_equal(inputs_strategie, self.strategie.get_informations())


    # set_grille
    def test_set_grille_cas_nominal(self):
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avion"],
                                 "taille": [2, 3, 3, 4, 5], "coord_x": [1, 5, 3, 5, 9],
                                 "coord_y": [1, 1, 5, 6, 9], "orientation": ["S", "S", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
        self.strategie.set_grille()
        grille_test = Grille(10,10)
        grille_test.create()
        self.assertEqual(grille_test.get_plateau(), self.strategie.get_grille().get_plateau())



    ## Méthodes de classe.
    # Fonction : placement_un_navire
    def test_placement_un_navire_cas_nominal(self):
        # Initialisation
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avions"],
                                 "taille": [2, 3, 3, 4, 5], "coord_x": [1, 5, 3, 5, 9],
                                 "coord_y": [1, 1, 5, 6, 9], "orientation": ["S", "S", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
        self.strategie.set_navires()
        self.strategie.set_informations()
        self.strategie.set_grille()

        self.assertEqual(True, self.strategie.placement_un_navire(self.strategie.get_grille().get_plateau(),
                                                                  inputs_strategie.loc[0]))
        self.assertEqual([['T', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['T', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']],
                         self.strategie.get_grille().get_plateau())

    def test_placement_un_navire_conflit_ligne(self):
        # Initialisation
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avions"],
                                 "taille": [2, 3, 3, 4, 5], "coord_x": [1, 1, 3, 5, 9],
                                 "coord_y": [1, 3, 5, 6, 9], "orientation": ["S", "O", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
        self.strategie.set_navires()
        self.strategie.set_informations()
        self.strategie.set_grille()

        self.assertEqual(True, self.strategie.placement_un_navire(self.strategie.get_grille().get_plateau(),
                                                                  inputs_strategie.loc[0]))
        self.assertEqual(False, self.strategie.placement_un_navire(self.strategie.get_grille().get_plateau(),
                                                                   inputs_strategie.loc[1]))
        self.assertEqual([['T', 'S', 'S', '-', '-', '-', '-', '-', '-', '-'],
                          ['T', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']],
                         self.strategie.get_grille().get_plateau())


    def test_placement_un_navire_conflit_colonne(self):
        # Initialisation
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avions"],
                                 "taille": [2, 3, 3, 4, 5], "coord_x": [1, 4, 3, 5, 9],
                                 "coord_y": [1, 1, 5, 6, 9], "orientation": ["S", "N", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
        self.strategie.set_navires()
        self.strategie.set_informations()
        self.strategie.set_grille()

        self.assertEqual(True, self.strategie.placement_un_navire(self.strategie.get_grille().get_plateau(), inputs_strategie.loc[0]))
        self.assertEqual(False, self.strategie.placement_un_navire(self.strategie.get_grille().get_plateau(), inputs_strategie.loc[1]))
        self.assertEqual([['T', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['T', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['S', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['S', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']], self.strategie.get_grille().get_plateau())


    # Fonction : placement_navires
    def test_placement_navires_cas_nominal(self):
        # Initialisation
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avions"],
                                 "taille": [2, 3, 3, 4, 5], "coord_x": [1, 5, 3, 5, 9],
                                 "coord_y": [1, 1, 5, 6, 9], "orientation": ["S", "S", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
        self.strategie.set_navires()
        self.strategie.set_informations()
        self.strategie.set_grille()

        self.assertEqual(True, self.strategie.placement_navires(plateau=self.strategie.get_grille().get_plateau(),
                                         informations=self.strategie.get_informations()))
        self.assertEqual([['T', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                             ['T', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                             ['-', '-', '-', '-', 'F', 'F', 'F', '-', '-', '-'],
                             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                             ['S', '-', 'C', 'C', 'C', 'C', '-', '-', 'P', '-'],
                             ['S', '-', '-', '-', '-', '-', '-', '-', 'P', '-'],
                             ['S', '-', '-', '-', '-', '-', '-', '-', 'P', '-'],
                             ['-', '-', '-', '-', '-', '-', '-', '-', 'P', '-'],
                             ['-', '-', '-', '-', '-', '-', '-', '-', 'P', '-'],
                             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']],
                            self.strategie.get_grille().get_plateau())


    def test_placement_navires_conflit_ligne(self):
        # Initialisation
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        # création artificielle d'un conflit de placement des navires sur la première ligne.
        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avions"],
                                 "taille": [2, 3, 3, 4, 5], "coord_x": [1, 1, 3, 5, 9],
                                 "coord_y": [1, 3, 5, 6, 9], "orientation": ["S", "O", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
        self.strategie.set_navires()
        self.strategie.set_informations()
        self.strategie.set_grille()

        self.strategie.placement_navires(plateau=self.strategie.get_grille().get_plateau(),
                                         informations=self.strategie.get_informations())
        self.assertEqual([['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']],
                            self.strategie.get_grille().get_plateau())


    def test_placement_navires_conflit_colonne(self):
        # Initialisation
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        # création artificielle d'un conflit de placement des navires sur la première colonne.
        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avions"],
                                 "taille": [2, 3, 3, 4, 5], "coord_x": [1, 3, 3, 5, 9],
                                 "coord_y": [1, 1, 5, 6, 9], "orientation": ["S", "N", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
        self.strategie.set_navires()
        self.strategie.set_informations()
        self.strategie.set_grille()

        self.assertEqual(False, self.strategie.placement_navires(plateau=self.strategie.get_grille().get_plateau(),
                                         informations=self.strategie.get_informations()))
        self.assertEqual([['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']],
                         self.strategie.get_grille().get_plateau())


    # Fonction : verifier_validite
    def test_verifier_validite_cas_nominal(self):
        # Initialisation
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avions"],
                                 "taille": [2, 3, 3, 4, 5], "coord_x": [1, 5, 3, 5, 9],
                                 "coord_y": [1, 1, 5, 6, 9], "orientation": ["S", "S", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
        self.strategie.set_navires()
        self.strategie.set_informations()
        self.strategie.set_grille()
        self.assertEqual(True, self.strategie.verifier_validite())


    def test_verifier_validite_navires_differents(self):
        # Initialisation
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.chaloupe}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avions"],
                                 "taille": [2, 3, 3, 4, 5], "coord_x": [1, 5, 3, 5, 9],
                                 "coord_y": [1, 1, 5, 6, 9], "orientation": ["S", "S", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
        self.strategie.set_navires()
        self.strategie.set_informations()
        self.strategie.set_grille()
        self.assertEqual(False, self.strategie.verifier_validite())


    def test_verifier_validite_chevauchement_placement(self):
        # Initialisation
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avions"],
                                 "taille": [2, 3, 3, 4, 5], "coord_x": [1, 4, 3, 5, 9],
                                 "coord_y": [1, 1, 5, 6, 9], "orientation": ["S", "N", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
        self.strategie.set_navires()
        self.strategie.set_informations()
        self.strategie.set_grille()
        self.assertEqual(False, self.strategie.verifier_validite())


    # Fonction : affichage_strategie
    def test_affichage_strategie_cas_nominal(self):
        # avec une strategie valide
        # Initialisation
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avions"],
                                 "taille": [2, 3, 3, 4, 5], "coord_x": [1, 5, 3, 5, 9],
                                 "coord_y": [1, 1, 5, 6, 9], "orientation": ["S", "S", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
        self.strategie.set_navires()
        self.strategie.set_informations()
        self.strategie.set_grille()

        self.assertEqual(True, self.strategie.affichage_strategie())


    def test_affichage_strategie_cas_invalide(self):
        ## avec une strategie invalide => definir les critère de validité d'une strategie
        # + attente des test de la methode verifier_validite
        ## Initialisation
        # Initialisation
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avions"],
                                 "taille": [2, 3, 3, 4, 5], "coord_x": [1, 4, 3, 5, 9],
                                 "coord_y": [1, 1, 5, 6, 9], "orientation": ["S", "N", "E", "O", "N"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)
        self.strategie.set_navires()
        self.strategie.set_informations()
        self.strategie.set_grille()
        self.assertEqual(False, self.strategie.verifier_validite())

        self.assertEqual(False, self.strategie.affichage_strategie())

