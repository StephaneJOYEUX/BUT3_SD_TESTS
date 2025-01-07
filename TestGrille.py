import unittest
from Grille import Grille, afficher_grille, afficher_couple_grilles

class TestGrille(unittest.TestCase) :
    def setUp(self) -> None:
        self.grille4: Grille = Grille(10,10)

    def test_initialisation_grille1(self) -> None :
        self.grille1 : Grille = Grille(10,10)
        self.assertEqual(10, self.grille1.get_nb_lignes())
        self.assertEqual(10, self.grille1.get_nb_colonne())



   def test_initialisation_grille2(self) -> None :
        try:
            self.grille2: Grille = Grille(0,0)
            self.assertEqual(0, self.grille2.get_nb_lignes())
            self.assertEqual(0, self.grille2.get_nb_colonne())
        except ValueError:
            self.assertEqual("Le nombre de lignes minimum est 10 !", ValueError)
