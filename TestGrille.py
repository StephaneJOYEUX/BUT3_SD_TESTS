import unittest
from Grille import Grille, afficher_grille, afficher_couple_grilles

class TestGrille(unittest.TestCase):
    
    def test_init_grille(self):
        grille = Grille(2, 2)
        self.assertEqual(2, grille.getNbLignes())
        self.assertEqual(2, grille.getNbColonnes())
        
    def test_creation_grille_nominal(self):
        grille = Grille(10,10)
        self.assertTrue(grille.creation_grille())
        self.assertEqual(grille.grille,
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

    def test_creation_grille_impossible_technique(self):
        
        grille = Grille(-1, -1)
        self.assertFalse(grille.creation_grille())
        #self.assertEqual(self.grille1.grille,
            #[['-','-'],
             #['-','-']])
             
    def test_creation_grille_impossible_fonctionnel(self):
        grille = Grille(0, 0)
        self.assertFalse(grille.creation_grille())
        grille = Grille(1, 1)
        self.assertFalse(grille.creation_grille())
        grille = Grille(1, 2)
        self.assertTrue(grille.creation_grille())
        grille = Grille(2, 1)
        self.assertTrue(grille.creation_grille())

    def test_afficher_grille(self):
        grille = Grille(10,10)
        self.assertTrue(grille.creation_grille())
        self.assertEqual(("- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"), afficher_grille(grille.grille))


    def test_afficher_couple_grilles(self):
        grille1 = Grille(10,10)
        grille2 = Grille(10,10)
        self.assertTrue(grille1.creation_grille())
        self.assertTrue(grille2.creation_grille())
        self.assertEqual(afficher_couple_grilles(grille1.grille, grille2.grille),
            "     Vos navires :                      Champ de tir :\n"
            "     - - - - - - - - - -                - - - - - - - - - -\n"
            "     - - - - - - - - - -                - - - - - - - - - -\n"
            "     - - - - - - - - - -                - - - - - - - - - -\n"
            "     - - - - - - - - - -                - - - - - - - - - -\n"
            "     - - - - - - - - - -                - - - - - - - - - -\n"
            "     - - - - - - - - - -                - - - - - - - - - -\n"
            "     - - - - - - - - - -                - - - - - - - - - -\n"
            "     - - - - - - - - - -                - - - - - - - - - -\n"
            "     - - - - - - - - - -                - - - - - - - - - -\n"
            "     - - - - - - - - - -                - - - - - - - - - -\n")    

if __name__ == '__main__': 
    unittest.main()