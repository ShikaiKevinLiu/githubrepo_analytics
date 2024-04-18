import pandas as pd
import os
import sys
from tqdm import tqdm
# temporary solution for relative imports e
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.generate_query import generate_query

print(os.getcwd())
watch_2023 = pd.read_csv("./tmp/2023_watch.csv")
watch_2023['owner'] = watch_2023['name'].str.split('/').str[0]
watch_2023['repo'] = watch_2023['name'].str.split('/').str[1]

query_pairs = list(zip(watch_2023['owner'], watch_2023['repo']))
import requests
import json

# Your personal access token from GitHub
access_token = json.load(open("/Users/shikailiu/gh_token.json"))['key']


# The API URL
url = 'https://api.github.com/graphql'

# Headers include the authentication token and the content type
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

# ------------------------------------------------------------

import time
import requests  # 假设你使用requests库发送API请求
for i in tqdm(range(1,10000, 100)):
    query = generate_query(query_pairs[i:i+100])

    # Payload is a dictionary with the key 'query' holding the GraphQL query
    payload = {
        "query": query
    }

    # Convert the payload to JSON format
    json_payload = json.dumps(payload)

    # Make the POST request
    response = requests.post(url, headers=headers, data=json_payload)

    # Print the response (status code and returned data)
    print(response.status_code)
    if response.status_code != 200:
        print("Error: API request failed")
        break
    file_path = f"./tmp/gh_api_data/data_{i}_{i+99}.json"

    # Write JSON data to file
    with open(file_path, "w") as json_file:
        json.dump(response.json()['data'], json_file)
    time.sleep(20)
