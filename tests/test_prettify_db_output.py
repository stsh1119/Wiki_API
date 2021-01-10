import unittest
from api.prettify_db_output import prepare_results_from_db


class TestPrepareResults(unittest.TestCase):

    def test_prepare_results_from_db_non_empty(self):  # test with normal amout of data
        test_data = (['1', '2', '3', '4', '5'],)
        expected_output = [{'id': '1', 'title': '2', 'text': '3', 'version': '4', 'is_main': '5'}]
        self.assertEqual(prepare_results_from_db(test_data), expected_output, 'Output != expected output')

    def test_prepare_results_from_db_with_empty_data(self):  # test with empty output from db
        test_data = (['', '', '', '', ''],)
        expected_output = [{'id': '', 'title': '', 'text': '', 'version': '', 'is_main': ''}]
        self.assertEqual(prepare_results_from_db(test_data), expected_output, 'Output != expected output')

    def test_prepare_results_from_db_exception(self):  # test with incorrect db output
        test_data = ([],)
        with self.assertRaises(IndexError):
            prepare_results_from_db(test_data)
