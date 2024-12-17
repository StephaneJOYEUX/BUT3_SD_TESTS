import unittest
from Grille import Grille
from Strategie import Strategie
from CreationStrategie import CreationStrategie

class MyTestCreationStrategieCase(unittest.TestCase):
    
    def setUp(self) -> None:
        # On fixe les parametres de la partie.

        self.navires = {'Torpilleur': [2, 'T'], 'Sous-marin':[3, 'S'], 'Frégate':[3, 'F'], 'Cuirassé':[4, 'C'], 'Porte-avions':[5, 'P']}

    def test_classe_creation_strategie(self):
        # On teste si la classe a bien permis la création d'une stratégie -> test de la bonne instanciation.
        # Utilisation d'un booléen de test pour court-circuiter les inputs.
        self.assertIsInstance(CreationStrategie(self.navires,Grille(10, 10), test = True).get_instance_strategie(), Strategie)