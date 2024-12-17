import unittest
from Grille import Grille, afficher_grille, afficher_couple_grilles

class MyTestGrilleCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.grille1: Grille = Grille(10,10)
        self.grille2: Grille = Grille(0,0)
        self.grille3: Grille = Grille(-1,-1)
        self.grille4: Grille = Grille(10,10)
    
    def test_init_grille(self):
    
        self.assertEqual(10, self.grille1.get_nb_lignes())
        self.assertEqual(10, self.grille1.get_nb_colonne())
        
    def test_creation_grille_de_jeu_input_positives(self):
        self.assertEqual(
                [['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-'],
                ['-','-','-','-','-','-','-','-','-','-']], self.grille1.grille)


    def test_creation_grille_de_jeu_valide(self):
        if self.assertEqual([], self.grille1.grille):
            "Grille valide"
        else:
            "Grille invalide"
        if self.assertEqual([], self.grille2.grille):
            "Grille valide"
        else:
            "Grille invalide"

    def test_creation_grille_de_jeu_invalide(self):
        if not self.assertEqual([], self.grille3.grille):
            "Grille invalide"
        else:
            "Grille valide"
        if not self.assertEqual([], self.grille4.grille):
            "Grille invalide"
        else:
            "Grille valide"


    def test_afficher_grille(self):
        self.assertEqual(("- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"), afficher_grille(self.grille1.grille))


    def test_afficher_couple_grilles(self):
        self.assertEqual((
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
            "     - - - - - - - - - -                - - - - - - - - - -\n"), afficher_couple_grilles(self.grille1.grille, self.grille4.grille))
    
    if __name__ == '__main__':
        unittest.main()