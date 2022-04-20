from newsapi import NewsApiClient


newsapi = NewsApiClient(api_key='352574f8179f4c848e700b1edd8b157a')


all_articles = newsapi.get_everything(q='Elon Musk tweets',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1,
                                      to='2022-04-05',
                                      from_param='2022-04-15',

                                      )

import json
	
# Serializing json
json_object = json.dumps(all_articles, indent = 4)

with open("em.json", "w") as outfile:
    outfile.write(json_object)

