import unittest

from TestGrille import TestGrille
from TestNavire import TestNavire
from TestStrategie import TestStrategie
from TestModeJeu import TestModeJeu
from TestCreationStrategie import TestCreationStrategie
from TestCreationModeJeu import TestCreationModeJeu
from TestChoixStrategie import TestChoixStrategie
from TestChoixModeJeu import TestChoixModeJeu

class Test(unittest.TestCase):
    def main(self):
        TestGrille()
        TestNavire()
        TestStrategie()
        TestModeJeu()

        # classes de creation
        TestCreationStrategie()
        TestCreationModeJeu()

        # classes de choix
        TestChoixStrategie()
        TestChoixModeJeu()

        # classe de jeu : BatailleNavale


if __name__ == '__main__':
    Test().main()
