# Python program to convert
# JSON file to CSV


import json
import csv 
import ast
import pandas as pd


# Opening JSON file and loading the data
# into the variable data
with open('combined.json') as json_file:
	data = json.load(json_file)

articles = data['articles']

for a in articles:
	del a['source']['id']
	del a['author']
	del['url']
	del a['urlToImage']
	del a['publishedAt']
	del a['content']

# now we will open a file for writing
data_file = open('news.csv', 'w', newline='')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for a in articles:
	try:

		if count == 0:

			# Writing headers of CSV file
			header = a.keys()
			csv_writer.writerow(header)
			count += 1

		# Writing data of CSV file
		csv_writer.writerow(a.values())
	except:
		pass

data_file.close()

'''
df = pd.read_csv("data_file.csv",encoding='cp1252')

df['source'] = df['source'].apply(ast.literal_eval)

for i in range(len(df)):
  df.source[i] = df.source[i]['name']

convert_dict = {'source': 'string',
                'description': 'string',
                'url':'string',
                'content':'string'}  
  
df = df.astype(convert_dict)  
print(df.dtypes)
'''