import unittest
from Grille import Grille
from Strategie import Strategie
from BatailleNavale import BatailleNavale


class TestBatailleNavale(unittest.TestCase):

    def setUp(self):
        # Initialisation des objets nécessaires
        self.navires = {'Torpilleur': [2, 'T'], 'Sous-marin':[3, 'S'], 'Frégate':[3, 'F'], 'Cuirassé':[4, 'C'], 'Porte-avions':[5, 'P']}

        self.strategie_j1 = Strategie({'Torpilleur': [2, 4, 9, 'O'], 'Sous-marin': [3, 3, 6, 'S'], 'Frégate': [3, 6, 9, 'S'],
                              'Cuirassé': [4, 9, 1, 'E'], 'Porte-avions': [5, 10, 7, 'N']}, self.navires,
                                 Grille(10, 10))

        self.strategie_j2 = Strategie({'Torpilleur': [2, 3, 9, 'E'], 'Sous-marin': [3, 2, 2, 'S'], 'Frégate': [3, 5, 3, 'S'],
                              'Cuirassé': [4, 5, 8, 'O'], 'Porte-avions': [5, 2, 4, 'E']}, self.navires,
                                 Grille(10, 10))

        self.bataille_navale = BatailleNavale(self.navires, self.strategie_j1, self.strategie_j2, test = True)

    def test_initialisation(self):
        self.assertEqual(self.bataille_navale.pseudo_j1, "Ordinateur 1")
        self.assertEqual(self.bataille_navale.pseudo_j2, "Ordinateur 2")
        self.assertEqual(self.bataille_navale.navires, self.navires)

        self.assertEqual(len(self.bataille_navale.grille_def_j1), 10)
        self.assertEqual(len(self.bataille_navale.grille_def_j2), 10)
        self.assertEqual(len(self.bataille_navale.grille_att_j1), 10)
        self.assertEqual(len(self.bataille_navale.grille_att_j2), 10)

    def test_instance(self):
        strategie_j1 = self.bataille_navale.instansiation_strategie(self.strategie_j1)
        strategie_j2 = self.bataille_navale.instansiation_strategie(self.strategie_j2)

        self.assertEqual(strategie_j1, self.strategie_j1)
        self.assertEqual(strategie_j2, self.strategie_j2)

    def test_grille(self):
        self.assertEqual(self.bataille_navale.grille_def_j1, [['-','-','-', '-','-','-','-','-','-', '-'],
                                                        ['-','-','-', '-','-','-','-','-','-', '-'],
                                                        ['-', '-','-', '-','-','S','-','-', '-', '-'],
                                                        ['-', '-','-', '-','-','S','-','T','T', '-'],
                                                        ['-', '-','-', '-','-','S','-', '-', '-', '-'],
                                                        ['-','-','-','-','-','-','P','-','F', '-'],
                                                        ['-','-','-','-','-','-','P','-','F', '-'],
                                                        ['-','-','-','-','-','-','P','-','F', '-'],
                                                        ['C','C','C', 'C','-','-','P','-','-', '-'],
                                                        ['-','-','-', '-','-','-','P','-','-', '-']])

        self.assertEqual(self.bataille_navale.grille_def_j2, [['-','-','-', '-','-','-', '-','-','-', '-'],
                                                        ['-', 'S', '-', 'P', 'P', 'P', 'P', 'P', '-', '-'],
                                                        ['-', 'S','-', '-','-','-', '-','-', 'T', 'T'],
                                                        ['-', 'S','-', '-','-','-', '-','-','-', '-'],
                                                        ['-','-','F', '-', 'C', 'C', 'C', 'C', '-', '-'],
                                                        ['-','-','F','-','-','-', '-','-','-', '-'],
                                                        ['-','-','F','-','-','-', '-','-','-', '-'],
                                                        ['-','-','-', '-','-','-', '-','-','-', '-'],
                                                        ['-','-','-', '-','-','-', '-','-','-', '-'],
                                                        ['-','-','-', '-','-','-', '-','-','-', '-']])

    def test_tir_rate(self):
        self.assertEqual(self.bataille_navale.tir(1, 1, 1), "Raté")

    def test_tir_reussi(self):
        self.assertEqual(self.bataille_navale.tir(2, 3, 6), "Touché")

    def test_touche_coule(self):
        self.bataille_navale.tir(2, 3, 6)
        self.bataille_navale.tir(2, 4, 6)
        self.assertEqual(self.bataille_navale.tir(2, 5, 6), "Touché, Coulé")
        self.assertEqual(self.bataille_navale.grille_def_j1, [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', 'T', 'T', '-'],
                                                        ['-', '-', '-', '-', '-', 'X', '-', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'P', '-', 'F', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'P', '-', 'F', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'P', '-', 'F', '-'],
                                                        ['C', 'C', 'C', 'C', '-', '-', 'P', '-', '-', '-'],
                                                        ['-', '-', '-', '-', '-', '-', 'P', '-', '-', '-']])

    def test_navire_coule(self):
        self.assertFalse(self.bataille_navale.navire_coule("S", self.bataille_navale.grille_def_j1))
        self.bataille_navale.tir(2, 3, 6)
        self.bataille_navale.tir(2, 4, 6)
        self.bataille_navale.tir(2, 5, 6)
        self.assertTrue(self.bataille_navale.navire_coule("S", self.bataille_navale.grille_def_j1))

    def test_tous_les_navires_ont_coule(self):
        self.assertFalse(self.bataille_navale.tous_les_navires_ont_coule(self.bataille_navale.grille_def_j1))
        #S
        self.bataille_navale.tir(2, 3, 6)
        self.bataille_navale.tir(2, 4, 6)
        self.bataille_navale.tir(2, 5, 6)
        #T
        self.bataille_navale.tir(2, 4, 8)
        self.bataille_navale.tir(2, 4, 9)
        #P
        self.bataille_navale.tir(2, 6, 7)
        self.bataille_navale.tir(2, 7, 7)
        self.bataille_navale.tir(2, 8, 7)
        self.bataille_navale.tir(2, 9, 7)
        self.bataille_navale.tir(2, 10, 7)
        #F
        self.bataille_navale.tir(2, 6, 9)
        self.bataille_navale.tir(2, 7, 9)
        self.bataille_navale.tir(2, 8, 9)
        #C
        self.bataille_navale.tir(2, 9, 1)
        self.bataille_navale.tir(2, 9, 2)
        self.bataille_navale.tir(2, 9, 3)
        self.bataille_navale.tir(2, 9, 4)
        self.assertTrue(self.bataille_navale.tous_les_navires_ont_coule(self.bataille_navale.grille_def_j1))





if __name__ == "__main__":
    unittest.main()
