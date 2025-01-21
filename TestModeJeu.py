import unittest
from ModeJeu import ModeJeu
from Navire import FactoryNavire


class TestModeJeu(unittest.TestCase):
    def setUp(self):
        self.cuirasse = FactoryNavire(nom="cuirassé", taille=4).get_navire()
        self.fregate = FactoryNavire(nom="frégate", taille=3).get_navire()
        self.sous_marin = FactoryNavire(nom="sous-marin", taille=3).get_navire()
        self.torpilleur = FactoryNavire(nom="torpilleur", taille=2).get_navire()
        self.porte_avions = FactoryNavire(nom="porte-avions", taille=5).get_navire()

        self.navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

    def test_initialisation_cas_nominal(self):
        self.mode_jeu = ModeJeu(nom='Normal', navires=self.navires, taille_grille=[10, 10])
        self.assertEqual([10, 10], self.mode_jeu.taille_grille)
        self.assertEqual('Normal', self.mode_jeu.nom)
        self.assertEqual(self.navires, self.mode_jeu.navires)

    def test_initialisation_cas_blitz(self):
        self.mode_jeu = ModeJeu(nom='Blitz', navires=self.navires, taille_grille=[5, 5])
        self.assertEqual([5, 5], self.mode_jeu.taille_grille)
        self.assertEqual('Blitz', self.mode_jeu.nom)
        self.assertEqual(self.navires, self.mode_jeu.navires)

    def test_initialisation_mauvaise_taille_grille(self):
        try:
            self.mode_jeu = ModeJeu(nom='Normal', navires=self.navires, taille_grille=[1, 1])
        except ValueError as current_error:
            self.assertEqual("La taille de la grille est invalide !", str(current_error))

    ## setters & getters
    # nom
    def test_set_nom_cas_nominal(self):
        self.mode_jeu = ModeJeu(nom='Normal', navires=self.navires, taille_grille=[10, 10])
        self.mode_jeu.set_nom()
        self.assertEqual("Normal", self.mode_jeu.get_nom())

    def test_set_nom_cas_trop_court(self):
        self.mode_jeu = ModeJeu(nom='T', navires=self.navires, taille_grille=[10, 10])
        try:
            self.mode_jeu.set_nom()
        except ValueError as current_error:
            self.assertEqual("Nom du mode de jeu trop court !", str(current_error))

        self.assertEqual(None, self.mode_jeu.get_nom())

    def test_set_nom_cas_trop_long(self):
        self.mode_jeu = ModeJeu(nom='testtesttesttesttesttesttesttest', navires=self.navires, taille_grille=[10, 10])
        try:
            self.mode_jeu.set_nom()
        except ValueError as current_error:
            self.assertEqual("Nom du mode de jeu trop long !", str(current_error))

        self.assertEqual(None, self.mode_jeu.get_nom())

    # navires
    def test_set_navires_cas_nominal(self):
        # initialisation
        self.mode_jeu = ModeJeu(nom='test', navires=self.navires, taille_grille=[10, 10])
        self.mode_jeu.set_navires()
        # test
        self.assertEqual(self.navires, self.mode_jeu.get_navires())
        self.assertEqual(set, type(self.mode_jeu.get_navires()))

    # taille_grille
    def test_set_taille_grille_cas_nominal(self):
        self.mode_jeu = ModeJeu(nom='Normal', navires=self.navires, taille_grille=[10, 10])
        self.mode_jeu.set_taille_grille()
        self.assertEqual([10, 10], self.mode_jeu.get_taille_grille())

    def test_set_taille_grille_cas_trop_petit(self):
        # initialisation avec une taille conforme (car il existe deja un test sur l'initialisation)
        self.mode_jeu = ModeJeu(nom='Normal', navires=self.navires, taille_grille=[10, 10])
        try:
            # modification de cette taille rentrée en paramètre avec le setter.
            self.mode_jeu.set_taille_grille([1, 1])
        except ValueError as current_error:
            self.assertEqual("La taille de la grille est invalide !", str(current_error))

        self.assertEqual(None, self.mode_jeu.get_taille_grille())

    def test_set_taille_grille_cas_trop_grand(self):
        # initialisation avec une taille conforme (car il existe deja un test sur l'initialisation)
        self.mode_jeu = ModeJeu(nom='Normal', navires=self.navires, taille_grille=[10, 10])
        try:
            # modification de cette taille rentrée en paramètre avec le setter.
            self.mode_jeu.set_taille_grille([21, 21])
        except ValueError as current_error:
            self.assertEqual("La taille de la grille est invalide !", str(current_error))

        self.assertEqual(None, self.mode_jeu.get_taille_grille())

    # methode de classe :
    def test_verifier_validiter_navires_cas_nominal(self):
        # initialisation
        self.mode_jeu = ModeJeu(nom='Normal', navires=self.navires, taille_grille=[10, 10])
        self.mode_jeu.set_taille_grille()
        self.mode_jeu.set_navires()
        self.mode_jeu.set_nom()
        # test
        self.assertEqual([True, 0], self.mode_jeu.verifier_validiter_navires())

    def test_verifier_validiter_navires_cas_non_conforme_1_navire_trop_grand(self):
        # test du cas de non conformité :
        # 1 navire à une taille > taille d'une ligne OU colonne de la grille.
        # initialisation
        self.porte_avions = FactoryNavire(nom="porte-avions", taille=6).get_navire()
        self.navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        self.mode_jeu = ModeJeu(nom='Normal', navires=self.navires, taille_grille=[5, 5])
        self.mode_jeu.set_taille_grille()
        self.mode_jeu.set_navires()
        self.mode_jeu.set_nom()
        # test
        self.assertEqual([False, 1], self.mode_jeu.verifier_validiter_navires())


    def test_verifier_validiter_navires_cas_non_conforme_taille_tot_navires_trop_grand(self):
        # test du cas de non conformité :
        # La taille de tous les navires ne permet pas de tous les placer dans la grille par manque de place.
        # initialisation
        self.porte_avions = FactoryNavire(nom="porte-avions", taille=5).get_navire()
        self.chaloupe = FactoryNavire(nom="chaloupe", taille=3).get_navire()
        self.uboat = FactoryNavire(nom="uboat", taille=4).get_navire()
        self.falcon = FactoryNavire(nom="falcon", taille=5).get_navire()
        self.eagle = FactoryNavire(nom="eagle", taille=5).get_navire()
        self.zebra = FactoryNavire(nom="zebra", taille=5).get_navire()
        self.bear = FactoryNavire(nom="bear", taille=5).get_navire()
        self.monkey = FactoryNavire(nom="monkey", taille=5).get_navire()
        self.horse = FactoryNavire(nom="horse", taille=5).get_navire()
        self.daulphin = FactoryNavire(nom="daulphin", taille=5).get_navire()
        self.navires = {self.cuirasse,
                        self.fregate,
                        self.sous_marin,
                        self.torpilleur,
                        self.porte_avions,
                        self.chaloupe,
                        self.uboat,
                        self.falcon,
                        self.eagle,
                        self.zebra,
                        self.bear,
                        self.monkey,
                        self.horse,
                        self.daulphin}

        self.mode_jeu = ModeJeu(nom='Normal', navires=self.navires, taille_grille=[6, 6])
        self.mode_jeu.set_taille_grille()
        self.mode_jeu.set_navires()
        self.mode_jeu.set_nom()
        # test
        self.assertEqual([False, 2], self.mode_jeu.verifier_validiter_navires())
