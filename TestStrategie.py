# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:27:06 2024

@author: courte12u
"""

from Grille import Grille
from Strategie import Strategie
from CreationStrategie import CreationStrategie
import unittest

class TestStrategie(unittest.TestCase):

    def setUp(self):

        #création de la grille
        self.grille_test = Grille(10,10)
        self.grille_test.creation_grille_de_jeu()

        #informations stratégie
        self.inputs_strategie = {'Torpilleur': [2, 4, 9, 'O'], 'Sous-marin': [3, 3, 6, 'S'], 'Frégate': [3, 6, 9, 'S'], 'Porte-avions': [5, 10, 7, 'N']}

        #informations sur les navires
        self.navires = {'Torpilleur': [2, 'T'], 'Sous-marin':[3, 'S'], 'Frégate':[3, 'F'], 'Cuirassé':[4, 'C'], 'Porte-avions':[5, 'P']}
        
        #création d'une stratégie
        self.strategie = Strategie(self.inputs_strategie, self.navires, self.grille_test)

    def test_initialisation(self):
        #test d'initialisation de la classe Strategie

        self.assertEqual(self.strategie.informations, self.inputs_strategie)
        self.assertEqual(self.strategie.navires, self.navires)
        self.assertEqual(self.strategie.instance_grille, self.grille_test)
        
    
    def test_placement_navires_joueur_valide(self):
        #placement d'un navire valide pour une place valide
        # je tente de placer un cuirassé
        self.grille_test.grille[2][1] = 'C'
        self.grille_test.grille[2][2] = 'C'
        self.grille_test.grille[2][3] = 'C'
        self.grille_test.grille[2][4] = 'C'

        # Vérification de la méthode placement_navires_joueur
        self.assertTrue(self.strategie.placement_navires_joueur(self.grille_test.grille, self.inputs_strategie))
        

    def test_placement_navires_joueur_invalide_conflit(self):
        #simuler un conflit de placement ente le cuirassé et sous marin
        self.grille_test.grille[2][2] = 'C'  # Le navire 'Cuirassé' est déjà placé à (2, 2)
        self.grille_test.grille[2][3] = 'C'
        self.grille_test.grille[2][4] = 'C'
        self.grille_test.grille[2][5] = 'C'
    
        
        # Vérification du retour False pour un placement invalide
        self.assertFalse(self.strategie.placement_navires_joueur(self.grille_test.grille, self.inputs_strategie))
        

    """
    def test_verifier_validite_valide(self):
        Test de la méthode verifier_validite pour une stratégie valide.
        # Simuler un placement valide
        self.grille_mock.grille[2][2] = 'C'  # Position de départ du navire 'Cuirassé'
        self.grille_mock.grille[3][2] = 'C'  # Continuation du navire 'Cuirassé'
        self.grille_mock.grille[4][2] = 'C'  # Continuation du navire 'Cuirassé'
        self.grille_mock.grille[5][2] = 'C'  # Continuation du navire 'Cuirassé'

        # Vérification que la stratégie est valide
        self.assertTrue(self.strategie.verifier_validite())

    def test_verifier_validite_invalide(self):
        Test de la méthode verifier_validite pour une stratégie invalide.
        # Simuler un placement invalide (chevauchement de navires)
        self.grille_mock.grille[2][2] = 'C'  # Placement du navire 'Cuirassé'
        self.grille_mock.grille[3][2] = 'T'  # Le navire 'Contre-torpilleur' chevauche le navire 'Cuirassé'
        
        # Vérification que la stratégie est invalide
        self.assertFalse(self.strategie.verifier_validite())

    def test_affichage_strategie_valide(self):
        Test de la méthode affichage_strategie pour une stratégie valide.
        # Simuler un placement valide des navires
        self.grille_mock.grille[2][2] = 'C'
        self.grille_mock.grille[3][2] = 'C'
        self.grille_mock.grille[4][2] = 'C'
        self.grille_mock.grille[5][2] = 'C'

        # Vérification que la fonction d'affichage de la grille est appelée
        with self.assertLogs(level='INFO') as log:
            self.strategie.affichage_strategie()
            self.assertIn('Stratégie valide', log.output)

    def test_affichage_strategie_invalide(self):
        Test de la méthode affichage_strategie pour une stratégie invalide.
        # Simuler un conflit de placement
        self.grille_mock.grille[2][2] = 'C'
        self.grille_mock.grille[3][2] = 'T'

        # Vérification que la fonction d'affichage indique que la stratégie est invalide
        with self.assertLogs(level='INFO') as log:
            self.strategie.affichage_strategie()
            self.assertIn('Stratégie non valide', log.output)

    def test_comparaison_strategie(self):
        Test de la méthode __eq__ pour comparer deux stratégies.
        # Création d'une autre instance de Strategie avec les mêmes informations
        autre_strategie = Strategie(self.inputs_strategie, self.navires, self.grille_mock)

        # Vérification que les stratégies sont égales
        self.assertTrue(self.strategie == autre_strategie)

        # Modifions légèrement les informations pour tester une comparaison différente
        autre_strategie.informations['Cuirassé'] = [4, 2, 3, 'E']
        self.assertFalse(self.strategie == autre_strategie)
    
    """

if __name__ == '__main__':
    unittest.main()


 
