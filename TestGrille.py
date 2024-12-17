import unittest
from Grille import *

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None :
        self.grille3x4 = Grille(3, 4)



    def test_initialisation_grille(self):

        # Vérification des attribut
        self.assertEqual(self.grille3x4.nb_lignes, 3)
        self.assertEqual(self.grille3x4.nb_colonnes, 4)

        self.assertEqual(len(self.grille3x4.grille), 3)
        self.assertEqual(len(self.grille3x4.grille[0]), 4)

    def test_creation_grille_de_jeu(self):
        # Création d'une grille de 2x2
        grille = Grille(2, 2)

        # Vérification de la grille
        self.assertTrue(grille.creation_grille_de_jeu())
        self.assertEqual(grille.grille, [['-', '-'], ['-', '-']])

    def test_afficher_grille(self):
        # Création d'une grille 2x2
        grille = Grille(2, 2)

        # Tester l'affichage de la grille
        result = afficher_grille(grille.grille)

        # Vérification du résultat
        expected_output = "- - \n- - \n\n"
        self.assertEqual(result, expected_output)

    def test_afficher_couple_grilles(self):
        # Création de deux grilles
        grille1 = Grille(2, 2)
        grille2 = Grille(2, 2)

        # Modifier certaines cases dans grille1 et grille2 pour avoir des différences
        grille1.grille[0][0] = "X"
        grille2.grille[1][1] = "O"

        # Tester l'affichage des deux grilles côte à côte
        result = afficher_couple_grilles(grille1.grille, grille2.grille)

        # Vérification du résultat attendu
        expected_output = "     Vos navires :                      Champ de tir :\n"
        expected_output += "     X -                - - \n"
        expected_output += "     - -                - O \n\n"

        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
