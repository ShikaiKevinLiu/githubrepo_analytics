"""Generate the static network HTML file, one file per year, and upload them to an S3 bucket."""

import pandas as pd
from ipysigma import Sigma
import networkx as nx
import boto3
import yaml
import json
import os

def generate_network_html(year: int, input_csv_path: str, output_html_path: str):
    """Generate the static network HTML file for a given year."""
    follows_df = pd.read_csv(input_csv_path)
    sub_df = follows_df.query("Weight > 1") # to make the html file smaller

    # Initialize a Graph
    G = nx.Graph()

    # Add edges to the graph
    for _, row in sub_df.iterrows():
        G.add_edge(row['Source'], row['Target'], weight=row['Weight'])

    # Optional: View the edges with weights
    # print(G.edges(data=True))

    Sigma.write_html(
        G,
        output_html_path,
        fullscreen=True,
        node_metrics=['louvain'],
        node_color='louvain',
        max_categorical_colors=10,

        default_edge_type='curve',
        node_size=G.degree,
        start_layout=15
    )
    print(f"Generated HTML for year {year}: {output_html_path}")

def upload_to_s3(file_path: str, bucket_name: str, file_key: str, aws_credentials: dict):
    """Upload a file to an S3 bucket."""
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_credentials["aws_access_key_id"],
        aws_secret_access_key=aws_credentials["aws_secret_access_key"],
        region_name='us-west-1'
    )
    # Define extra arguments for S3 upload
    extra_args = {'ContentType': 'text/html'}

    # Upload file to S3
    s3.upload_file(file_path, bucket_name, file_key, ExtraArgs=extra_args)
    print(f"Uploaded {file_path} to s3://{bucket_name}/{file_key}")

if __name__ == '__main__':
    # Load configuration
    with open("./repo_analytics/config/config.yaml", 'r', encoding='utf-8') as file:
        configs = yaml.safe_load(file)

    # Load AWS credentials
    AWS_CREDENTIAL_PATH = configs["etl"]["AWS_CREDENTIAL_PATH"]
    AWS_CREDENTIAL = json.load(open(AWS_CREDENTIAL_PATH, encoding='utf-8'))
    bucket_name = 'static-webpage-sliu'

    for year in range(2020, 2024):
        input_csv_path = f'./tmp/repo_network_{year}.csv'
        output_html_path = f'./tmp/dataset_{year}.html'
        file_key = f'dataset_{year}.html'

        generate_network_html(year, input_csv_path, output_html_path)
        upload_to_s3(output_html_path, bucket_name, file_key, AWS_CREDENTIAL)

