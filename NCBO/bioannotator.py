import json
import re
import requests
import os
from BeautifulSoup import BeautifulSoup

####################################################################################
# Uses NCBO REST API to extract all HPO concepts
# 
# ENTER API KEY
####################################################################################
my_api_key = 'ENTER_API_KEY'
####################################################################################

def get_ncbo_hpo(txt):
    query = {'apikey': my_api_key,
        'text': txt,
             'ontologies': 'HP',
             'format': 'json'}
    url = 'http://data.bioontology.org/annotator'
    response = requests.get(url, params=query)
    print response.status_code
    if response.status_code != 200:
        print "No HPO Code mapped"
    else:
        json_result = json.loads(response.text)
        for each in json_result:
            hpo_id = each['annotatedClass']['@id']
            rest = each['annotations'][0]['text']
            hpo_id = re.search(r'HP_\d{7}',hpo_id).group()
            hpo_id = re.sub('_',':',hpo_id)
            print rest+"\t"+hpo_id

for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        print filename
        f=open( os.path.join ( '.', filename),'r')
        print get_ncbo_hpo(f.read().strip())
        f.close()
        continue
        sleep(2000)
    else:
        continue
        sleep(2000)
