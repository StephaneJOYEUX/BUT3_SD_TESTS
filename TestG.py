import unittest
from Grille import Grille
import io
import sys
from Grille import afficher_grille
from Grille import afficher_couple_grilles

class TestGrille(unittest.TestCase):

    def test_initialisation_grille(self):
        grille = Grille(3, 3)
        self.assertEqual(grille.nb_lignes, 3)
        self.assertEqual(grille.nb_colonnes, 3)
        self.assertEqual(len(grille.grille), 3)  
        self.assertEqual(len(grille.grille[0]), 3)  
        
        for ligne in grille.grille:
            self.assertTrue(all(cell == "-" for cell in ligne))
        
    def test_initialisation_grille_vide(self):
        grille = Grille(0, 0)
        self.assertEqual(grille.nb_lignes, 0)
        self.assertEqual(grille.nb_colonnes, 0)
        self.assertEqual(grille.grille, [])


class TestAffichage(unittest.TestCase):

    def test_affichage_grille(self):
        grille = Grille(3, 3)
        # Capture la sortie de print
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        afficher_grille(grille.grille)
        
        sys.stdout = sys.__stdout__  # Restaure stdout
        
        # Vérifie que l'affichage est correct
        expected_output = "- - - \n- - - \n- - - \n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_afficher_couple_grilles(self):
        grille1 = Grille(2, 2)
        grille2 = Grille(2, 2)
        
        # Capture la sortie de print
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        afficher_couple_grilles(grille1.grille, grille2.grille)
        
        sys.stdout = sys.__stdout__  # Restaure stdout
        
        # Vérifie que l'affichage est correct
        expected_output = "     Vos navires :                      Champ de tir :\n"
        expected_output += "     - -                - -\n"
        expected_output += "     - -                - -\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

