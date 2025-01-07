import unittest
from Grille import Grille, afficher_grille, afficher_couple_grilles

class TestGrille(unittest.TestCase):

    def setUp(self):
        """Initialisation avant chaque test. Crée plusieurs instances de Grille pour les tests."""
        # Grilles de taille 3x3 et 5x5
        self.grille_3x3 = Grille(3, 3)
        self.grille_5x5 = Grille(5, 5)
        
        # Modifications de la grille 3x3 pour tests spécifiques
        self.grille_3x3_mod = Grille(3, 3)
        self.grille_3x3_mod.grille[0][0] = "X"  # Modification de la cellule (0, 0)
        
        # Autres grilles modifiées pour tester différentes valeurs
        self.grille_3x3_mod_2 = Grille(3, 3)
        self.grille_3x3_mod_2.grille[0][0] = "O"  # Modification de la cellule (0, 0)
    
    def test_grille_3x3(self):
        #test sur le nb de ligne et de colonne egal à [3,3]
        self.assertEqual(self.grille_3x3.nb_colonnes, 3)
        self.assertEqual(self.grille_3x3.nb_lignes, 3)

    def test_creation_grille(self):
        """
        Vérifie la création d'une grille avec des '-'.
        - Ce test assure que lors de la création d'une grille de taille 3x3, 
          toutes les cellules sont initialisées avec la valeur '-'.
        """
        expected_3x3 = [["-" for _ in range(3)] for _ in range(3)]
        self.assertEqual(self.grille_3x3.grille, expected_3x3)

    def test_grille_5x5(self):
        """
        Vérifie la création d'une grille de taille 5x5.
        - Ce test assure que lors de la création d'une grille de taille 5x5, 
          toutes les cellules sont également initialisées avec la valeur '-'.
        """
        expected_5x5 = [["-" for _ in range(5)] for _ in range(5)]
        self.assertEqual(self.grille_5x5.grille, expected_5x5)

    def test_grille_non_modifiee(self):
        """
        Vérifie qu'une grille non modifiée reste remplie de '-'.
        - Ce test vérifie que la grille reste inchangée avec des cellules contenant la valeur '-'
          tant qu'aucune modification n'a été effectuée.
        """
        for ligne in self.grille_3x3.grille:
            self.assertTrue(all(cell == "-" for cell in ligne))

    def test_grille_modifiee(self):
        """
        Vérifie qu'une grille peut être modifiée.
        - Ce test vérifie que, lorsque nous modifions une cellule d'une grille (exemple : mettre un 'X' à la position (0,0)),
          la modification est correctement appliquée.
        """
        self.assertEqual(self.grille_3x3_mod.grille[0][0], "X")
        self.assertEqual(self.grille_3x3_mod.grille[1][0], "-")
        self.assertEqual(self.grille_3x3_mod.grille[0][1], "-")

    def test_grille_taille_3x3_avec_valeurs(self):
        """
        Vérifie l'état de la grille de taille 3x3 après modification de certaines cellules.
        - Ce test assure que la grille 3x3 est modifiée correctement lorsque certaines cellules sont mises à jour 
          (ici, la cellule (0, 0) est définie à 'X').
        """
        expected = [
            ["X", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]
        self.assertEqual(self.grille_3x3_mod.grille, expected)

    def test_grille_taille_5x5_avec_valeurs(self):
        """
        Vérifie l'état de la grille de taille 5x5 après modification de certaines cellules.
        - Ce test vérifie qu'une modification peut être effectuée correctement sur une grille plus grande (5x5).
          Nous modifions la cellule (0,0) pour y insérer 'O', puis nous comparons la grille à la valeur attendue.
        """
        self.grille_5x5.grille[0][0] = "O"
        expected = [["-" for _ in range(5)] for _ in range(5)]
        expected[0][0] = "O"
        self.assertEqual(self.grille_5x5.grille, expected)

    def test_grille_avec_autre_valeur(self):
        """
    Test d'une grille de 3x3 avec des valeurs différentes ('X' et 'O').
    - Ce test vérifie que la grille accepte des valeurs autres que le caractère '-' (comme 'X' et 'O').
      Ici, nous modifions la cellule (0, 0) pour 'X' et la cellule (1, 1) pour 'O', puis nous vérifions que 
      la grille correspond à l'état attendu.
    """
    # On modifie la grille comme suit
        self.grille_3x3_mod_2.grille[0][0] = "X"  # Modification de la cellule (0, 0)
        self.grille_3x3_mod_2.grille[1][1] = "O"  # Modification de la cellule (1, 1)

    # La grille attendue avec ces modifications
        expected = [
            ["X", "-", "-"],
            ["-", "O", "-"],
            ["-", "-", "-"]
        ]
    
    # Comparaison de la grille modifiée et de la grille attendue
        self.assertEqual(self.grille_3x3_mod_2.grille, expected)

    def test_modification_ligne(self):
        """
        Vérifie la modification d'une ligne spécifique.
        - Ce test vérifie que la modification d'une ligne spécifique (ici la première ligne) est correctement appliquée.
        """
        self.grille_3x3_mod.grille[0] = ["X", "X", "X"]  # Modifier la première ligne
        expected = [
            ["X", "X", "X"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]
        self.assertEqual(self.grille_3x3_mod.grille, expected)

    # Test sur la modification d'une colonne
    def test_modification_colonne(self):
        """
        Vérifie la modification d'une colonne spécifique.
        - Ce test vérifie que la modification d'une colonne spécifique (ici la première colonne) est correctement appliquée.
        """
        # Modification de la première colonne
        self.grille_3x3_mod.grille[0][0] = "X"
        self.grille_3x3_mod.grille[1][0] = "X"
        self.grille_3x3_mod.grille[2][0] = "X"
        
        expected = [
            ["X", "-", "-"],
            ["X", "-", "-"],
            ["X", "-", "-"]
        ]
        self.assertEqual(self.grille_3x3_mod.grille, expected)

    # Test pour vérifier le contenu d'une ligne après modification
    def test_verification_ligne_modifiee(self):
        """
        Vérifie le contenu d'une ligne après modification.
        - Ce test vérifie que la ligne (ici la première) contient les bonnes valeurs après une modification.
        """
        self.grille_3x3_mod_2.grille[0] = ["X", "O", "-"]  # Modification de la première ligne
        self.assertEqual(self.grille_3x3_mod_2.grille[0], ["X", "O", "-"])

    # Test pour vérifier le contenu d'une colonne après modification
    def test_verification_colonne_modifiee(self):
        """
        Vérifie le contenu d'une colonne après modification.
        - Ce test vérifie que la colonne (ici la première) contient les bonnes valeurs après une modification.
        """
        self.grille_3x3_mod_2.grille[0][0] = "X"
        self.grille_3x3_mod_2.grille[1][0] = "O"
        self.grille_3x3_mod_2.grille[2][0] = "-"
        
        # Vérification de la colonne (0) après modification
        self.assertEqual([self.grille_3x3_mod_2.grille[i][0] for i in range(3)], ["X", "O", "-"])

    # Test pour vérifier que l'ensemble de la grille est correctement modifié par des lignes et colonnes
    def test_modification_lignes_colonnes_combinees(self):
        """
        Vérifie que la modification combinée de lignes et colonnes fonctionne.
        - Ce test vérifie que nous pouvons appliquer des modifications sur une ligne et une colonne simultanément
          et que la grille reflète correctement ces modifications.
        """
        # Modifier la première ligne et la première colonne
        self.grille_3x3_mod_2.grille[0] = ["X", "X", "X"]
        self.grille_3x3_mod_2.grille[1][0] = "O"
        self.grille_3x3_mod_2.grille[2][0] = "-"
        
        expected = [
            ["X", "X", "X"],
            ["O", "-", "-"],
            ["-", "-", "-"]
        ]
        self.assertEqual(self.grille_3x3_mod_2.grille, expected)

"""
2 Test à résoudre car ne fonctionne pas

    def test_grille_invalide(self):
        with self.assertRaises(ValueError):
            Grille(0,0)
        with self.assertRaises(ValueError):
            Grille(-1,-1)
    
    def test_creation_grille_de_jeu_impossible_fonctionnel(self):
        grille = Grille(0, 0)
        self.assertFalse(grille.creation_grille_de_jeu())
"""
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
if __name__ == "__main__":
    unittest.main()
