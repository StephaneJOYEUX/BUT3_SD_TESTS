import unittest
from Grille import Grille, afficher_grille, afficher_couple_grilles

class TestGrille(unittest.TestCase):
    def setUp(self):
        self.grille = Grille(10, 10)

    def test_creation_grille_de_jeu(self):
        # Teste si la grille est correctement créée avec les bonnes dimensions
        self.assertEqual(len(self.grille.grille), 10)
        self.assertEqual(len(self.grille.grille[0]), 10)
        self.assertTrue(all(cell == '-' for row in self.grille.grille for cell in row))

    def test_grille_dimensions(self):
        # Teste la création d'une grille de dimensions personnalisées
        grille_custom = Grille(5, 8)
        self.assertEqual(len(grille_custom.grille), 5)
        self.assertEqual(len(grille_custom.grille[0]), 8)

    def test_afficher_grille(self):
        # Teste l'affichage de la grille (simple validation pour le bon fonctionnement)
        try:
            afficher_grille(self.grille.grille)
        except Exception as e:
            self.fail(f"afficher_grille raised an exception: {e}")

    def test_afficher_couple_grilles(self):
        # Teste l'affichage de deux grilles côte-à-côte
        try:
            afficher_couple_grilles(self.grille.grille, self.grille.grille)
        except Exception as e:
            self.fail(f"afficher_couple_grilles raised an exception: {e}")

    def test_grille_invalide(self):
        # Teste si la création d'une grille avec des dimensions invalides lève une erreur
        with self.assertRaises(ValueError):
            Grille(-1, 10)
        with self.assertRaises(ValueError):
            Grille(10, -1)
        with self.assertRaises(ValueError):
            Grille(0, 10)
        with self.assertRaises(ValueError):
            Grille(10, 0)


if __name__ == "__main__":
    unittest.main()
