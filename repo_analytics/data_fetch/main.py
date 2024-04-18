"""
This is the main file for the repo_analytics package.
"""

from utils.generate_query import generate_query
print(generate_query([("owner1",'repo1'), ("owner2",'repo2')]))