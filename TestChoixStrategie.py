from unittest import TestCase
from Strategie import Strategie_2, FactoryStrategie
from CreationStrategie import CreationStrategie_2
from Navire import Navire, FactoryNavire
from Grille import Grille
from ChoixStrategie import ChoixStrategie_2

class TestChoixStrategie(TestCase):
    def setUp(self):
        self.cuirasse = FactoryNavire(nom="cuirassé", taille=4).get_navire()
        self.fregate = FactoryNavire(nom="frégate", taille=3).get_navire()
        self.sous_marin = FactoryNavire(nom="sous-marin", taille=3).get_navire()
        self.torpilleur = FactoryNavire(nom="torpilleur", taille=2).get_navire()
        self.porte_avions = FactoryNavire(nom="porte-avions", taille=5).get_navire()

    ## Setters & Getters


    ## Methodes de classe
    def test_ecriture_fichier_sauvegarde(self):
        # Initialisation
        self.navires = {self.torpilleur, self.sous_marin, self.fregate, self.cuirasse, self.porte_avions}
        self.choix_strategie = ChoixStrategie_2("mon_pseudo", self.navires, test=True)


        # avant d'ecrire dans le fichier de sauvegarde, il faut set_artificiellement le self.referentiel
        self.choix_strategie.ecrire_fichier_sauvegarde()


    def test_lecture_fichier_sauvegarde(self):
        # Initialisation
        self.navires = {self.torpilleur, self.sous_marin, self.fregate, self.cuirasse, self.porte_avions}
        self.choix_strategie = ChoixStrategie_2("mon_pseudo", self.navires, test=True)
        self.choix_strategie.lire_fichier_sauvegarde()
        print(self.choix_strategie.get_referentiel())

    def test_intialisation(self):
        # Initialisation
        self.navires = {self.torpilleur, self.sous_marin, self.fregate, self.cuirasse, self.porte_avions}
        self.choix_strategie = ChoixStrategie_2("mon_pseudo", self.navires)

