import unittest
from Strategie import Strategie
from Grille import Grille


class TestStrategie(unittest.TestCase):

    def setUp(self):
        self.grille = Grille(10, 10)
        self.grille.creation_grille_de_jeu()
        # stratégie
        self.inputs_strategie = {
            'Torpilleur': [2, 4, 9, 'O'],
            'Sous-marin': [3, 3, 6, 'S'],
            'Frégate': [3, 6, 9, 'S'],
            'Porte-avions': [5, 10, 7, 'N']
        }
        # navires
        self.navires = {
            'Torpilleur': [2, 'T'],
            'Sous-marin': [3, 'S'],
            'Frégate': [3, 'F'],
            'Cuirassé': [4, 'C'],
            'Porte-avions': [5, 'P']
        }
        # Création d'une stratégie
        self.strategie = Strategie(self.inputs_strategie, self.navires, self.grille)

    def test_initialisation(self):
        self.assertEqual(self.strategie.informations, self.inputs_strategie)
        self.assertEqual(self.strategie.navires, self.navires)
        self.assertEqual(self.strategie.instance_grille, self.grille)

    def test_placement_joueur_valide(self):
        self.assertTrue(self.strategie.placement_navires_joueur(self.grille.plateau, self.inputs_strategie))

    def test_placement_joueur_invalide(self):
        self.grille.plateau[3][5] = 'F'
        self.assertFalse(self.strategie.placement_navires_joueur(self.grille.plateau, self.inputs_strategie))

    def test_placement_navire_valide(self):
        navire = 'Sous-marin'
        self.assertTrue(self.strategie.placement_un_navire(self.grille.plateau, self.inputs_strategie, navire))

    def test_placement_navire_invalide(self):
        navire = 'Porte-avions'
        inputs_invalides = {'Porte-avions': [5, 10, 10, 'E']}  # Placement hors limites
        self.assertFalse(self.strategie.placement_un_navire(self.grille.plateau, inputs_invalides, navire))

    def test_verifier_valide(self):
        self.assertTrue(self.strategie.verifier_validite())

    def test_verifier_invalide(self):
        self.grille.plateau[3][5] = 'F'
        self.assertFalse(self.strategie.verifier_validite())

    def test_affichage_valide(self):
        result = self.strategie.affichage_strategie()
        self.assertTrue(result)

    def test_affichage_invalide(self):
        inputs_invalides = {'Sous-marin': [3, 11, 11, 'N']}  # Placement hors limites
        strategie_invalide = Strategie(inputs_invalides, self.navires, self.grille)
        result = strategie_invalide.affichage_strategie()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
