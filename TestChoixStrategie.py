import unittest
from copy import deepcopy
from ChoixStrategie import ChoixStrategie
from Strategie import Strategie
from Grille import Grille


class TestChoixStrategie(unittest.TestCase):

    def setUp(self):
        self.pseudo = "test"
        self.navires = ["sous-marin", "cuirassé", "torpilleur", "porte-avions", "frégate"]
        # Réinitialiser le fichier avant chaque test
        with open("sauvegardes_strategies.txt", "w", encoding="UTF-8") as f:
            f.write("")  # Vide le fichier
        self.strategie_choix = ChoixStrategie(self.pseudo, navires=self.navires, Grille=Grille(10, 10), test=True)

    def test_initialisation(self):
        self.assertEqual(self.strategie_choix.pseudo_joueur, self.pseudo)
        self.assertEqual(self.strategie_choix.navires, self.navires)

    def test_get_referentiel(self):
        self.assertEqual(self.strategie_choix.get_referentiel(), [])

    def test_get_strategie(self):
        self.assertIsNone(self.strategie_choix.get_strategie())

    def test_lire_fichier_sauvegarde_vide(self):
        with open("sauvegardes_strategies.txt", "w", encoding="UTF-8") as f:
            f.write("")
        self.strategie_choix.lire_fichier_sauvegarde()
        self.assertEqual(self.strategie_choix.get_referentiel(), [])

    def test_lire_fichier_sauvegarde_avec_donnees(self):
        with open("sauvegardes_strategies.txt", "w", encoding="UTF-8") as f:
            f.write("{'nom': 'strategie1', 'details': {}}\n")
        self.strategie_choix.lire_fichier_sauvegarde()
        self.assertEqual(len(self.strategie_choix.get_referentiel()), 1)
        self.assertIsInstance(self.strategie_choix.get_referentiel()[0], Strategie)

    def test_ecrire_fichier_sauvegarde(self):
        self.strategie_choix.referentiel = [Strategie({"nom": "strategie_test", "details": {}}, self.navires)]
        self.strategie_choix.ecrire_fichier_sauvegarde()
        with open("sauvegardes_strategies.txt", "r", encoding="UTF-8") as f:
            contenu = f.read()
        self.assertIn("{'nom': 'strategie_test', 'details': {}}", contenu)


if __name__ == "__main__":
    unittest.main()
