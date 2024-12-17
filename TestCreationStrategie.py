# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:27:55 2024

@author: courte12u
"""

from Grille import Grille
from Startegie import Strategie
from CreationStrategie import CreationStrategie
import unittest

class MyTestCreationStrategieCase(unittest.TestCase):

    def test_classe_creation_strategie(self):
        # On teste si la classe a bien permis la création d'une stratégie -> test de la bonne instanciation.
        # Utilisation d'un booléen de test pour court-circuiter les inputs.
        self.assertIsInstance(CreationStrategie(self.navires,Grille(10, 10), test = True).get_instance_strategie(), Strategie)