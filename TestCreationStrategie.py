import unittest
from unittest.mock import patch
from Strategie import Strategie
from CreationStrategie import CreationStrategie

class TestCreationStrategie(unittest.TestCase):

    @patch('builtins.input')
    def test_creer_strategie_valide(self, mock_input):
        mock_input.side_effect = [
            '1',  
            '1',  
            'E',  
            '3',  
            '3',  
            'S'   
        ]
        
        navires = {
            'Porte-avions': [5, 1, 1, 'E'], 
            'Sous-marin': [3, 3, 6, 'S']
        }
        
        creation_strategie = CreationStrategie(navires, test=True)
        
        instance_strategie = creation_strategie.get_instance_strategie()
        
        self.assertTrue(instance_strategie.verifier_validite())

    @patch('builtins.input')
    def test_entrées_invalides(self, mock_input):
        mock_input.side_effect = [
            '0',  
            '1',  
            'E',  
            '5',  
            '15',  
            'S'    
        ]
        
        navires = {
            'Porte-avions': [5, 1, 1, 'E'], 
            'Sous-marin': [3, 3, 6, 'S']
        }
        
        creation_strategie = CreationStrategie(navires, test=True)
        
        instance_strategie = creation_strategie.get_instance_strategie()
        
        self.assertTrue(instance_strategie.verifier_validite())

    def test_get_instance_strategie(self):
        navires = {
            'Porte-avions': [5, 1, 1, 'E'], 
            'Sous-marin': [3, 3, 6, 'S']
        }
        
        creation_strategie = CreationStrategie(navires, test=True)
        instance_strategie = creation_strategie.get_instance_strategie()
        
        self.assertIsNotNone(instance_strategie)
        self.assertIsInstance(instance_strategie, Strategie)


if __name__ == '__main__':
    unittest.main()