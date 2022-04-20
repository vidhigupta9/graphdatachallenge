# Imports
import pyTigerGraph as tg
import json
import pandas as pd

# Connection parameters to Tigergraph
hostName = "https://a2c927145d9544f0968367fea409254c.i.tgcloud.io"
userName = "tigergraph"
password = "monday02"

conn = tg.TigerGraphConnection(host=hostName, username=userName, password=password)

print("Connected to",conn)

conn.graphname="news"
secret = conn.createSecret()
authToken = conn.getToken(secret)
authToken = authToken[0]
print(authToken)
conn = tg.TigerGraphConnection(host=hostName, graphname="news", username=userName, password=password, apiToken=authToken)

def pprint(string):
  print(json.dumps(string, indent=2))

results = conn.gsql('''
  USE GRAPH news
  BEGIN
  CREATE LOADING JOB newdata FOR GRAPH news {
  DEFINE FILENAME MyDataSource;
  LOAD MyDataSource TO VERTEX Post VALUES($0, $1, $2, $4) USING SEPARATOR=",", HEADER="true", EOL="\\n", QUOTE="double";
  LOAD MyDataSource TO VERTEX Hashtag VALUES($5) USING SEPARATOR=",", HEADER="true", EOL="\\n", QUOTE="double";
  LOAD MyDataSource TO VERTEX Hashtag VALUES($6) USING SEPARATOR=",", HEADER="true", EOL="\\n", QUOTE="double";
  LOAD MyDataSource TO VERTEX Hashtag VALUES($7) USING SEPARATOR=",", HEADER="true", EOL="\\n", QUOTE="double";
  LOAD MyDataSource TO VERTEX Hashtag VALUES($8) USING SEPARATOR=",", HEADER="true", EOL="\\n", QUOTE="double";
  LOAD MyDataSource TO EDGE posted VALUES($3, $0, $2) USING SEPARATOR=",", HEADER="true", EOL="\\n", QUOTE="double";
  LOAD MyDataSource TO EDGE has_tag VALUES($0, $5) USING SEPARATOR=",", HEADER="true", EOL="\\n", QUOTE="double";
  LOAD MyDataSource TO EDGE has_tag VALUES($0, $6) USING SEPARATOR=",", HEADER="true", EOL="\\n", QUOTE="double";
  LOAD MyDataSource TO EDGE has_tag VALUES($0, $7) USING SEPARATOR=",", HEADER="true", EOL="\\n", QUOTE="double";
  LOAD MyDataSource TO EDGE has_tag VALUES($0, $8) USING SEPARATOR=",", HEADER="true", EOL="\\n", QUOTE="double";
  }
  END
  ''')
print(results)

# Load the posts file wiht the 'load_posts' job
posts_file = '/content/TigerGraph-101/posts.csv'
results = conn.uploadFile(posts_file, fileTag='MyDataSource', jobName='load_posts')
print(json.dumps(results, indent=2))