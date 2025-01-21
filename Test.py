import unittest
from BatailleNavale import BatailleNavale
from Strategie import Strategie
from Grille import Grille
from CreationStrategie import CreationStrategie
from ChoixStrategie import ChoixStrategie

from TestGrille import TestGrille
from TestNavire import TestNavire
from TestStrategie import TestStrategie
from TestModeJeu import TestModeJeu


class Test(unittest.TestCase):

    def main(self):
        TestGrille()
        TestNavire()
        TestStrategie()
        TestModeJeu()


if __name__ == '__main__':
    Test().main()
