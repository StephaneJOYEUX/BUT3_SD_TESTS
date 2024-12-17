import unittest
from BatailleNavale import BatailleNavale
from Strategie import Strategie
from Grille import Grille
from unittest.mock import patch

class TestBatailleNavale(unittest.TestCase):
    def setUp(self):
        self.navires = {
            'Torpilleur': [2, 'T'], 'Sous-marin': [3, 'S'], 'Frégate': [3, 'F'],
            'Cuirassé': [4, 'C'], 'Porte-avions': [5, 'P']
        }
        self.strategie_j1 = Strategie({
            'Torpilleur': [2, 1, 1, 'S'], 'Sous-marin': [3, 2, 2, 'E']
        }, self.navires, Grille(10, 10))
        self.strategie_j2 = Strategie({
            'Frégate': [3, 5, 5, 'S'], 'Cuirassé': [4, 3, 3, 'N']
        }, self.navires, Grille(10, 10))
        self.bataille = BatailleNavale(self.navires, self.strategie_j1, self.strategie_j2, Grille(10, 10), test=True)

    def test_navire_coule(self):
        self.bataille.grille_def_j2[4][5] = '-'
        result = self.bataille.navire_coule('F', self.bataille.grille_def_j2)
        self.assertTrue(result)

    def test_tir_rate(self):
        result = self.bataille.tir(1, 1, 1)
        self.assertEqual(result, "Raté")

    def test_tir_touche(self):
        self.bataille.grille_def_j2[4][5] = 'F'
        result = self.bataille.tir(1, 5, 6)
        self.assertEqual(result, "Touché")

    def test_tir_touche_coule(self):
        self.bataille.grille_def_j2[4][5] = 'F'
        self.bataille.grille_def_j2[5][5] = '-'
        result = self.bataille.tir(1, 5, 6)
        self.assertEqual(result, "Touché, Coulé")

    def test_tous_les_navires_ont_coule(self):
        for i in range(10):
            for j in range(10):
                self.bataille.grille_def_j2[i][j] = '-'
        self.assertTrue(self.bataille.tous_les_navires_ont_coule(self.bataille.grille_def_j2))

if __name__ == "__main__":
    unittest.main()
