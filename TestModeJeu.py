import unittest
from ModeJeu import ModeJeu
from Navire import Navire


class TestModeJeu(unittest.TestCase) :
    def setUp(self):
        self.cuirasse = Navire(nom="cuirassé", taille=4)
        self.fregate = Navire(nom="frégate", taille=3)
        self.sous_marin = Navire(nom="sous-marin", taille=3)
        self.torpilleur = Navire(nom="torpilleur", taille=2)
        self.porte_avions = Navire(nom="porte-avions", taille=5)

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
        try :
            self.mode_jeu = ModeJeu(nom='Normal', navires=self.navires, taille_grille=[1,1])
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
        try :
            self.mode_jeu.set_nom()
        except ValueError as current_error :
            self.assertEqual("Nom du mode de jeu trop court !", str(current_error))

    def test_set_nom_cas_trop_long(self):
        self.mode_jeu = ModeJeu(nom='rfjvjbsdkhvbdkhvbhbhbcdhkcb', navires=self.navires, taille_grille=[10, 10])
        try:
            self.mode_jeu.set_nom()
        except ValueError as current_error:
            self.assertEqual("Nom du mode de jeu trop long !", str(current_error))

    # navires
    def test_set_navires_cas_nominal(self):
        # pas de probleme de conformité
        # verification que la var de classe _navires correspond à celle donnée en paramètre.
        # verifier que le get_nb_navires() renvoie bien le len(self.navires).
        pass

    def test_set_navires_cas_non_conforme_1_navire_trop_grand(self):
        # test du cas de non conformité :
        # 1 navire à une taille > taille d'une ligne OU colonne de la grille.
        pass

    def test_set_navires_cas_non_conforme_taille_tot_navires_trop_grand(self):
        # test du cas de non conformité :
        # La taille de tous les navires ne permet pas de tous les placer dans la grille par manque de place.
        pass


    # taille_grille
    def test_set_taille_grille_cas_nominal(self):
        self.mode_jeu = ModeJeu(nom='Normal', navires=self.navires, taille_grille=[10, 10])
        self.mode_jeu.set_taille_grille()
        self.assertEqual([10, 10], self.mode_jeu.get_taille_grille())

    def test_set_taille_grille_cas_trop_petit(self):
        # initialisation avec une taille conforme (car il existe deja un test sur l'initialisation)
        self.mode_jeu = ModeJeu(nom='Normal', navires=self.navires, taille_grille=[10, 10])
        try :
            # modification de cette taille rentrée en paramètre avec le setter.
            self.mode_jeu.set_taille_grille([1,1])
            self.assertEqual([], self.mode_jeu.get_taille_grille())
        except ValueError as current_error :
            self.assertEqual("La taille de la grille est invalide !", str(current_error))


    def test_set_taille_grille_cas_trop_grand(self):
        # initialisation avec une taille conforme (car il existe deja un test sur l'initialisation)
        self.mode_jeu = ModeJeu(nom='Normal', navires=self.navires, taille_grille=[10, 10])
        try :
            # modification de cette taille rentrée en paramètre avec le setter.
            self.mode_jeu.set_taille_grille([21,21])
            self.assertEqual([], self.mode_jeu.get_taille_grille())
        except ValueError as current_error :
            self.assertEqual("La taille de la grille est invalide !", str(current_error))