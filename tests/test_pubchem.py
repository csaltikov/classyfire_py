import unittest
from classyfire import pubchem


class TestPubchem(unittest.TestCase):
    def setUp(self):
        self.pyruvate = "pyruvate"
        pass

    def test_get_inhcikey(self):
        results = pubchem.get_inchikey(self.pyruvate)
        expected = "LCTONWCANYUPML-UHFFFAOYSA-M"
        self.assertEqual(results, expected)


if __name__ == '__main__':
    unittest.main()