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
    生成包含多个仓库查询的GraphQL查询字符串。

    参数:
    repos (list of tuple): 列表，其中每个元组包含('owner', 'name')。

    返回:
    str: GraphQL查询字符串。
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
