import unittest
from ChoixStrategie import ChoixStrategie
from Grille import Grille
from Strategie import Strategie

class TestChoixStrategie(unittest.TestCase):
    def setUp(self) -> None:
        self.navires = {
            'Torpilleur': [2, 'T'], 'Sous-marin': [3, 'S'], 'Frégate': [3, 'F'],
            'Cuirassé': [4, 'C'], 'Porte-avions': [5, 'P']
        }
        self.grille = Grille(10, 10)
        # Création d'un fichier de sauvegarde temporaire
        with open("sauvegardes_strategies.txt", "w", encoding="UTF-8") as file:
            file.write("{\'Torpilleur\': [2, 1, 1, 'S'], \'Sous-marin\': [3, 3, 3, 'E']}\n")
        
    def tearDown(self) -> None:
        # Nettoyage du fichier temporaire
        open("sauvegardes_strategies.txt", "w").close()

    def test_lire_fichier_sauvegarde(self):
        choix = ChoixStrategie("joueur_test", self.navires, self.grille, test=True)
        referentiel = choix.get_referentiel()
        self.assertEqual(len(referentiel), 1)
        self.assertIsInstance(referentiel[0], Strategie)

    def test_ecrire_fichier_sauvegarde(self):
        choix = ChoixStrategie("joueur_test", self.navires, self.grille, test=True)
        nouvelle_strategie = Strategie({'Frégate': [3, 2, 2, 'N']}, self.navires)
        choix.referentiel.append(nouvelle_strategie)
        choix.ecrire_fichier_sauvegarde()
        
        with open("sauvegardes_strategies.txt", "r", encoding="UTF-8") as file:
            lignes = file.readlines()
        self.assertEqual(len(lignes), 2)
        self.assertIn("{'Frégate': [3, 2, 2, 'N']}\n", lignes)

    def test_get_strategie(self):
        choix = ChoixStrategie("joueur_test", self.navires, self.grille, test=True)
        strategie = choix.get_strategie()
        self.assertIsNone(strategie)  # Aucune stratégie n'est encore définie

if __name__ == "__main__":
    unittest.main()
