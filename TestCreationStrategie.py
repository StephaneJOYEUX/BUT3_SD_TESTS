import unittest
from CreationStrategie import CreationStrategie
from Strategie import Strategie
from Grille import Grille

class TestCreationStrategie(unittest.TestCase):

    def setUp(self):
        """
        Configuration de l'environnement de test avec des données de base pour les navires et une grille.
        """
        self.navires = {
            'Porte-avions': [5, 'P'],
            'Cuirassé': [4, 'C'],
            'Sous-marin': [3, 'S'],
            'Frégate': [3, 'F'],
            'Torpilleur': [2, 'T']
        }
        self.grille = Grille(10, 10)

    def test_initialisation(self):
        """
        Test de l'initialisation de CreationStrategie sans mode test.
        """
        creation = CreationStrategie(self.navires, self.grille, test=True)
        self.assertIsInstance(creation, CreationStrategie)
        self.assertEqual(creation.derniere_ligne_grille, 10)
        self.assertEqual(creation.derniere_colonne_grille, 10)

    def test_input_donnees_placement_navire(self):
        """
        Test de la méthode input_donnees_placement_navire avec des données simulées.
        """
        creation = CreationStrategie(self.navires, self.grille, test=True)

        # Mock des données
        creation.premiere_ligne_grille = 1
        creation.derniere_ligne_grille = 10
        creation.premiere_colonne_grille = 1
        creation.derniere_colonne_grille = 10

        # Simule une saisie correcte pour un navire
        navire = 'Torpilleur'
        taille = self.navires[navire][0]

        # Mock direct de la méthode (remplacer input)
        def mock_input(prompt):
            if 'ligne' in prompt:
                return '5'
            elif 'colonne' in prompt:
                return '6'
            elif 'orientation' in prompt:
                return 'E'

        creation.input = mock_input  # Mock la méthode input
        print("Pour les tests : ligne : 5, colonne : 6 et direction : E")
        result = creation.input_donnees_placement_navire(navire)
        self.assertEqual(result, [taille, 5, 6, 'E'])

    def test_creation_strategie_valide(self):
        """
        Test de la méthode creer_strategie avec une stratégie valide.
        """
        creation = CreationStrategie(self.navires, self.grille, test=True)

        # Mock des données pour simuler une stratégie valide
        creation.inputs_strategie = {
            'Torpilleur': [2, 1, 1, 'E'],
            'Sous-marin': [3, 2, 2, 'S'],
            'Cuirassé': [4, 7, 7, 'N'],
            'Porte-avions': [5, 9, 1, 'E']
        }

        # Vérifie que la stratégie est valide
        creation.instance_strategie = Strategie(creation.inputs_strategie, self.navires, self.grille)
        self.assertTrue(creation.instance_strategie.verifier_validite())

    def test_get_instance_strategie(self):
        """
        Test de la méthode get_instance_strategie pour vérifier qu'elle retourne une instance valide.
        """
        creation = CreationStrategie(self.navires, self.grille, test=True)
        instance_strategie = creation.get_instance_strategie()

        self.assertIsNotNone(instance_strategie)
        self.assertIsInstance(instance_strategie, Strategie)

    def test_classe_creation_strategie(self):
        # On teste si la classe a bien permis la création d'une stratégie -> test de la bonne instanciation.
        # Utilisation d'un booléen de test pour court-circuiter les inputs.
        self.assertIsInstance(CreationStrategie(self.navires,Grille(10, 10), test = True).get_instance_strategie(), Strategie)

if __name__ == '__main__':
    unittest.main()