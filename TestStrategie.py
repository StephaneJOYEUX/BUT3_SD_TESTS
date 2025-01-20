import unittest
from Grille import *
from Strategie import *


class TestStrategie(unittest.TestCase):

    def setUp(self):
        self.grille = Grille(10, 10)
        self.grille.creation_grille_de_jeu()

        self.navires = {
            'porte_avion': [5, 'P'],
            'croiseur': [4, 'C'],
            'contre_torpilleur': [3, 'T'],
            'sous_marin': [3, 'S'],
            'torpilleur': [2, 'D']
        }

    ''' à corriger
    def test_verifier_valide(self):
        strategie_valide = {
            'porte_avion': [5, 1, 1, 'E'],
            'croiseur': [4, 3, 1, 'S'],
            'contre_torpilleur': [3, 5, 5, 'E'],
            'sous_marin': [3, 7, 7, 'N'],
            'torpilleur': [2, 9, 9, 'W']
        }
        strategie = Strategie(strategie_valide, self.navires, self.grille)
        self.assertTrue(strategie.verifier_validite())'''

    def test_verifier_chevauchement(self):
        strategie_chevauchement = {
            'porte_avion': [5, 1, 1, 'E'],
            'croiseur': [4, 1, 3, 'S']
        }
        strategie = Strategie(strategie_chevauchement, self.navires, self.grille)
        self.assertFalse(strategie.verifier_validite())

    def test_placement_joueur_valide(self):
        strategie_valide = {
            'porte_avion': [5, 1, 1, 'E'],
            'croiseur': [4, 3, 1, 'S']
        }
        strategie = Strategie(strategie_valide, self.navires, self.grille)
        self.assertTrue(strategie.placement_navires_joueur(self.grille.plateau, strategie_valide))

    def test_placement_navire_valide(self):
        strategie = {'porte_avion': [5, 1, 1, 'E']}
        strategie_instance = Strategie(strategie, self.navires, self.grille)
        self.assertTrue(strategie_instance.placement_un_navire(self.grille.plateau, strategie, 'porte_avion'))

    def test_placement_navire_hors_grille(self):
        strategie = {'porte_avion': [5, 1, 8, 'E']}  # Position hors grille
        strategie_instance = Strategie(strategie, self.navires, self.grille)
        self.assertFalse(strategie_instance.placement_un_navire(self.grille.plateau, strategie, 'porte_avion'))

    def test_placement_navire_chevauchement(self):
        strategie = {
            'porte_avion': [5, 1, 1, 'E'],
            'croiseur': [4, 1, 3, 'S']
        }
        strategie_instance = Strategie(strategie, self.navires, self.grille)
        strategie_instance.placement_un_navire(self.grille.plateau, strategie, 'porte_avion')
        self.assertFalse(strategie_instance.placement_un_navire(self.grille.plateau, strategie, 'croiseur'))

    def test_strategie_valide(self):
        strategie_valide = {
            'porte_avion': [5, 1, 1, 'E']
        }
        strategie_instance = Strategie(strategie_valide, self.navires, self.grille)
        self.assertTrue(strategie_instance.verifier_validite())
        strategie_instance.affichage_strategie()


if __name__ == '__main__':
    unittest.main()
