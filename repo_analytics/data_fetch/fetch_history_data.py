from google.cloud import bigquery
from tqdm import tqdm
import pandas as pd
import os
from pprint import pprint
# 展开用户家目录
credential_path = "~/clean-node-420103-6e83908c3a44.json"
resolved_path = os.path.expanduser(credential_path)

# 设置环境变量
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = resolved_path
# # 初始化BigQuery客户端
# 创建一个客户端实例
current_directory = os.getcwd()
print("当前工作目录:", current_directory)

if __name__ == "__main__":
    client = bigquery.Client()

    for yr in tqdm(range(2016, 2024)):
        # 查询语句
        query = f"""
            SELECT  repo.url,repo.name, count(repo.url) as url_count, count(repo.name) as name_count
            FROM `githubarchive.year.{yr}`
            where type = 'WatchEvent'
            group by repo.url,repo.name
            order by name_count desc
            limit 10000
        """
        
        query_job = client.query(query)  # API request
        df = query_job.to_dataframe()  
        df.to_csv(f"./tmp/{yr}_watch.csv", index=False)


    # # 执行查询
    # query_job = client.query(query)  # API request
    # df = query_job.to_dataframe()  
    # df