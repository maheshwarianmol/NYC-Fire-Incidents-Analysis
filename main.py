from sodapy import Socrata
import requests
from requests.auth import HTTPBasicAuth
import argparse
import sys
import os
import json
 

# Creates a parser. Parser is the thing where you add your arguments. 
parser = argparse.ArgumentParser(description='Fire Incident Dispatch Data')
# In the parse, we have two arguments to add.
# The first one is a required argument for the program to run. If page_size is not passed in, don’t let the program to run
parser.add_argument('--page_size', type=int, help='how many rows to get per page', required=True)
# The second one is an optional argument for the program to run. It means that with or without it your program should be able to work.
parser.add_argument('--num_pages', type=int, help='how many pages to get in total')
# Take the command line arguments passed in (sys.argv) and pass them through the parser.
# Then you will ned up with variables that contains page size and num pages.  
args = parser.parse_args(sys.argv[1:])
print(args)


DATASET_ID=os.environ["DATASET_ID"]
APP_TOKEN=os.environ["APP_TOKEN"]
ES_HOST=os.environ["ES_HOST"]
ES_USERNAME=os.environ["ES_USERNAME"]
ES_PASSWORD=os.environ["ES_PASSWORD"]
INDEX_NAME=os.environ["INDEX_NAME"]


if __name__ == '__main__':
    
    try:
        # {ES_HOST}/{INDEX_NAME}: This is the URL to create payroll index, which is our Elasticsearch db.
        resp = requests.put(f"{ES_HOST}/{INDEX_NAME}", auth=HTTPBasicAuth(ES_USERNAME, ES_PASSWORD),
            json={
                "settings": {
                    "number_of_shards": 1,
                    "number_of_replicas": 1
                },
                "mappings": {
                    "properties": {
                        "incident_datetime": {"type": "date"},
                        "incident_response_seconds_qy": {"type": "float"},
                        "dispatch_response_seconds_qy": {"type": "float"},
                        "incident_borough": {"type": "keyword"},
                        "incident_classification": {"type": "keyword"},
                        "starfire_incident_id": {"type": "keyword"},
                        "incident_close_datetime": {"type": "date"},
                    }
                },
            }
        )
        resp.raise_for_status()
        #print(resp.json())

    # If try to run the above code again, which creates an index, it will give an error. Because, it’s already created.
    # In order to avoid it, we raise an exception.
    except Exception as e:
        print("Index already exists! Skipping")

    for i in range(0, args.num_pages):
        client = Socrata("data.cityofnewyork.us", APP_TOKEN, timeout=10000)
        #rows = client.get(DATASET_ID, limit=10)
        rows = client.get(DATASET_ID, limit=args.page_size, offset=(i*args.page_size),)
        es_rows = [] 
        
        for row in rows:
            try:
                # Convert
                es_row = {}
                es_row["incident_datetime"] = row["incident_datetime"]
                es_row["incident_response_seconds_qy"] = row["incident_response_seconds_qy"]
                es_row["dispatch_response_seconds_qy"] = row["dispatch_response_seconds_qy"]
                es_row["incident_borough"] = row["incident_borough"]
                es_row["incident_classification"] = row["incident_classification"] #edited
                es_row["starfire_incident_id"] = row["starfire_incident_id"]
                es_row["incident_close_datetime"] = row["incident_close_datetime"]
          
            except Exception as e:
                #print (f"Error!: {e}, skipping row: {row}")
                continue
            
            es_rows.append(es_row)
         
        #bulk API    
        bulk_upload_data = ""
        
        for line in es_rows:
            print(f'Handling row {line["starfire_incident_id"]}')
            action = '{"index": {"_index": "' + INDEX_NAME + '", "_id": "' + line["starfire_incident_id"] + '"}}'
            data = json.dumps(line)
            bulk_upload_data += f"{action}\n"
            bulk_upload_data += f"{data}\n"
    
        #print (bulk_upload_data)
        
        try:
            # Upload to Elasticsearch by creating a document
            resp = requests.post(f"{ES_HOST}/_bulk",
                    data=bulk_upload_data,auth=HTTPBasicAuth(ES_USERNAME, ES_PASSWORD), headers = {"Content-Type": "application/x-ndjson"})
            resp.raise_for_status()
            #print(resp.json())(edited)
            print("Done")
            #If it fails, skip that row and move on.
        except Exception as e:
            print(f"Failed to insert in ES: {e}, skipping row: {row}")
            continue
        
    