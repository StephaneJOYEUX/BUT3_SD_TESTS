import unittest
from Grille import *


class TestGrille(unittest.TestCase):

    def setUp(self):

        self.grille3x4 = Grille(3, 4)
        self.grille2x2 = Grille(2, 2)#Grille(0, 0)

        #self.grilleError = Grille(1.2, 2.3)
        #self.grilleError1 = Grille("", "")
        #self.grilleError2 = Grille(-1,-1)

    def test_initialisation(self):

        self.assertEqual(self.grille3x4.get_nb_lignes(), 3)
        self.assertEqual(self.grille3x4.get_nb_colonnes(), 4)

        self.assertEqual(len(self.grille3x4.plateau), 3)
        self.assertEqual(len(self.grille3x4.plateau[0]), 4)

    def test_creation(self):

        self.assertTrue(self.grille2x2.creation_grille_de_jeu())
        self.assertEqual(self.grille2x2.plateau, [['-','-'], ['-','-']])

    def test_afficher(self):

        reslt = afficher_grille(self.grille2x2.plateau)

        expected = "- -\n- -\n"
        self.assertEqual(reslt, expected)

    def test_couple_grilles(self):
        self.grille2x2.plateau[0][0] = "X"
        self.grille3x4.plateau[1][1] = "O"

        expected = "     Vos navires :                      Champ de tir :\n"
        expected += "X -                - - - -\n"
        expected += "- -                - O - -\n"
        expected += "                - - - -\n"

        reslt = afficher_couple_grilles(self.grille2x2.plateau, self.grille3x4.plateau)

        self.assertEqual(reslt, expected)


if __name__ == '__main__':
    unittest.main()
