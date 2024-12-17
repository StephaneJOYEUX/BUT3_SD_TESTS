# Tests unitaires pour la classe Grille et les fonctions d'affichage
class TestGrille(unittest.TestCase):

    def test_creation_grille_de_jeu(self):
        # Test pour vérifier que la grille est bien initialisée
        grille = Grille(3, 4)
        self.assertEqual(grille.nb_lignes, 3)
        self.assertEqual(grille.nb_colonnes, 4)
        self.assertTrue(all(cell == "-" for row in grille.grille for cell in row))

    def test_creation_grille_de_jeu_vide(self):
        # Test pour une grille vide (0 lignes, 0 colonnes)
        grille = Grille(0, 0)
        self.assertEqual(grille.nb_lignes, 0)
        self.assertEqual(grille.nb_colonnes, 0)
        self.assertEqual(grille.grille, [])

    def test_creation_grille_non_vide(self):
        # Test pour une grille non vide
        grille = Grille(2, 3)
        self.assertEqual(grille.nb_lignes, 2)
        self.assertEqual(grille.nb_colonnes, 3)
        self.assertTrue(all(cell == "-" for row in grille.grille for cell in row))

    def test_afficher_grille(self):
        # Tester l'affichage de la grille
        grille = Grille(2, 2)
        expected_output = "- - \n- - \n\n"
        
        captured_output = StringIO()
        sys.stdout = captured_output
        afficher_grille(grille.grille)
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_afficher_couple_grilles(self):
        # Tester l'affichage de deux grilles
        grille1 = [["-", "-", "-"], ["-", "-", "-"]]
        grille2 = [["X", "-", "-"], ["-", "X", "O"]]
        
        expected_output = (
            "     Vos navires :                      Champ de tir :\n"
            "     - - -                X - - \n"
            "     - - -                - X O \n\n"
        )
        
        captured_output = StringIO()
        sys.stdout = captured_output
        afficher_couple_grilles(grille1, grille2)
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()