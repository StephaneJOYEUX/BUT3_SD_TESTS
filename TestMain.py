import unittest

from TestBatailleNavale import TestBatailleNavale
from TestChoixStrategie import TestChoixStrategie
from TestCreationStrategie import TestCreationStrategie
from TestGrille import TestGrille
from TestStrategie import TestStrategie

class TestMain(unittest.TestCase):
    def main(self):
        TestGrille()
        TestStrategie()
        TestCreationStrategie()
        TestChoixStrategie()
        TestBatailleNavale()

if __name__ == '__main__':
    unittest.main()