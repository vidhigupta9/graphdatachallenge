from newsapi import NewsApiClient


newsapi = NewsApiClient(api_key='352574f8179f4c848e700b1edd8b157a')


all_articles = newsapi.get_everything(q='Will Smith',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2,
                                      to='2022-03-15',
                                      from_param='2022-03-20'
                                      )

import json
	
# Serializing json
json_object = json.dumps(all_articles, indent = 4)

with open("ws.json", "w") as outfile:
    outfile.write(json_object)

