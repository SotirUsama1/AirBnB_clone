from models.base_model import BaseModel
import unittest

"""
Defines unittests for models/base_model.py.
"""


class TestBaseModel(unittest.TestCase):
    """
    Unittest class
    """

    def test_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_save(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertGreater(initial_updated_at, model.updated_at)

    def test_to_dic(self):
        model = BaseModel()
        dic = model.to_dict()
        self.assertIsInstance(dic, dict)
        self.assertEqual(dic['__class__'], model.__class__)
        self.assertEqual(dic['id'], model.id)
        self.assertEqual(dic['created_at'], model.created_at.isoformat())
        self.assertEqual(dic['updated_at'], model.updated_at.isoformat())

    def test_str(self):
        model = BaseModel()
        form = '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)
        self.assertTrue(str(model).startswith('[BaseModel]'))
        self.assertIn(model.id, str(model))
        self.assertin(model.__dict__, str(model))


if __name__ == '__main__':
    unittest.main
