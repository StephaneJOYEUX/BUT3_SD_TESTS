import unittest
from Grille import *

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None :

        self.grille3x4 = Grille(3, 4)
        self.grille2x2 = Grille(2, 2)

        #self.grilleError = Grille(1.2, 2.3)
        #self.grilleError1 = Grille("", "")
        #self.grilleError2 = Grille(-1,-1)

    def test_initialisation_grille(self):

        self.assertEqual(self.grille3x4.get_nb_lignes(), 3)
        self.assertEqual(self.grille3x4.get_nb_colonnes(), 4)

    def test_init_grille(self):

        self.assertEqual(len(self.grille3x4.grille), 3)
        self.assertEqual(len(self.grille3x4.grille[0]), 4)

    def test_creation_grille_de_jeu(self):

        self.assertTrue(self.grille2x2.creation_grille_de_jeu())

    def test_afficher_grille(self):

        reslt = afficher_grille(self.grille2x2.grille)

        expected = "- -\n- -\n"
        self.assertEqual(reslt, expected)

    def test_afficher_couple_grilles(self):
        self.grille2x2.grille[0][0] = "X"
        self.grille3x4.grille[1][1] = "O"

        expected = "     Vos navires :                      Champ de tir :\n"
        expected += "     X -                - - \n"
        expected += "     - -                - O \n\n"

        reslt = afficher_couple_grilles(self.grille2x2.grille, self.grille3x4.grille)

        self.assertEqual(reslt, expected)


if __name__ == '__main__':
    unittest.main()
