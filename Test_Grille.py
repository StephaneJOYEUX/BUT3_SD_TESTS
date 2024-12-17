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
        grille_custom = Grille(7, 10)
        self.assertEqual(grille_custom.getNbLignes(), 7)
        self.assertEqual(grille_custom.getNbColonnes(), 10)

    def test_getters(self):
        # Teste les getters pour les dimensions de la grille
        self.assertEqual(self.grille.getNbLignes(), 10)
        self.assertEqual(self.grille.getNbColonnes(), 10)

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

    def test_grille_valide(self):
        # Teste si une grille valide est créée sans erreur
        try:
            grille_valide = Grille(10, 10)
            self.assertEqual(grille_valide.getNbLignes(), 10)
            self.assertEqual(grille_valide.getNbColonnes(), 10)
        except Exception as e:
            self.fail(f"La création d'une grille valide a échoué ... : {e}")

    def test_grille_invalide(self):
        # Teste si une grille invalide lève une ValueError
        with self.assertRaises(ValueError):
            Grille(0, 0)  
        with self.assertRaises(ValueError):
            Grille(-1, -1)  


if __name__ == "__main__":
    unittest.main()
