import unittest
from Grille import Grille
from Strategie import Strategie

class TestStrategie(unittest.TestCase):

    def setUp(self):
        # Préparation des données de test communes à plusieurs tests
        self.navires = {
            "Porte-avions": [5, "P"],
            "Cuirassé": [4, "C"],
            "Sous-marin": [3, "S"],
            "Frégate": [3, "F"],
            "Torpilleur": [2, "T"]
        }

        self.strategie_valide = {
            "Porte-avions": [5, 1, 1, "E"],
            "Cuirassé": [4, 3, 3, "S"],
            "Sous-marin": [3, 5, 5, "N"],
            "Frégate": [3, 7, 7, "N"],
            "Torpilleur": [2, 9, 9, "W"]
        }

        self.strategie_invalide = {
            "Porte-avions": [5, 1, 1, "E"],
            "Cuirassé": [4, 1, 1, "S"]  # Croiseur commence à la même position que le Porte-avions
        }

        self.strategie_j1 = Strategie({'Torpilleur': [2, 4, 9, 'O'], 'Sous-marin': [3, 3, 6, 'S'], 'Frégate': [3, 6, 9, 'S'],
                              'Cuirassé': [4, 9, 1, 'E'], 'Porte-avions': [5, 10, 7, 'N']}, self.navires,
                                 Grille(10, 10))

    def test_initialisation(self):
        grille = Grille(10, 10)
        strategie = Strategie(self.strategie_valide, self.navires, grille)
        
        self.assertIsNotNone(strategie.instance_grille)
        self.assertEqual(strategie.informations, self.strategie_valide)

    def test_placement_navires_valide(self):
        grille = Grille(10, 10)
        strategie = Strategie(self.strategie_valide, self.navires, grille)
        
        self.assertTrue(strategie.verifier_validite())

    def test_placement_navires_invalide(self):
        grille = Grille(10, 10)
        strategie = Strategie(self.strategie_invalide, self.navires, grille)

        self.assertFalse(strategie.verifier_validite())

    def test_placement_un_navire_valide(self):
        grille = Grille(10, 10)
        grille.creation_grille()
        strategie = Strategie({}, self.navires, grille)
        
        resultat = strategie.placement_un_navire(grille.grille, self.strategie_valide, "Porte-avions")
        self.assertTrue(resultat)
        self.assertEqual(grille.grille[0][0], "P")
        self.assertEqual(grille.grille[0][4], "P")

    def test_placement_un_navire_hors_grille(self):
        grille = Grille(5, 5)
        grille.creation_grille()
        strategie = Strategie({}, self.navires, grille)

        strategie_hors_grille = {
            "Porte-avions": [5, 1, 1, "N"]  # Sortie de la grille
        }
        resultat = strategie.placement_un_navire(grille.grille, strategie_hors_grille, "Porte-avions")
        self.assertFalse(resultat)

    def test_affichage_strategie(self):
        grille = Grille(10, 10)
        strategie = Strategie(self.strategie_valide, self.navires, grille)

        # Vérifier que la méthode ne lève pas d'exception
        try:
            strategie.affichage_strategie()
        except Exception as e:
            self.fail(f"affichage_strategie a levé une exception: {e}")
            
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

if __name__ == '__main__': 
    unittest.main()