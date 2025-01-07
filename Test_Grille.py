import unittest
from Grille import Grille, afficher_grille, afficher_couple_grilles

class GrilleTest(unittest.TestCase):
    def setUp(self):
        """Initialise une grille par défaut pour les tests."""
        self.grille = Grille(10, 10)

    def test_creation_grille_de_jeu(self):
        """Teste si la grille est correctement créée avec les bonnes dimensions."""
        self.assertEqual(len(self.grille.grille), 10, "La grille doit avoir 10 lignes.")
        self.assertEqual(len(self.grille.grille[0]), 10, "Chaque ligne doit avoir 10 colonnes.")
        self.assertTrue(all(cell == '-' for row in self.grille.grille for cell in row),
                        "Toutes les cellules doivent être initialisées avec '-'.")

    def test_grille_dimensions_personnalisees(self):
        """Teste la création d'une grille avec des dimensions personnalisées."""
        grille_custom = Grille(5, 8)
        self.assertEqual(len(grille_custom.grille), 5, "La grille doit avoir 5 lignes.")
        self.assertEqual(len(grille_custom.grille[0]), 8, "Chaque ligne doit avoir 8 colonnes.")

    def test_creation_grille_negative_dimensions(self):
        """Teste si une erreur est levée pour des dimensions négatives."""
        with self.assertRaises(ValueError, msg="Les dimensions négatives doivent lever une ValueError."):
            Grille(-1, 10)
        with self.assertRaises(ValueError, msg="Les dimensions négatives doivent lever une ValueError."):
            Grille(10, -1)

    def test_reinitialisation_grille(self):
        """Teste la réinitialisation de la grille après modification."""
        self.grille.grille[0][0] = "X"  # Modifie une cellule
        self.grille.creation_grille_de_jeu()  # Réinitialise la grille
        self.assertEqual(self.grille.grille[0][0], "-", "La cellule doit être réinitialisée à '-'.")

    def test_afficher_grille(self):
        """Teste l'affichage de la grille."""
        try:
            afficher_grille(self.grille.grille)
        except Exception as e:
            self.fail(f"afficher_grille a levé une exception : {e}")

    def test_afficher_grille_personnalisee(self):
        """Teste l'affichage d'une grille avec des valeurs personnalisées."""
        self.grille.grille[0][0] = "X"
        self.grille.grille[1][1] = "O"
        try:
            afficher_grille(self.grille.grille)
        except Exception as e:
            self.fail(f"afficher_grille a levé une exception : {e}")

    def test_afficher_couple_grilles(self):
        """Teste l'affichage de deux grilles côte à côte."""
        try:
            afficher_couple_grilles(self.grille.grille, self.grille.grille)
        except Exception as e:
            self.fail(f"afficher_couple_grilles a levé une exception : {e}")

    def test_afficher_couple_grilles_diff_tailles(self):
        """Teste l'affichage de deux grilles de tailles différentes."""
        grille_small = Grille(5, 5)
        grille_large = Grille(10, 10)
        try:
            afficher_couple_grilles(grille_small.grille, grille_large.grille)
        except Exception as e:
            self.fail(f"afficher_couple_grilles a levé une exception : {e}")

    def test_creation_grille_vide(self):
        """Teste la création de la grille après avoir vidé manuellement la grille."""
        self.grille.grille = []  # Vide la grille
        self.grille.creation_grille_de_jeu()  # Réinitialise la grille
        self.assertEqual(len(self.grille.grille), 10, "La grille doit avoir 10 lignes après réinitialisation.")
        self.assertEqual(len(self.grille.grille[0]), 10, "Chaque ligne doit avoir 10 colonnes après réinitialisation.")


if __name__ == "__main__":
    unittest.main()
