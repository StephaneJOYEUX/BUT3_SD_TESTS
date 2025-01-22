import unittest
from ChoixStrategie import ChoixStrategie
from Grille import Grille
from Strategie import Strategie
from CreationStrategie import CreationStrategie

class TestChoixStrategie(unittest.TestCase):
    def setUp(self):
        """
        Initialisation des tests. Création d'une grille et de navires pour les tests.
        """
        self.navires = {
            "Porte-avions": (5, "P"),
            "Cuirassé": (4, "C"),
            "Sous-marin": (3, "S"),
            "Frégate": (3, "F"),
            "Torpilleur": (2, "T")
        }
        self.grille = Grille(10, 10)

        # Nettoyage ou création du fichier de sauvegarde vide avant chaque test
        with open('sauvegardes_strategies.txt', 'w', encoding='UTF-8') as f:
            f.write("")

    def test_choisir_strategie_existante(self):
        """
        Teste la sélection d'une stratégie existante dans le référentiel.
        """
        # Création de stratégies fictives
        strategie1 = Strategie({"Porte-avions": [5, 1, 1, "E"]}, self.navires)
        strategie2 = Strategie({"Cuirassé": [4, 5, 5, "N"]}, self.navires)

        choix_strategie = ChoixStrategie("Joueur1", self.navires, self.grille, test=True)
        choix_strategie.referentiel = [strategie1, strategie2]

        # Simule la sélection d'une stratégie par son index
        choix_strategie.strategie = choix_strategie.referentiel[1]

        self.assertEqual(choix_strategie.strategie, strategie2)
        self.assertNotEqual(choix_strategie.strategie, strategie1)

    def test_lire_fichier_sauvegarde(self):
        """
        Teste la lecture des stratégies sauvegardées dans le fichier.
        """
        # Écriture dans le fichier de sauvegarde
        with open('sauvegardes_strategies.txt', 'w', encoding='UTF-8') as f:
            f.write('{"Porte-avions": [1, 1, 1, "E"]}\n')
            f.write('{"Croiseur": [4, 5, 5, "N"]}\n')

        choix_strategie = ChoixStrategie("Joueur1", self.navires, self.grille, test=True)

        # Vérification du contenu du référentiel
        self.assertEqual(len(choix_strategie.referentiel), 2)
        self.assertEqual(choix_strategie.referentiel[0].informations, {"Porte-avions": [1, 1, 1, "E"]})
        self.assertEqual(choix_strategie.referentiel[1].informations, {"Croiseur": [4, 5, 5, "N"]})

    def test_ecrire_fichier_sauvegarde(self):
        """
        Teste l'écriture des stratégies dans le fichier de sauvegarde.
        """
        choix_strategie = ChoixStrategie("Joueur1", self.navires, self.grille, test=True)

        # Ajout d'une stratégie fictive dans le référentiel
        strategie = Strategie({"Porte-avions": [5, 1, 1, "E"]}, self.navires)
        choix_strategie.referentiel.append(strategie)
        choix_strategie.ecrire_fichier_sauvegarde()

        # Vérification du contenu du fichier de sauvegarde
        with open('sauvegardes_strategies.txt', 'r', encoding='UTF-8') as f:
            lignes = f.readlines()

        self.assertEqual(len(lignes), 1)
        self.assertEqual(lignes[0].strip(), "{'Porte-avions': [5, 1, 1, 'E']}")

    def test_valider_input_utilisateur(self):
        """
        Teste la méthode valider_input_utilisateur pour vérifier les entrées utilisateur.
        """
        choix_strategie = ChoixStrategie("Joueur1", self.navires, self.grille, test=True)

        # Test en entrée directe pour simuler des cas valides et non valides
        choix_valide = choix_strategie.valider_input_utilisateur("Test choix", "oui", "non")
        self.assertIn(choix_valide, ["oui", "non"])

if __name__ == "__main__":
    unittest.main()