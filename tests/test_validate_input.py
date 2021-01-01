import unittest
from app.validate_input import validate_input


class TestValidations(unittest.TestCase):

    def test_validate_input_positive(self):
        test_object = {
                       "id": 2,
                       "is_main": 0,
                       "text": "Body",
                       "title": "1st",
                       "version": 3
                       }
        self.assertEqual(validate_input(test_object), True, 'All fields should be present')

    def test_validate_input_negative(self):
        test_object = {
                       "id": 1,
                       "text": "Body",
                       "title": "1st"
                       }
        self.assertEqual(validate_input(test_object), None, 'If seme fields are absent - None should be returned')


if __name__ == '__main__':
    unittest.main()
