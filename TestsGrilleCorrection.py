import unittest
from Grille import Grille, afficher_grille, afficher_couple_grilles

class TestGrille(unittest.TestCase) :
    
    def test_creation_grille_de_jeu_default(self):
        grille = Grille(10,10)
        self.assertTrue(grille.creation_grille_de_jeu())
        self.assertEqual(grille.plateau,
               [['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-']])

    def test_creation_grille_de_jeu_imposible_technique(self):
        grille = Grille(-1,-1)
        self.assertFalse(grille.creation_grille_de_jeu())
        
    def test_creation_grille_de_jeu_imposible_fonctionnel(self):
        grille = Grille(0, 0)
        self.assertFalse(grille.creation_grille_de_jeu())
        grille = Grille(1, 1)
        self.assertFalse(grille.creation_grille_de_jeu())
        grille = Grille(1, 2)
        self.assertTrue(grille.creation_grille_de_jeu())
        grille = Grille(2, 1)
        self.assertTrue(grille.creation_grille_de_jeu())

if __name__ == '__main__':
    unittest.main()