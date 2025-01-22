import pandas as pd

from unittest import TestCase
from Navire import FactoryNavire
from Grille import Grille, afficher_grille
from Strategie import FactoryStrategie
from BatailleNavale import BatailleNavale


class TestBatailleNavale(TestCase):
    def setUp(self):
        """__init__(self, navires: set, strategie_joueur1: Strategie, strategie_joueur2: Strategie,
        instance_grille: Grille = Grille(10, 10), pseudo_j1: str = 'Ordinateur 1',
        pseudo_j2: str = 'Ordinateur 2',
        test: bool = False):"""
        ## Initialisation
        # navires
        self.cuirasse = FactoryNavire(nom="cuirassé", taille=4).get_navire()
        self.fregate = FactoryNavire(nom="frégate", taille=3).get_navire()
        self.sous_marin = FactoryNavire(nom="sous-marin", taille=3).get_navire()
        self.torpilleur = FactoryNavire(nom="torpilleur", taille=2).get_navire()
        self.porte_avions = FactoryNavire(nom="porte-avions", taille=5).get_navire()

        self.navires = {self.torpilleur, self.sous_marin, self.fregate, self.cuirasse, self.porte_avions}

        # grille
        self.grille = Grille(10, 10)
        self.grille.create()

        # inputs strategie
        data_inputs_strategie = {"nom": ["torpilleur", "sous-marin", "frégate", "cuirassé", "porte-avions"],
                                 "taille": [2, 3, 3, 4, 5], "coord_x": [1, 2, 3, 4, 5],
                                 "coord_y": [1, 2, 3, 4, 5], "orientation": ["S", "S", "S", "S", "S"]}
        inputs_strategie = pd.DataFrame(data_inputs_strategie)

        # strategie
        self.strategie_j1 = FactoryStrategie(navires=self.navires, inputs_strategie=inputs_strategie,
                                             grille=self.grille, complete=True).get_strategie()
        self.strategie_j2 = FactoryStrategie(navires=self.navires, inputs_strategie=inputs_strategie,
                                             grille=self.grille, complete=True).get_strategie()

        self.pseudo_j1 = 'pseudo_j1'
        self.pseudo_j2 = 'Ordinateur 2'

    # navire_coule
    def test_navire_coule_true(self):
        pass

    def test_navire_coule_false(self):
        pass


    # tous_les_navires_ont_coule
    def test_tous_les_navires_ont_coule_true(self):
        pass

    def test_tous_les_navires_ont_coule_false(self):
        pass

    # tir
    def test_tir_touche(self):
        self.bataille_navale = BatailleNavale(navires=self.navires, test=True, pseudo_j1=self.pseudo_j1,
                                              pseudo_j2=self.pseudo_j2, instance_grille=self.grille,
                                              strategie_joueur1=self.strategie_j1, strategie_joueur2=self.strategie_j2)
        # aide visuelle pour le deboggage
        self.strategie_j1.affichage_strategie()

        self.bataille_navale.tir(numJoueur=1, colonne=1, ligne=1)
        afficher_grille(self.bataille_navale.grille_def_j2)

    def test_tir_touche_coule(self):
        pass

    def test_tir_rate(self):
        pass
