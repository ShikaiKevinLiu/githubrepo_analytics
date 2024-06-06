"""This script is used to fetch all history data from BigQuery when initializing the project."""
import yaml
from google.cloud import bigquery
from google.oauth2 import service_account
from tqdm import tqdm

if __name__ == "__main__":
    with open("repo_analytics/config/config.yaml", 'r', encoding='utf-8') as file:
        configs = yaml.safe_load(file)
    CREDENTIAL_PATH = configs["etl"]["GOOGLE_CREDENTIALS_PATH"]
    # Initialize a BigQuery Client
    credentials = service_account.Credentials.from_service_account_file(CREDENTIAL_PATH)
    client = bigquery.Client(credentials=credentials)

    for yr in tqdm(range(2016, 2024)):
        # query statm
        query = f"""
            SELECT  repo.url,repo.name, count(repo.url) as url_count, count(repo.name) as name_count
            FROM `githubarchive.year.{yr}`
            where type = 'WatchEvent'
            group by repo.url,repo.name
            order by name_count desc
            limit 20000
        """
        query_job = client.query(query)  # API request
        df = query_job.to_dataframe()
        
        # todo: wirte code for mkdir if not exists, and folder path in config.yaml
        df.to_csv(f"./tmp/{yr}_watch.csv", index=False)
