from unittest import TestCase
from CreationModeJeu import CreationModeJeu
from Grille import Grille
from ModeJeu import FactoryModeJeu
from Navire import FactoryNavire


class TestCreationModeJeu(TestCase):
    def setUp(self):

        self.cuirasse = FactoryNavire(nom="cuirassé", taille=4).get_navire()
        self.fregate = FactoryNavire(nom="frégate", taille=3).get_navire()
        self.sous_marin = FactoryNavire(nom="sous-marin", taille=3).get_navire()
        self.torpilleur = FactoryNavire(nom="torpilleur", taille=2).get_navire()
        self.porte_avions = FactoryNavire(nom="porte-avions", taille=5).get_navire()

        self.navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

    ## Setters & Getters
    # nom
    def test_set_get_nom_cas_nominal(self):
        self.creation_mode_jeu = CreationModeJeu(nom="Normal")
        self.creation_mode_jeu.set_nom()

        self.assertEqual("Normal", self.creation_mode_jeu.get_nom())

    # mode_jeu
    def test_set_get_mode_jeu_cas_nominal(self):
        self.creation_mode_jeu = CreationModeJeu(nom="Normal")
        mode_jeu_test = FactoryModeJeu(nom="Normal", navires=self.navires, taille_grille=[10, 10]).get_mode_jeu()
        self.creation_mode_jeu.set_mode_jeu(mode_jeu=mode_jeu_test)

        self.assertEqual(mode_jeu_test, self.creation_mode_jeu.get_mode_jeu())

    # navires
    def test_set_get_navires_cas_nominal(self):
        self.creation_mode_jeu = CreationModeJeu(nom="Normal")
        self.creation_mode_jeu.set_navires(self.navires)

        self.assertEqual(self.navires, self.creation_mode_jeu.get_navires())

    # grille
    def test_set_get_grille_cas_nominal(self):
        self.creation_mode_jeu = CreationModeJeu(nom="Normal")
        self.creation_mode_jeu.set_grille([10, 10])
        grille_test = Grille(10, 10)
        grille_test.create()

        self.assertEqual(grille_test, self.creation_mode_jeu.get_grille())

    def test_set_get_grille_cas_grille_invalide(self):
        self.creation_mode_jeu = CreationModeJeu(nom="Normal")
        try:
            self.creation_mode_jeu.set_grille([1, 1])
        except ValueError as current_error:
            self.assertEqual("Impossible de créer la grille !", str(current_error)[0:31])

        self.assertIs(None, self.creation_mode_jeu.get_grille())

    ## Methode de classe
    # afficher navires
    def test_afficher_navires_cas_nominal(self):
        self.creation_mode_jeu = CreationModeJeu(nom="Normal")
        self.assertEqual(True, self.creation_mode_jeu.afficher_navires(self.navires))

    ## Pas de tests sur les autres methodes de classe :
    # main & inputs_navire
    # elles dépendent des inputs utilisateurs.
