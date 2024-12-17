import unittest
from Strategie import Strategie
from Grille import Grille

class TestStrategie(unittest.TestCase):
    def setUp(self) -> None:
        self.navires = {
            'Torpilleur': [2, 'T'], 'Sous-marin': [3, 'S'], 'Frégate': [3, 'F'], 
            'Cuirassé': [4, 'C'], 'Porte-avions': [5, 'P']
        }
        self.strategie = Strategie({
            'Torpilleur': [2, 4, 9, 'O'], 'Sous-marin': [3, 3, 6, 'S'], 
            'Frégate': [3, 6, 9, 'S'], 'Cuirassé': [4, 9, 1, 'E'], 'Porte-avions': [5, 10, 7, 'N']
        }, self.navires, Grille(10, 10))

    def test_initialisation_strategie(self):
        self.assertEqual(
            self.strategie.informations,
            {
                'Torpilleur': [2, 4, 9, 'O'], 'Sous-marin': [3, 3, 6, 'S'],
                'Frégate': [3, 6, 9, 'S'], 'Cuirassé': [4, 9, 1, 'E'], 'Porte-avions': [5, 10, 7, 'N']
            }
        )

    def test_grille_apres_initialisation(self):
        expected_grille = [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', 'S', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', 'S', '-', 'T', 'T', '-'],
            ['-', '-', '-', '-', '-', 'S', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', 'P', '-', 'F', '-'],
            ['-', '-', '-', '-', '-', '-', 'P', '-', 'F', '-'],
            ['-', '-', '-', '-', '-', '-', 'P', '-', 'F', '-'],
            ['C', 'C', 'C', 'C', '-', '-', 'P', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', 'P', '-', '-', '-']
        ]
        self.assertEqual(self.strategie.instance_grille.grille, expected_grille)

    def test_verification_validite(self):
        self.assertTrue(self.strategie.verifier_validite())

    def test_placement_un_navire(self):
        grille = Grille(10, 10).creation_grille_de_jeu()
        navire_place = self.strategie.placement_un_navire(grille, {
            'Torpilleur': [2, 5, 5, 'S']
        }, 'Torpilleur')
        self.assertTrue(navire_place)

    def test_strategie_non_valide(self):
        # Placement invalide, chevauchement ou hors grille
        strategie_invalide = Strategie(
            {'Torpilleur': [2, 9, 9, 'S']}, self.navires, Grille(10, 10)
        )
        self.assertFalse(strategie_invalide.verifier_validite())

if __name__ == "__main__":
    unittest.main()
