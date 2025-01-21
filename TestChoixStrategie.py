from unittest import TestCase
from Strategie import Strategie, FactoryStrategie
from Navire import Navire, FactoryNavire
from Grille import Grille
from ChoixStrategie import ChoixStrategie


class TestChoixStrategie(TestCase):
    def setUp(self):
        self.cuirasse = FactoryNavire(nom="cuirassé", taille=4).get_navire()
        self.fregate = FactoryNavire(nom="frégate", taille=3).get_navire()
        self.sous_marin = FactoryNavire(nom="sous-marin", taille=3).get_navire()
        self.torpilleur = FactoryNavire(nom="torpilleur", taille=2).get_navire()
        self.porte_avions = FactoryNavire(nom="porte-avions", taille=5).get_navire()

        self.navires = {self.torpilleur, self.sous_marin, self.fregate, self.cuirasse, self.porte_avions}

    ## Getters

    ## Methodes de classe
    def test_ecriture_fichier_sauvegarde(self):
        # Initialisation
        self.choix_strategie = ChoixStrategie("mon_pseudo", self.navires, test=True)

        # avant d'ecrire dans le fichier de sauvegarde, il faut set_artificiellement le self.referentiel
        self.choix_strategie.ecrire_fichier_sauvegarde()

    def test_lecture_fichier_sauvegarde(self):
        # Initialisation
        self.choix_strategie = ChoixStrategie("mon_pseudo", self.navires, test=True)
        self.choix_strategie.lire_fichier_sauvegarde()

    # a modifier
    def test_intialisation(self):
        # Initialisation
        self.choix_strategie = ChoixStrategie("mon_pseudo", self.navires)
