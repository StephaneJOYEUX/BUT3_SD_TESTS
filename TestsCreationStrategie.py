import unittest
from Grille import Grille  
from CreationStrategie import CreationStrategie  

class TestCreationStrategie(unittest.TestCase):

    def setUp(self):
        """Initialisation avant chaque test. Crée une grille et des navires de test."""
        self.navires_test = {
            'Torpilleur': [2, 4, 9, 'O'],
            'Sous-marin': [3, 3, 6, 'S'],
            'Frégate': [3, 6, 9, 'S'],
            'Cuirassé': [4, 9, 1, 'E'],
            'Porte-avions': [5, 10, 7, 'N']
        }
        self.grille_test = Grille(10, 10)  # Grille de 10x10 pour les tests

    def test_creation_strategie_validite(self):
        """
        Test de la méthode 'creer_strategie' avec des entrées simulées valides.
        Vérifie que la stratégie est correctement créée et que les navires sont bien placés.
        """
        # Simuler les entrées pour les navires
        inputs_simules = [
            (5, 5, 'E'),
            (6, 6, 'S'),
            (7, 7, 'O'),
            (8, 8, 'N'),
            (9, 9, 'E')
        ]
        
        # Créer un objet `CreationStrategie` dans le test
        creation_strategie = CreationStrategie(
            self.navires_test,          # Dictionnaire des navires
            self.grille_test,           # L'objet Grille (instance de Grille)
            test=True,                  # L'option test
            inputs_simules=inputs_simules  # Liste des entrées simulées
        )

        # Créer la stratégie
        strategie = creation_strategie.creer_strategie()

        # Vérification que l'instance de stratégie est bien créée
        self.assertTrue(isinstance(strategie, Strategie))
        self.assertEqual(len(strategie.navires), len(self.navires_test))

if __name__ == "__main__":
    unittest.main()
