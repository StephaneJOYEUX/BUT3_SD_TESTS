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
        
    def test_affichage_grille_double(self) -> None:
        # Initialisation des grilles
        grille_1 = Grille(10, 10)
        grille_2 = Grille(10, 10)
        
        # Affichage des grilles via la fonction
        resultat = afficher_couple_grilles(grille_1.grille, grille_2.grille)
    
        # Résultat attendu
        resultat_attendu = """     Vos navires :                      Champ de tir :
         - - - - - - - - - -                - - - - - - - - - -
         - - - - - - - - - -                - - - - - - - - - -
         - - - - - - - - - -                - - - - - - - - - -
         - - - - - - - - - -                - - - - - - - - - -
         - - - - - - - - - -                - - - - - - - - - -
         - - - - - - - - - -                - - - - - - - - - -
         - - - - - - - - - -                - - - - - - - - - -
         - - - - - - - - - -                - - - - - - - - - -
         - - - - - - - - - -                - - - - - - - - - -
         - - - - - - - - - -                - - - - - - - - - -"""

        # Comparaison des résultats
        self.assertEqual(resultat, resultat_attendu)

        
                             
if __name__ == '__main__': 
    unittest.main()             
               
               
               
               
               
               
               
               