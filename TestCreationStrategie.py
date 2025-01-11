from unittest import TestCase
from Navire import Navire
from CreationStrategie import CreationStrategie
from Grille import Grille

class TestCreationStrategie(TestCase) :
    def setUp(self):
        self.cuirasse = Navire(nom="cuirassé", taille=4)
        self.fregate = Navire(nom="frégate", taille=3)
        self.sous_marin = Navire(nom="sous-marin", taille=3)
        self.torpilleur = Navire(nom="torpilleur", taille=2)
        self.porte_avions = Navire(nom="porte-avions", taille=5)

    ## Setters & Getters (pour cette classes, il ne me semble pas qu'il existe des cas non-nominaux)
    # navires
    def test_set_navires_cas_nominal(self):
        self.navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}
        self.creation_strategie = CreationStrategie(navires=self.navires)
        self.creation_strategie.set_navires()
        self.assertEqual(self.navires, self.creation_strategie.get_navires())

    # grille
    def test_set_grille_cas_nominal(self):
        self.navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}
        self.creation_strategie = CreationStrategie(navires=self.navires)
        self.creation_strategie.set_grille()
        taille_x = 10
        taille_y = 10
        grille_test = Grille(taille_x, taille_y)
        grille_test.create()
        self.assertEqual(grille_test.plateau, self.creation_strategie.get_grille().get_plateau())
        self.assertEqual(taille_x, self.creation_strategie.derniere_ligne_grille)
        self.assertEqual(taille_y, self.creation_strategie.derniere_colonne_grille)

    ## Methodes de classe (dépend d'input utilisateurs => comment faire ?)
    # creer_strategie


    # input_donnees_placement_navire
