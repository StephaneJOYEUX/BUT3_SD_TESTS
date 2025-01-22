from unittest import TestCase
from ChoixModeJeu import ChoixModeJeu
from Navire import FactoryNavire
from ModeJeu import FactoryModeJeu
from Grille import Grille


class TestChoixModeJeu(TestCase):
    def setUp(self):
        # navires
        self.cuirasse = FactoryNavire(nom="cuirassé", taille=4).get_navire()
        self.fregate = FactoryNavire(nom="frégate", taille=3).get_navire()
        self.sous_marin = FactoryNavire(nom="sous-marin", taille=3).get_navire()
        self.torpilleur = FactoryNavire(nom="torpilleur", taille=2).get_navire()
        self.porte_avions = FactoryNavire(nom="porte-avions", taille=5).get_navire()

        self.navires = {self.cuirasse, self.fregate, self.sous_marin, self.torpilleur, self.porte_avions}

        # grille
        self.grille = Grille(10, 10)
        self.grille.create()
        self.taille_grille = [self.grille.get_nb_lignes(), self.grille.get_nb_colonnes()]

        # mode_jeu
        self.mode_jeu = FactoryModeJeu(nom="Normal", navires=self.navires,
                                       taille_grille=self.taille_grille).get_mode_jeu()

    ## Setters & Getters
    # navires
    def test_set_get_navires_cas_nominal(self):
        self.choix_mode_jeu = ChoixModeJeu()
        self.choix_mode_jeu.set_navires(self.navires)

        self.assertEqual(self.navires, self.choix_mode_jeu.get_navires())

    # grille
    # il n'existe pas de cas où la grille est de taille incorrecte car l'instance de Grille est déjà créée
    # => les tests sur la taille sont déjà effectué.
    def test_set_get_grille_cas_nominal(self):
        self.choix_mode_jeu = ChoixModeJeu()
        self.choix_mode_jeu.set_grille(self.grille)

        self.assertEqual(self.grille, self.choix_mode_jeu.get_grille())

    # mode_jeu
    def test_set_get_mode_jeu_cas_nominal(self):
        self.choix_mode_jeu = ChoixModeJeu()
        self.choix_mode_jeu.set_mode_jeu(self.mode_jeu)

        self.assertEqual(self.mode_jeu, self.choix_mode_jeu.get_mode_jeu())

    # attributes
    def test_set_attributes_cas_nominal(self):
        self.choix_mode_jeu = ChoixModeJeu()
        self.choix_mode_jeu.set_attributes(nb_lignes=self.taille_grille[0], nb_colonnes=self.taille_grille[1],
                                           navires=self.navires, nom_mode_jeu="Normal")

        self.assertEqual(self.grille, self.choix_mode_jeu.get_grille())
        self.assertEqual(self.navires, self.choix_mode_jeu.get_navires())
        self.assertEqual(self.mode_jeu, self.choix_mode_jeu.get_mode_jeu())

    def test_set_attributes_cas_incorrect(self):
        self.choix_mode_jeu = ChoixModeJeu()
        taille_grille_test = [1, 1]
        try:
            self.choix_mode_jeu.set_attributes(nb_lignes=taille_grille_test[0], nb_colonnes=taille_grille_test[1],
                                               navires=self.navires, nom_mode_jeu="Normal")
        except ValueError as current_error:
            self.assertEqual("Impossible de créer la grille !", str(current_error)[0:31])

    ## Methodes de classes
    # lecture fichier sauvegarde

    # ecriture fichier sauvegarde

    # afficher_navires

    ## a faire :
    # setters & getters + set_attributes
    # lecture/ecriture ficher sauvegarde (entete)
    # afficher_navires
