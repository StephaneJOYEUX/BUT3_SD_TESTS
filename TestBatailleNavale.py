import unittest
from BatailleNavale import BatailleNavale
from Strategie import Strategie
from Grille import Grille

class TestBatailleNavale(unittest.TestCase):

    def setUp(self):
        # Initialisation des données pour les tests
        self.navires = {
            "Torpilleur": [2, "T"],
            "Sous-marin": [3, "S"],
            "Frégate": [3, "F"],
            "Cuirassé": [4, "C"],
            "Porte-avions": [5, "P"]
        }
        
        # Stratégies fictives pour les tests
        self.strategie_j1 = Strategie(
            {
                "Torpilleur": [2, 1, 1, "E"],
                "Sous-marin": [3, 3, 3, "S"],
                "Frégate": [3, 5, 5, "N"],
                "Cuirassé": [4, 7, 7, "W"],
                "Porte-avions": [5, 9, 9, "N"]
            },
            self.navires
        )
        self.strategie_j2 = Strategie(
            {
                "Torpilleur": [2, 2, 2, "E"],
                "Sous-marin": [3, 4, 4, "S"],
                "Frégate": [3, 6, 6, "N"],
                "Cuirassé": [4, 8, 8, "W"],
                "Porte-avions": [5, 10, 10, "N"]
            },
            self.navires
        )
        self.grille = Grille(10, 10)

    def test_initialisation(self):
        # Teste si la classe s'initialise correctement avec les grilles et stratégies
        partie = BatailleNavale(self.navires, self.strategie_j1, self.strategie_j2, self.grille, test=True)
        self.assertEqual(len(partie.grille_def_j1), 10)
        self.assertEqual(len(partie.grille_def_j2), 10)
        self.assertEqual(len(partie.grille_att_j1), 10)
        self.assertEqual(len(partie.grille_att_j2), 10)

    def test_tir_rate(self):
        # Teste un tir qui rate
        partie = BatailleNavale(self.navires, self.strategie_j1, self.strategie_j2, self.grille, test=True)
        resultat = partie.tir(1, 1, 1)  # La case (1, 1) est vide
        self.assertEqual(resultat, "Raté")

    def test_tir_touche(self):
        # Teste un tir qui touche
        partie = BatailleNavale(self.navires, self.strategie_j1, self.strategie_j2, self.grille, test=True)
        resultat = partie.tir(1, 4, 4)  # La case (3, 3) contient un navire
        self.assertEqual(resultat, "Touché")

    def test_tir_touche_coule(self):
        # Teste un tir qui coule un navire
        partie = BatailleNavale(self.navires, self.strategie_j1, self.strategie_j2, self.grille, test=True)
        partie.tir(1, 4, 4)  # Touche le sous-marin
        partie.tir(1, 5, 4)  # Touche le sous-marin
        resultat = partie.tir(1, 6, 4)  # Coule le sous-marin
        self.assertEqual(resultat, "Touché, Coulé")

    def test_victoire(self):
        # Teste la condition de victoire
        partie = BatailleNavale(self.navires, self.strategie_j1, self.strategie_j2, self.grille, test=True)
        # Couler tous les navires de J2
        for navire, coords in self.strategie_j2.informations.items():
            taille, x, y, direction = coords
            for i in range(taille):
                if direction == "E":
                    partie.tir(1, x, y + i)
                elif direction == "S":
                    partie.tir(1, x + i, y)
                elif direction == "W":
                    partie.tir(1, x, y - i)
                elif direction == "N":
                    partie.tir(1, x - i, y)
        self.assertTrue(partie.tous_les_navires_ont_coule(partie.grille_def_j2))

    def test_play_ordinateur(self):
        # Teste si l'ordinateur peut jouer un tour
        partie = BatailleNavale(self.navires, self.strategie_j1, self.strategie_j2, self.grille, test=True)
        victoire_ordinateur = partie.play_ordinateur()
        self.assertIn(victoire_ordinateur, [True, False])

if __name__ == "__main__":
    unittest.main()