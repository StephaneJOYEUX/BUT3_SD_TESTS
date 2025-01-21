import unittest

from TestGrille import TestGrille
from TestNavire import TestNavire
from TestStrategie import TestStrategie
from TestModeJeu import TestModeJeu
from TestCreationStrategie import TestCreationStrategie

class Test(unittest.TestCase):

    def main(self):
        TestGrille()
        TestNavire()
        TestStrategie()
        TestModeJeu()
        TestCreationStrategie()


if __name__ == '__main__':
    Test().main()
