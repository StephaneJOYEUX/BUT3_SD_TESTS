# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:27:06 2024

@author: courte12u
"""

from Grille import Grille
from Startegie import Strategie
from CreationStrategie import CreationStrategie
import unittest

class MyTestClasseStrategie(unittest.TestCase):

    def test_classe_strategie(self):
        # Vérification que la stratégie à bien été instanciée et que les méthodes de classes fonctionnent
        self.assertEqual(self.strategie_j1.informations, {'Torpilleur': [2, 4, 9, 'O'], 'Sous-marin': [3, 3, 6, 'S'], 'Frégate': [3, 6, 9, 'S'],
                              'Cuirassé': [4, 9, 1, 'E'], 'Porte-avions': [5, 10, 7, 'N']})
        self.assertEqual(self.strategie_j1.instance_grille.grille, [['-','-','-', '-','-','-','-','-','-', '-'],
                                                                    ['-','-','-', '-','-','-','-','-','-', '-'],
                                                                    ['-', '-','-', '-','-','S','-','-', '-', '-'],
                                                                    ['-', '-','-', '-','-','S','-','T','T', '-'],
                                                                    ['-', '-','-', '-','-','S','-', '-', '-', '-'],
                                                                    ['-','-','-','-','-','-','P','-','F', '-'],
                                                                    ['-','-','-','-','-','-','P','-','F', '-'],
                                                                    ['-','-','-','-','-','-','P','-','F', '-'],
                                                                    ['C','C','C', 'C','-','-','P','-','-', '-'],
                                                                    ['-','-','-', '-','-','-','P','-','-', '-']])
