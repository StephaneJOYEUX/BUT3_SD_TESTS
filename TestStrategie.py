import unittest
from Strategie import Strategie


class MyTestCase(unittest.TestCase) :
    def setUp(self) -> None:
        pass

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