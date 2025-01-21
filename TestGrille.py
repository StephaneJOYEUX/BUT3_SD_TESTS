import unittest
from Grille import Grille, afficher_grille, afficher_couple_grilles
"""
utilisateur doit pouvoir choisir la taille de la grille
"""

class TestGrille(unittest.TestCase):

    def test_creation_grille_valide(self) -> None:
        grille_valide = Grille(2,2)  
        self.assertTrue(grille_valide.creation_grille_de_jeu())
    
    def test_creation_grille_invalide_fonctionnelle(self)-> None :
            grille_invalide = Grille(1, 1)  
            with self.assertRaises(ValueError):
                grille_invalide.creation_grille_de_jeu()
                
    def test_creation_grille_invalide_technique(self)-> None :
            grille_invalide = Grille(-1, -1)  
            with self.assertRaises(ValueError):
                grille_invalide.creation_grille_de_jeu()
      
    def test_affichage_grille_simple(self)-> None :

        self.grille = [
            ["-", "-"],
            ["-", "-"]
        ]

        resultat_grille_affiche = afficher_grille(self.grille)


        resultat_grille_affichage_esperer = "- -\n- -\n"


        self.assertEqual(resultat_grille_affiche, resultat_grille_affichage_esperer)
        
    def test_afficher_couple_grilles(self):
        grille1 = Grille(10,10)
        grille2 = Grille(10,10)
        self.assertTrue(grille1.creation_grille_de_jeu())
        self.assertTrue(grille2.creation_grille_de_jeu())
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
               
               
               
               
               
               
               
               