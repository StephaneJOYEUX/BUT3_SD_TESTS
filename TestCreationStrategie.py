from unittest import TestCase
from Navire import Navire, FactoryNavire
from CreationStrategie import CreationStrategie
from Grille import Grille

class TestCreationStrategie(TestCase) :
    def setUp(self):
        self.cuirasse = FactoryNavire(nom="cuirassé", taille=4).get_navire()
        self.fregate = FactoryNavire(nom="frégate", taille=3).get_navire()
        self.sous_marin = FactoryNavire(nom="sous-marin", taille=3).get_navire()
        self.torpilleur = FactoryNavire(nom="torpilleur", taille=2).get_navire()
        self.porte_avions = FactoryNavire(nom="porte-avions", taille=5).get_navire()

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
