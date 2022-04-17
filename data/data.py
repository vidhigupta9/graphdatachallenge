# Python program to convert
# JSON file to CSV


import json
import csv 

# Opening JSON file and loading the data
# into the variable data
with open('combined.json') as json_file:
	data = json.load(json_file)

articles = data['articles']


for a in articles:
	del a['source']['id']
	del a['author']
	del a['title']
	del a['urlToImage']
	del a['publishedAt']

# now we will open a file for writing
data_file = open('data_file.csv', 'w', newline='')

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
