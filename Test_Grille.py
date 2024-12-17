import unittest
from Grille import Grille, afficher_grille, afficher_couple_grilles

class GrilleTest(unittest.TestCase):
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

    def test_grille_negative_dimensions(self):
        # Teste si la création d'une grille avec des dimensions négatives lève une erreur
        with self.assertRaises(ValueError):
            Grille(-1, 10)
        with self.assertRaises(ValueError):
            Grille(10, -1)


    def test_creation_grille_de_jeu_modifiee(self):
        # Modifie la grille après l'initialisation et teste si elle est correctement réinitialisée
        self.grille.grille[0][0] = "X"  # Change un élément
        self.grille.creation_grille_de_jeu()  # Réinitialise la grille
        self.assertEqual(self.grille.grille[0][0], "-")  # Vérifie que la grille a été réinitialisée

    def test_afficher_grille_personnalisee(self):
        # Teste l'affichage d'une grille avec des valeurs spécifiques
        self.grille.grille[0][0] = "X"
        self.grille.grille[1][1] = "O"
        try:
            afficher_grille(self.grille.grille)
        except Exception as e:
            self.fail(f"afficher_grille raised an exception: {e}")

    def test_afficher_couple_grilles_diff_size(self):
        # Teste l'affichage de deux grilles de tailles différentes
        grille_small = Grille(5, 5)
        grille_large = Grille(10, 10)
        try:
            afficher_couple_grilles(grille_small.grille, grille_large.grille)
        except Exception as e:
            self.fail(f"afficher_couple_grilles raised an exception: {e}")

    def test_creation_grille_de_jeu_vide(self):
        # Crée une grille vide et teste la méthode de création
        self.grille.grille = []
        self.grille.creation_grille_de_jeu()
        self.assertEqual(len(self.grille.grille), 10)  # Vérifie que la grille a bien 10 lignes
        self.assertEqual(len(self.grille.grille[0]), 10)  # Vérifie que chaque ligne a bien 10 colonnes



if __name__ == "__main__":
    unittest.main()
