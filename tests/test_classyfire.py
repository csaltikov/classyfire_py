import unittest
from classyfire import classyfire


class TestClassyfire(unittest.TestCase):
    def setUp(self):
        self.inchikey = "LCTONWCANYUPML-UHFFFAOYSA-M"
        pass

    def test_get_inhcikey(self):
        cf = classyfire.ClassyFire()
        observed_results = cf.get_entity_classification(self.inchikey)
        observed = observed_results["class"]["name"]
        expected = 'Keto acids and derivatives'
        self.assertEqual(observed, expected)


if __name__ == '__main__':
    unittest.main()