import unittest
from inspect import GEN_RUNNING

from Grille import Grille, afficher_grille, afficher_couple_grilles





class TestGrille(unittest.TestCase) :
    # Tests sur la creation
    def test_creation_grille_cas_nominal(self) -> None:
        self.grille: Grille = Grille(10, 10)
        self.assertEqual(True, self.grille.create())
        self.assertEqual(
            [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']], self.grille.plateau)
        self.assertEqual(10, self.grille.get_nb_lignes())
        self.assertEqual(10, self.grille.get_nb_colonne())

    def test_creation_grille_cas_nul(self) -> None :
        self.grille: Grille = Grille(0, 0)
        self.assertEqual(False, self.grille.create())
        self.assertEqual([], self.grille.plateau)
        self.assertEqual(None, self.grille.get_nb_lignes())
        self.assertEqual(None, self.grille.get_nb_colonne())

    def test_creation_grille_cas_negatif(self) -> None :
        self.grille: Grille = Grille(-1, -1)
        self.assertEqual(False, self.grille.create())
        self.assertEqual([], self.grille.plateau)
        self.assertEqual(None, self.grille.get_nb_lignes())
        self.assertEqual(None, self.grille.get_nb_colonne())


    # Tests sur le setter (lignes)
    def test_setter_nb_lignes_cas_nominal(self) -> None:
        self.grille = Grille(10, 10)
        try:
            self.grille.set_nb_lignes(self.grille.nombre_lignes)
        except ValueError as current_error:
            self.assertEqual(f"Le nombre de lignes minimum est {self.grille.taille_min} !", str(current_error))
        self.assertEqual(10, self.grille.get_nb_lignes())


    def test_setter_nb_lignes_cas_nul(self) -> None:
        self.grille = Grille(0, 0)
        try:
            self.grille.set_nb_lignes(self.grille.nombre_lignes)
        except ValueError as current_error:
            self.assertEqual(f"Le nombre de lignes minimum est {self.grille.taille_min} !", str(current_error))
        self.assertEqual(None, self.grille.get_nb_lignes())


    def test_setter_nb_lignes_cas_negatif(self) -> None:
        self.grille = Grille(-1, -1)
        try:
            self.grille.set_nb_lignes(self.grille.nombre_lignes)
        except ValueError as current_error :
            self.assertEqual(f"Le nombre de lignes minimum est {self.grille.taille_min} !", str(current_error))
        self.assertEqual(None, self.grille.get_nb_lignes())


    # Tests setter (colonnes)
    def test_setter_nb_colonnes_cas_nominal(self) -> None:
        self.grille = Grille(10, 10)
        try:
            self.grille.set_nb_colonnes(self.grille.nombre_colonnes)
        except ValueError as current_error:
            self.assertEqual(f"Le nombre de colonnes minimum est {self.grille.taille_min} !", str(current_error))
        self.assertEqual(10, self.grille.get_nb_colonne())


    def test_setter_nb_colonnes_cas_nul(self) -> None:
        self.grille = Grille(0, 0)
        try:
            self.grille.set_nb_colonnes(self.grille.nombre_colonnes)
        except ValueError as current_error:
            self.assertEqual(f"Le nombre de colonnes minimum est {self.grille.taille_min} !", str(current_error))
        self.assertEqual(None, self.grille.get_nb_colonne())


    def test_setter_nb_colonnes_cas_negatif(self) -> None:
        self.grille = Grille(-1, -1)
        try:
            self.grille.set_nb_colonnes(self.grille.nombre_colonnes)
        except ValueError as current_error:
            self.assertEqual(f"Le nombre de colonnes minimum est {self.grille.taille_min} !", str(current_error))
        self.assertEqual(None, self.grille.get_nb_colonne())


    # Tests d'affichage
    def test_afficher_grille(self)-> None:
        self.grille = Grille(10,10)
        self.grille.create()
        self.assertEqual(("- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"
                          "- - - - - - - - - -\n"), afficher_grille(self.grille.plateau))

    def test_afficher_couple_grilles(self):
        # intialisation des grilles
        self.grille1 = Grille(10,10)
        self.grille2 = Grille(10,10)
        # creation des plateau
        self.grille1.create()
        self.grille2.create()
        # test sur l'affichage simultané des 2 grilles
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
            "     - - - - - - - - - -                - - - - - - - - - -\n"),
            afficher_couple_grilles(self.grille1.plateau, self.grille2.plateau))
