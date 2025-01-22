import unittest
from Grille import Grille
from Strategie import Strategie
from CreationStrategie import CreationStrategie


class TestCreationStrategie(unittest.TestCase):

    def setUp(self):
        self.navires = {
            'Torpilleur': [2],
            'Sous-marin': [3],
            'Frégate': [3],
            'Cuirassé': [4],
            'Porte-avions': [5]
        }
        self.grille = Grille(10, 10)
        self.strategie = CreationStrategie(self.navires, self.grille, test=True)

    def test_initialisation(self):
        self.assertIsNotNone(self.strategie)
        self.assertEqual(self.strategie.premiere_ligne_grille, 1)
        self.assertEqual(self.strategie.derniere_ligne_grille, 10)
        self.assertEqual(self.strategie.premiere_colonne_grille, 1)
        self.assertEqual(self.strategie.derniere_colonne_grille, 10)

    def test_instance_strategie(self):
        self.assertIsInstance(self.strategie.get_instance_strategie(), Strategie)

    def test_strategie_valide_par_defaut(self):
        """test de la stratégie par default """
        self.assertTrue(self.strategie.get_instance_strategie().verifier_validite())


if __name__ == "__main__":
    unittest.main()

