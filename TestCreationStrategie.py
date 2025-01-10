from unittest import TestCase
from Navire import Navire

class TestCreationStrategie(TestCase) :
    def setUp(self):
        self.cuirasse = Navire(nom="cuirassé", taille=4)
        self.fregate = Navire(nom="frégate", taille=3)
        self.sous_marin = Navire(nom="sous-marin", taille=3)
        self.torpilleur = Navire(nom="torpilleur", taille=2)
        self.porte_avions = Navire(nom="porte-avions", taille=5)

        self.navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

    def test_initialisation(self):
        pass