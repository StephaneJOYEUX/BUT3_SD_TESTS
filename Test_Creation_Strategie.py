import unittest
from CreationStrategie import CreationStrategie
from Grille import Grille
from Strategie import Strategie

class TestCreationStrategie(unittest.TestCase):
    def setUp(self) -> None:
        self.navires = {
            'Torpilleur': [2, 'T'], 'Sous-marin': [3, 'S'], 'Frégate': [3, 'F'],
            'Cuirassé': [4, 'C'], 'Porte-avions': [5, 'P']
        }
        self.grille = Grille(10, 10)

    def test_creation_strategie_instance(self):
        # Test avec des valeurs prédéfinies (mode test=True)
        creation = CreationStrategie(self.navires, self.grille, test=True)
        strategie = creation.get_instance_strategie()
        self.assertIsInstance(strategie, Strategie)
        
    def test_strategie_contenu(self):
        # Teste si les valeurs de stratégie sont correctes après création en mode test
        creation = CreationStrategie(self.navires, self.grille, test=True)
        strategie = creation.get_instance_strategie()
        expected_strategie = {
            'Torpilleur': [2, 4, 9, 'O'], 'Sous-marin': [3, 3, 6, 'S'],
            'Frégate': [3, 6, 9, 'S'], 'Cuirassé': [4, 9, 1, 'E'], 'Porte-avions': [5, 10, 7, 'N']
        }
        self.assertEqual(strategie.informations, expected_strategie)

    def test_grille_validite(self):
        # Teste si la grille est correctement mise à jour
        creation = CreationStrategie(self.navires, self.grille, test=True)
        strategie = creation.get_instance_strategie()
        self.assertTrue(strategie.verifier_validite())

if __name__ == "__main__":
    unittest.main()
