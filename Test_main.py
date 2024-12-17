import unittest
from main import choix_nom_et_strategie_joueur
from ChoixStrategie import ChoixStrategie
from Strategie import Strategie
from Grille import Grille
from unittest.mock import patch

class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.navires = {
            'Torpilleur': [2, 'T'], 'Sous-marin': [3, 'S'], 'Frégate': [3, 'F'],
            'Cuirassé': [4, 'C'], 'Porte-avions': [5, 'P']
        }

    @patch('builtins.input', side_effect=['Player1'])
    @patch('ChoixStrategie.ChoixStrategie.get_strategie', return_value=Strategie(
        {'Torpilleur': [2, 1, 1, 'S']}, {
            'Torpilleur': [2, 'T'], 'Sous-marin': [3, 'S']
        }, Grille(10, 10)))
    def test_choix_nom_et_strategie_joueur(self, mock_get_strategie, mock_input):
        result = choix_nom_et_strategie_joueur(1)
        self.assertEqual(result[0], 'Player1')
        self.assertIsInstance(result[1], Strategie)

if __name__ == "__main__":
    unittest.main()
