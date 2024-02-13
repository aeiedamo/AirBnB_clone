import unittest
from unittest.mock import patch
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_init_no_args(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_init_with_args(self):
        test_id = "test_id"
        created_at = datetime.datetime(2024, 1, 1, 12, 0, 0)
        updated_at = datetime.datetime(2024, 1, 2, 12, 0, 0)
        base_model = BaseModel(
            id=test_id,
            created_at=created_at.isoformat(),
            updated_at=updated_at.isoformat(),
        )
        self.assertEqual(base_model.id, test_id)
        self.assertEqual(base_model.created_at, created_at)
        self.assertEqual(base_model.updated_at, updated_at)

    def test_str(self):
        self.assertEqual(
            str(self.base_model),
            "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__),
        )

    @patch("models.storage.save")
    def test_save(self, mock_save):
        self.base_model.save()
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)
        mock_save.assert_called_once()

    def test_to_dict(self):
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertIsInstance(base_model_dict["created_at"], str)
        self.assertIsInstance(base_model_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
