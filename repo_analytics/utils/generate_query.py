"""
this script generate GraphQL query for multiple repositories using github api,and using Python
"""
from typing import List, Tuple

def process_alias(alias: str) -> str:
    """
    clean the alias string format to satisfy the graphQL syntax
    """
    #rule 1: replace - with _
    alias = alias.replace("-", "_")
    #rule 2: replace . with _
    alias = alias.replace(".", "_")
    return alias


def generate_query(repos: List[Tuple[str, str]]) -> str:
    """
    argument:
    repos (list of tuple): ('owner', 'name')

    return:
    str: GraphQL query statment
    """
    query_parts = []
    for i, (owner, name) in enumerate(repos, start=1):
        part = f"""
        repo_{i}_{process_alias(owner)}_{process_alias(name)}: repository(owner: "{owner}", name: "{name}") {{
            name
            stargazerCount
            forkCount
            repositoryTopics(first: 10) {{
                edges {{
                    node {{
                        id
                        url
                    }}
                }}
            }}
        }}"""
        query_parts.append(part)
    full_query = "query RepositoriesInfo {" + "".join(query_parts) + "}"
    return full_query
