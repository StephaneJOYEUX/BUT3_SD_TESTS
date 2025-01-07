import unittest
from Grille import Grille, afficher_grille, afficher_couple_grilles

class MyTestCase(unittest.TestCase) :
    def setUp(self) -> None:
        self.grille1 : Grille = Grille(10,10)
        self.grille2 : Grille = Grille(0,0)
        self.grille3 : Grille = Grille(-1,-1)
        self.grille4 : Grille = Grille(10,10)

    def test_creation_grille_de_jeu_input_positives(self):
        print('test')
        self.assertEqual(self.grille1.grille,
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

    def test_creation_grille_de_jeu_input_nulles(self):
        self.assertEqual(self.grille2.grille, [])

    def test_creation_grille_de_jeu_input_negatives(self):
        self.assertEqual(self.grille3.grille, [])


    def test_afficher_grille(self):
        self.assertEqual(afficher_grille(self.grille1.grille),
               """- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -\n\n""")

    def test_afficher_couple_grilles(self):
        self.assertEqual(afficher_couple_grilles(self.grille1.grille, self.grille4.grille),
               """- - - - - - - - - -\n
               - - - - - - - - - -\n
               - - - - - - - - - -\n
               - - - - - - - - - -\n
               - - - - - - - - - -\n
               - - - - - - - - - -\n
               - - - - - - - - - -\n
               - - - - - - - - - -\n
               - - - - - - - - - -\n
               - - - - - - - - - -\n\n""")

if __name__ == '__main__':
    unittest.main()