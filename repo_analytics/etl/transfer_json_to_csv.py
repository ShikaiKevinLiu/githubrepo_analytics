"""This Script transfers the Repo attributes data(forkcount, topics, etc.) from JSON to CSV format,
then transfer the data into a network data format"""
from itertools import combinations
from collections import defaultdict
import pandas as pd
from repo_analytics.utils.etl_helpers import combine_json_files

def dict_to_pandas(data: dict) -> pd.DataFrame:
    """
    Convert a dictionary to a pandas DataFrame
    Input: repo attributes data in raw json format
    Output: a pandas DataFrame with the dictionary data
    """
    # Initialize an empty list to store the extracted data
    data_list = []
    # Loop over the dictionary items
    for repo_name, repo_info in data.items():
        # Skip this iteration if repo_info is None or empty,
        # this is because the repository was deleted or other reasons
        if not repo_info:
            print(f"Warning: No data for {repo_name}, skipping.")
            continue
        # Extract the 'name', 'forkCount','starCount' and 'repositoryTopics'
        name = repo_info.get('name', 'Missing')  # Provide a default value in case 'name' is missing
        fork_count = repo_info.get('forkCount', 'Missing')
        star_count = repo_info.get('stargazerCount', 'Missing')

        # extract topics as a list
        repo_topics = repo_info.get('repositoryTopics', {}).get('edges', 'Missing')
        topics = [topic['node']['url'].split('/')[-1] for topic in repo_topics if 'node' in topic and 'url' in topic['node']]
        # Append a tuple with the extracted information to the data list
        data_list.append((name, fork_count, star_count, topics))
    # Convert the list of tuples to a pandas DataFrame
    df = pd.DataFrame(data_list, columns=['name', 'forkCount', 'star_count', 'topics'])
    return df

def create_network_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a network DataFrame from a DataFrame of repository topics
    Input: a pandas DataFrame with columns 'name', 'forkCount', 'star_count', 'topics'
    Output: a pandas DataFrame with columns 'topic1', 'topic2', 'edge_count'
    """
    # Create a default dictionary to count pairs
    pair_counts = defaultdict(int)

    # Iterate over each list of topics and count pairs
    for topics_list in df['topics']:
        # Get all combinations of topics in pairs from the list
        for topic_pair in combinations(topics_list, 2):
            # Sort the pair to ensure (topic1, topic2), (topic2, topic1) are not regarded as two different pairs
            sorted_pair = tuple(sorted(topic_pair))
            pair_counts[sorted_pair] += 1

    # Now convert the pair counts into a DataFrame
    network_data = pd.DataFrame(
        [(pair[0], pair[1], count) for pair, count in pair_counts.items()],
        columns=['Source', 'Target', 'Weight']
    )
    return network_data


if __name__ == '__main__':
    
    years = range(2020, 2024)
    for year in years:
        # Step 1: Combine all JSON files for the specified year into one large dictionary
        repo_attributes_data = combine_json_files('tmp/gh_api_data/', year)

        # Step 2: Convert the dictionary to a pandas DataFrame
        df_repo = dict_to_pandas(repo_attributes_data)

        # Step 3: Create a network DataFrame from the repository topics
        network_df = create_network_data(df_repo)
        
        # Step 4: Save the network DataFrame to a CSV file
        network_df.to_csv(f'tmp/repo_network_{year}.csv', index=False)