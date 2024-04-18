"""
Unit tests for generate_query function
"""
import unittest
import sys
import os
print(os.getcwd())
print(sys.path,"\n")
print("当前工作目录:", os.getcwd())

from repo_analytics.utils.generate_query import generate_query

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(os.getcwd())

class TestGenerateQuery(unittest.TestCase):
    """
    test generate_query function
    """
    def test_generate_query_single_repo(self):
        """
        test generate_query with single repository
        """
        result = generate_query([('owner1', 'repo1')])
        expected = """query RepositoriesInfo {
            repo_1_owner1_repo1: repository(owner: "owner1", name: "repo1") {
            name
            stargazerCount
            forkCount
            repositoryTopics(first: 10) {
                edges {
                    node {
                        id
                        url
                    }
                }
            }
        }}"""
        result_lines = result.split('\n')
        expected_lines = expected.split('\n')
        result_no_indent = [line.strip() for line in result_lines]
        expected_no_indent = [line.strip() for line in expected_lines]
        self.assertEqual(result_no_indent, expected_no_indent)

    def test_generate_query_multiple_repos(self):
        """
        test generate_query with multiple repositories
        """
        result = generate_query([('owner1', 'repo1'), ('owner2', 'repo2'), ('owner3', 'repo3')])
        expected = """query RepositoriesInfo {
            repo_1_owner1_repo1: repository(owner: "owner1", name: "repo1") {
            name
            stargazerCount
            forkCount
            repositoryTopics(first: 10) {
                edges {
                    node {
                        id
                        url
                    }
                }
            }
        }
        repo_2_owner2_repo2: repository(owner: "owner2", name: "repo2") {
            name
            stargazerCount
            forkCount
            repositoryTopics(first: 10) {
                edges {
                    node {
                        id
                        url
                    }
                }
            }
        }
        repo_3_owner3_repo3: repository(owner: "owner3", name: "repo3") {
            name
            stargazerCount
            forkCount
            repositoryTopics(first: 10) {
                edges {
                    node {
                        id
                        url
                    }
                }
            }
        }}"""
        result_lines = result.split('\n')
        expected_lines = expected.split('\n')
        result_no_indent = [line.strip() for line in result_lines]
        expected_no_indent = [line.strip() for line in expected_lines]
        self.assertEqual(result_no_indent, expected_no_indent)

if __name__ == '__main__':
    unittest.main()
