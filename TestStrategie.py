import unittest
from Grille import Grille
from Strategie import Strategie

class MyTestStrategieCase(unittest.TestCase):
    
    def setUp(self) -> None:
        # On fixe les parametres de la partie.
        
        self.navires = {'Torpilleur': [2, 'T'], 'Sous-marin':[3, 'S'], 'Frégate':[3, 'F'], 'Cuirassé':[4, 'C'], 'Porte-avions':[5, 'P']}
        
        self.strategie_j1 = Strategie({'Torpilleur': [2, 4, 9, 'O'], 'Sous-marin': [3, 3, 6, 'S'], 'Frégate': [3, 6, 9, 'S'],
                              'Cuirassé': [4, 9, 1, 'E'], 'Porte-avions': [5, 10, 7, 'N']}, self.navires,
                                 Grille(10, 10))

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