"""consume githug graphQl API to fetch attributes data for the repositories"""

import os
import yaml
import sys
import json
import time
from tqdm import tqdm
import requests
import pandas as pd

# temporary solution for relative imports when testing the code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
for i in sys.path:
    print(i)
from repo_analytics.utils.generate_query import generate_query

# Your personal access token from GitHub
with open("repo_analytics/config/config.yaml", 'r', encoding='utf-8') as file:
    configs = yaml.safe_load(file)
print(configs)
GITHUB_TOKEN_PATH = configs["etl"]["GITHUB_TOKEN_PATH"]
GITHUB_API_URL = configs["etl"]["GITHUB_API_URL"]
GITHUB_TOKEN = json.load(open(GITHUB_TOKEN_PATH, encoding='utf-8'))['key']

# Headers include the authentication token and the content type
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Content-Type": "application/json",
}


years = [2020, 2021, 2022, 2023]  # year to query data

for year in years:
    watch_file = f"./tmp/{year}_watch.csv"
    watch_data = pd.read_csv(watch_file)
    watch_data['owner'] = watch_data['name'].str.split('/').str[0]
    watch_data['repo'] = watch_data['name'].str.split('/').str[1]

    query_pairs = list(zip(watch_data['owner'], watch_data['repo']))

    start, end, step = 1, 20000, 200
    for i in tqdm(range(start, end, step)):
        success = False
        while not success: # inner while loop in case if request failed, the request is not skipped
            query = generate_query(query_pairs[i:i+100])

            payload = {
                "query": query
            }

            json_payload = json.dumps(payload)
            response = requests.post(GITHUB_API_URL, headers=headers, data=json_payload)

            #print(response.status_code)
            if response.status_code == 200:
                success = True
                file_path = f"./tmp/gh_api_data/data_{year}_{i}_{i+199}.json"

                with open(file_path, "w") as json_file:
                    json.dump(response.json()['data'], json_file)
            else:
                print("Error: API request failed. Sleeping for a few minutes before retrying.")
                time.sleep(600)  # sleep for 10 minutes if the number of requests exceeds the limit

        time.sleep(20)  # don't request too frequently, which causes the request to be blocked