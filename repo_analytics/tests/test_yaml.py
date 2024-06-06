"""
some discussion online said yaml in python does not work soemtimes
this is to test if yaml works in python, for example read the yaml files
"""
import unittest
import yaml
class TestYamlFunction(unittest.TestCase):
    """
    Test Yaml function
    """
    def test_yaml_read_file(self):
        """
        Test yaml read file function
        """
        with open("repo_analytics/tests/test_files/test_yaml.yaml", 'r', encoding='utf-8') as file:
            result = yaml.safe_load(file)
        print(result)

        expected = {
            'etl': {
                'raw_data_path': 'data/raw/',
                'processed_data_path': 'data/processed/',
                'output_data_path': 'data/output/'
            },
            'database': {
                'host': 'localhost',
                'port': 5432,
                'user': 'username',
                'password': 'password'
            }
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
