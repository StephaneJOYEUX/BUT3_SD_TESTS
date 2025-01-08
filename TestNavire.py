import unittest
from sys import excepthook

from Navire import Navire


class TestNavire(unittest.TestCase) :
    def setUp(self):
        pass

    def test_initialisation(self):
        self.navire = Navire("cuirassé", 3)
        self.assertEqual("cuirassé", self.navire.nom)
        self.assertEqual("C", self.navire.symbole)
        self.assertEqual(3, self.navire.taille)

    ## setters & getters
    # nom
    def test_setter_nom_cas_nominal(self):
        self.navire = Navire("cuirassé", 3)
        # pas de gestion du cas d'erreur ici, car nous ne sommes pas censé en avoir une.
        self.navire.set_nom()
        self.assertEqual("cuirassé", self.navire.get_nom())

    def test_setter_nom_cas_trop_court(self):
        self.navire = Navire("cu", 3)
        try :
            self.navire.set_nom()
        except ValueError as current_error :
            self.assertEqual("Le nom de ce navire est invalide - trop court.", str(current_error))

    def test_setter_nom_cas_trop_long(self):
        self.navire = Navire("sqbcqibcqucsuqcsub", 3)
        try :
            self.navire.set_nom()
        except ValueError as current_error :
            self.assertEqual("Le nom de ce navire est invalide - trop long.", str(current_error))

    # symbole
    def test_setter_symbole_cas_nominal(self):
        self.navire = Navire("cuirassé", 3)
        self.navire.set_symbole()
        self.assertEqual("C", self.navire.get_symbole())

    # taille
    def test_setter_taille_cas_nominal(self):
        self.navire = Navire("cuirassé", 3)
        self.navire.set_taille()
        self.assertEqual(3, self.navire.get_taille())

    def test_setter_taille_trop_court(self):
        self.navire = Navire("cuirassé", 1)
        try :
            self.navire.set_taille()
        except ValueError as current_error :
            self.assertEqual("Taille non valide ! Elle doit être supérieure ou égale à 2 !", str(current_error))


    def test_setter_taille_trop_long(self):
        self.navire = Navire("cuirassé", 15)
        try :
            self.navire.set_taille()
        except ValueError as current_error :
            self.assertEqual("Taille non valide ! Elle doit être inférieur à 10 !", str(current_error))
