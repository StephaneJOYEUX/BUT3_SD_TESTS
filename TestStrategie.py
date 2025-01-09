import unittest
from Strategie import Strategie, Strategie_2
from Navire import Navire


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
        self.cuirasse = Navire(nom="cuirassé", taille=4)
        self.fregate = Navire(nom="frégate", taille=3)
        self.sous_marin = Navire(nom="sous-marin", taille=3)
        self.torpilleur = Navire(nom="torpilleur", taille=2)
        self.porte_avions = Navire(nom="porte-avions", taille=5)


    def test_set_navires_cas_nominal(self)->None:
        navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}
        inputs_strategie = {'Torpilleur': [2, 1, 1, 'S'],
                                  'Sous-marin': [3, 5, 1, 'S'],
                                  'Frégate': [3, 3, 5, 'E'],
                                  'Cuirassé': [4, 5, 6, 'O'],
                                  'Porte-avions': [5, 9, 9, 'N']}
        self.strategie = Strategie_2(inputs_strategie=inputs_strategie, navires=navires)

        self.strategie.set_navires(navires=self.strategie.navires)
        self.strategie.set_informations(self.strategie.informations)

        self.assertEqual(navires, self.strategie.get_navires())
        self.assertEqual({'Torpilleur': [2, 1, 1, 'S'],
                                  'Sous-marin': [3, 5, 1, 'S'],
                                  'Frégate': [3, 3, 5, 'E'],
                                  'Cuirassé': [4, 5, 6, 'O'],
                                  'Porte-avions': [5, 9, 9, 'N']}, self.strategie.get_informations())


