import unittest
from Grille import Grille
from Strategie import Strategie
from ChoixStrategie import ChoixStrategie

class MyTestChoixStrategieCase(unittest.TestCase):
    
    def setUp(self) -> None:
        # On fixe les parametres de la partie.

        self.navires = {'Torpilleur': [2, 'T'], 'Sous-marin':[3, 'S'], 'Frégate':[3, 'F'], 'Cuirassé':[4, 'C'], 'Porte-avions':[5, 'P']}
    
    def test_classe_choix_strategie(self):
        # On test si la classe a bien permis la lecture du fichier de sauvegarde.
        # Cela couvre l'option "choisir" de l'utilisateur.
        # Pour ce qui est du choix "créer", le test précédent le couvre.

        # 1er test : verifier que le fichier de sauvegarde est lu correctement avec la construction de l'instance strategie
        self.assertIsInstance(ChoixStrategie('joueur_test', self.navires, Grille(10,10), test = True).referentiel[0], Strategie)

        # 2nd test : verifions que la première strategie sauvegardée correspond au résultat attendu.
        # Ce 2nd test permet de tester aussi la methode __eq__ de la classe Strategie.
        self.assertEqual(ChoixStrategie('joueur_test', self.navires, Grille(10,10), test = True).referentiel[0],Strategie({'Torpilleur': [2, 1, 1, 'S'],
                                                                                                                 'Sous-marin': [3, 5, 1, 'S'],
                                                                                                                 'Frégate': [3, 3, 5, 'E'],
                                                                                                                 'Cuirassé': [4, 5, 6, 'O'],
                                                                                                                 'Porte-avions': [5, 9, 9, 'N']}, self.navires))
        
        