import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_inheritance(self):
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes_default_values(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")


if __name__ == "__main__":
    unittest.main()
