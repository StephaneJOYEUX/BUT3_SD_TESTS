# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:24:29 2024

@author: courte12u
"""

import unittest
from BatailleNavale import BatailleNavale
from Strategie import Strategie
from Grille import Grille
from CreationStrategie import CreationStrategie
from ChoixStrategie import ChoixStrategie

class MyTestCase(unittest.TestCase):
    # Initialisation de paramètres commun à plusieurs tests.
    def setUp(self) -> None:
        # On fixe les parametres de la partie.

        self.navires = {'Torpilleur': [2, 'T'], 'Sous-marin':[3, 'S'], 'Frégate':[3, 'F'], 'Cuirassé':[4, 'C'], 'Porte-avions':[5, 'P']}

        self.strategie_j1 = Strategie({'Torpilleur': [2, 4, 9, 'O'], 'Sous-marin': [3, 3, 6, 'S'], 'Frégate': [3, 6, 9, 'S'],
                              'Cuirassé': [4, 9, 1, 'E'], 'Porte-avions': [5, 10, 7, 'N']}, self.navires,
                                 Grille(10, 10))

        self.strategie_j2 = Strategie({'Torpilleur': [2, 3, 9, 'E'], 'Sous-marin': [3, 2, 2, 'S'], 'Frégate': [3, 5, 3, 'S'],
                              'Cuirassé': [4, 5, 8, 'O'], 'Porte-avions': [5, 2, 4, 'E']}, self.navires,
                                 Grille(10, 10))

        self.BatailleNavale = BatailleNavale(self.navires, self.strategie_j1, self.strategie_j2, test = True)

    def test_instances_partie(self):
        # On teste si les objets strategie de self.BatailleNavale sont bien des instances de la classe Strategie().
        # Sinon, on ne peut pas jouer en gros.
        self.assertIsInstance(self.BatailleNavale.strategie_j1, Strategie)
        self.assertIsInstance(self.BatailleNavale.strategie_j2, Strategie)

    def test_scenario_premier_tour(self):
        # tester que les strategie soient correctement placée dans les bonnes grilles (de defense de chacun des joueurs)
        self.assertEqual(self.BatailleNavale.grille_def_j1, [['-','-','-', '-','-','-','-','-','-', '-'],
                                                        ['-','-','-', '-','-','-','-','-','-', '-'],
                                                        ['-', '-','-', '-','-','S','-','-', '-', '-'],
                                                        ['-', '-','-', '-','-','S','-','T','T', '-'],
                                                        ['-', '-','-', '-','-','S','-', '-', '-', '-'],
                                                        ['-','-','-','-','-','-','P','-','F', '-'],
                                                        ['-','-','-','-','-','-','P','-','F', '-'],
                                                        ['-','-','-','-','-','-','P','-','F', '-'],
                                                        ['C','C','C', 'C','-','-','P','-','-', '-'],
                                                        ['-','-','-', '-','-','-','P','-','-', '-']])

        self.assertEqual(self.BatailleNavale.grille_def_j2, [['-','-','-', '-','-','-', '-','-','-', '-'],
                                                        ['-', 'S', '-', 'P', 'P', 'P', 'P', 'P', '-', '-'],
                                                        ['-', 'S','-', '-','-','-', '-','-', 'T', 'T'],
                                                        ['-', 'S','-', '-','-','-', '-','-','-', '-'],
                                                        ['-','-','F', '-', 'C', 'C', 'C', 'C', '-', '-'],
                                                        ['-','-','F','-','-','-', '-','-','-', '-'],
                                                        ['-','-','F','-','-','-', '-','-','-', '-'],
                                                        ['-','-','-', '-','-','-', '-','-','-', '-'],
                                                        ['-','-','-', '-','-','-', '-','-','-', '-'],
                                                        ['-','-','-', '-','-','-', '-','-','-', '-']])


        ## Premier tour
        # Le premier parametre de la methode de tir est le numéro du joueur qui tire (1 ou 2)
        self.assertEqual(self.BatailleNavale.tir(1, 1, 1), "Raté")
        self.assertEqual(self.BatailleNavale.tir(2, 3, 6), "Touché")
        # Un joueur qui touche rejoue
        self.assertEqual(self.BatailleNavale.tir(2, 4, 6), "Touché")
        self.assertEqual(self.BatailleNavale.tir(2, 5, 6), "Touché, Coulé")
        self.assertEqual(self.BatailleNavale.tir(2, 4, 8), "Touché")
        self.assertEqual(self.BatailleNavale.tir(2, 4, 9), "Touché, Coulé")
        self.assertEqual(self.BatailleNavale.tir(2, 1, 1), "Raté")

        # Fin du tour de jeu
        # On fait une assertion sur les grilles

        self.assertEqual(self.BatailleNavale.grille_def_j1, [['0', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', 'X', 'X', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'P', '-', 'F', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'P', '-', 'F', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'P', '-', 'F', '-'],
                                                        ['C', 'C', 'C', 'C', '-', '-', 'P', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'P', '-', '-', '-']])

        self.assertEqual(self.BatailleNavale.grille_def_j2, [['0', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', 'S', '-', 'P', 'P', 'P', 'P', 'P', '-', '-'],
                                                        ['-', 'S', '-', '-', '-', '-', '-', '-', 'T', 'T'],
                                                        ['-', 'S', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', 'F', '-', 'C', 'C', 'C', 'C', '-', '-'],
                                                        ['-', '-', 'F', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', 'F', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']])

        self.assertEqual(self.BatailleNavale.grille_att_j1, [['0', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']])

        self.assertEqual(self.BatailleNavale.grille_att_j2, [['0', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', 'X', 'X', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']])


        # Tests pour verifier si les bateaux ont coulés.
        # pour le joueur 2
        for infos_navire in self.navires.values():
            initiale = infos_navire[1]
            #verifie que les navires n'ont pas coulé
            self.assertFalse(self.BatailleNavale.navire_coule(initiale,self.BatailleNavale.grille_def_j2))

        # pour le joueur 1 il faut faire du cas par cas car il y a des bateaux coulés et non
        self.assertTrue(self.BatailleNavale.navire_coule('T', self.BatailleNavale.grille_def_j1))
        self.assertTrue(self.BatailleNavale.navire_coule('S', self.BatailleNavale.grille_def_j1))
        self.assertFalse(self.BatailleNavale.navire_coule('C', self.BatailleNavale.grille_def_j1))
        self.assertFalse(self.BatailleNavale.navire_coule('P', self.BatailleNavale.grille_def_j1))
        self.assertFalse(self.BatailleNavale.navire_coule('F', self.BatailleNavale.grille_def_j1))


        ## Deuxième tour
        self.assertEqual(self.BatailleNavale.tir(1, 2, 4), "Touché")
        self.assertEqual(self.BatailleNavale.tir(1, 2, 5), "Touché")
        self.assertEqual(self.BatailleNavale.tir(1, 2, 6), "Touché")
        self.assertEqual(self.BatailleNavale.tir(1, 2, 7), "Touché")
        self.assertEqual(self.BatailleNavale.tir(1, 2, 8), "Touché, Coulé")
        self.assertEqual(self.BatailleNavale.tir(1, 1, 2), "Raté")
        # Un joueur qui touche rejoue
        self.assertEqual(self.BatailleNavale.tir(2, 6, 7), "Touché")
        self.assertEqual(self.BatailleNavale.tir(2, 7, 7), "Touché")
        self.assertEqual(self.BatailleNavale.tir(2, 8, 7), "Touché")
        self.assertEqual(self.BatailleNavale.tir(2, 9, 7), "Touché")
        self.assertEqual(self.BatailleNavale.tir(2, 10, 7), "Touché, Coulé")
        self.assertEqual(self.BatailleNavale.tir(2, 9, 1), "Touché")
        self.assertEqual(self.BatailleNavale.tir(2, 9, 2), "Touché")
        self.assertEqual(self.BatailleNavale.tir(2, 9, 3), "Touché")
        self.assertEqual(self.BatailleNavale.tir(2, 9, 4), "Touché, Coulé")
        self.assertEqual(self.BatailleNavale.tir(2, 1, 2), "Raté")

        # Fin du tour de jeu
        # On fait une assertion sur les grilles

        self.assertEqual(self.BatailleNavale.grille_def_j1, [['0', '0', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', 'X', 'X', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'X', '-', 'F', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'X', '-', 'F', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'X', '-', 'F', '-'],
                                                        ['X', 'X', 'X', 'X', '-', '-', 'X', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'X', '-', '-', '-']])

        self.assertEqual(self.BatailleNavale.grille_def_j2, [['0', '0', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', 'S', '-', 'X', 'X', 'X', 'X', 'X', '-', '-'],
                                                        ['-', 'S', '-', '-', '-', '-', '-', '-', 'T', 'T'],
                                                        ['-', 'S', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', 'F', '-', 'C', 'C', 'C', 'C', '-', '-'],
                                                        ['-', '-', 'F', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', 'F', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']])

        self.assertEqual(self.BatailleNavale.grille_att_j1, [['0', '0', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', 'X', 'X', 'X', 'X', 'X', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']])

        self.assertEqual(self.BatailleNavale.grille_att_j2, [['0', '0', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', 'X', 'X', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'X', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'X', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'X', '-', '-', '-'],
                                                        ['X', 'X', 'X', 'X', '-', '-', 'X', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'X', '-', '-', '-']])

        # Tests pour verifier si les bateaux ont coulés.
        # pour le joueur 1
        self.assertTrue(self.BatailleNavale.navire_coule('T', self.BatailleNavale.grille_def_j1))
        self.assertTrue(self.BatailleNavale.navire_coule('S', self.BatailleNavale.grille_def_j1))
        self.assertTrue(self.BatailleNavale.navire_coule('C', self.BatailleNavale.grille_def_j1))
        self.assertTrue(self.BatailleNavale.navire_coule('P', self.BatailleNavale.grille_def_j1))
        self.assertFalse(self.BatailleNavale.navire_coule('F', self.BatailleNavale.grille_def_j1))

        # pour le joueur 2
        self.assertFalse(self.BatailleNavale.navire_coule('T', self.BatailleNavale.grille_def_j2))
        self.assertFalse(self.BatailleNavale.navire_coule('S', self.BatailleNavale.grille_def_j2))
        self.assertFalse(self.BatailleNavale.navire_coule('C', self.BatailleNavale.grille_def_j2))
        self.assertTrue(self.BatailleNavale.navire_coule('P', self.BatailleNavale.grille_def_j2))
        self.assertFalse(self.BatailleNavale.navire_coule('F', self.BatailleNavale.grille_def_j2))


        ## Troisème tour
        self.assertEqual(self.BatailleNavale.tir(1, 9, 9), "Raté")

        self.assertEqual(self.BatailleNavale.tir(2, 6, 9), "Touché")
        self.assertEqual(self.BatailleNavale.tir(2, 7, 9), "Touché")
        self.assertEqual(self.BatailleNavale.tir(2, 8, 9), "Touché, Coulé")

        # Fin du tour de jeu
        # On fait une assertion sur les grilles

        self.assertEqual(self.BatailleNavale.grille_def_j1, [['0', '0', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', 'X', 'X', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'X', '-', 'X', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'X', '-', 'X', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'X', '-', 'X', '-'],
                                                        ['X', 'X', 'X', 'X', '-', '-', 'X', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'X', '-', '-', '-']])

        self.assertEqual(self.BatailleNavale.grille_def_j2, [['0', '0', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', 'S', '-', 'X', 'X', 'X', 'X', 'X', '-', '-'],
                                                        ['-', 'S', '-', '-', '-', '-', '-', '-', 'T', 'T'],
                                                        ['-', 'S', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', 'F', '-', 'C', 'C', 'C', 'C', '-', '-'],
                                                        ['-', '-', 'F', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', 'F', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '0', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']])

        self.assertEqual(self.BatailleNavale.grille_att_j1, [['0', '0', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', 'X', 'X', 'X', 'X', 'X', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '0', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']])

        self.assertEqual(self.BatailleNavale.grille_att_j2, [['0', '0', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', 'X', 'X', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'X', '-', 'X', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'X', '-', 'X', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'X', '-', 'X', '-'],
                                                        ['X', 'X', 'X', 'X', '-', '-', 'X', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'X', '-', '-', '-']])

        # Tests pour verifier si les navires ont coulés.
        # pour le joueur 1
        self.assertTrue(self.BatailleNavale.navire_coule('T', self.BatailleNavale.grille_def_j1))
        self.assertTrue(self.BatailleNavale.navire_coule('S', self.BatailleNavale.grille_def_j1))
        self.assertTrue(self.BatailleNavale.navire_coule('C', self.BatailleNavale.grille_def_j1))
        self.assertTrue(self.BatailleNavale.navire_coule('P', self.BatailleNavale.grille_def_j1))
        self.assertTrue(self.BatailleNavale.navire_coule('F', self.BatailleNavale.grille_def_j1))

        # pour le joueur 2
        self.assertTrue(self.BatailleNavale.navire_coule('P', self.BatailleNavale.grille_def_j2))
        self.assertFalse(self.BatailleNavale.navire_coule('S', self.BatailleNavale.grille_def_j2))
        self.assertFalse(self.BatailleNavale.navire_coule('C', self.BatailleNavale.grille_def_j2))
        self.assertFalse(self.BatailleNavale.navire_coule('T', self.BatailleNavale.grille_def_j2))
        self.assertFalse(self.BatailleNavale.navire_coule('F', self.BatailleNavale.grille_def_j2))

        # Derniere assertion sur la fonction de fin  de partie
        self.assertTrue(self.BatailleNavale.tous_les_navires_ont_coule(self.BatailleNavale.grille_def_j1))
