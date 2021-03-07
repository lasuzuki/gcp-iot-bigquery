import os
import json
import time
from google.cloud import pubsub_v1
from google.cloud import bigquery
subscriber = pubsub_v1.SubscriberClient()

# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_name}`
subscription_path = subscriber.subscription_path(
  'dtn-host-iot-297209', 'listener')
def callback(message):
  value = message.data  

  # Send message to host X  
  os.system(f'echo "{value}" | bpsource ipn:X.X')

  # Decode the messages from bytes to be in JSON format accepted by BigQuert
  y = value.decode(encoding="utf-8")
  json_acceptable_string = y.replace("'", "\"")
  d = json.loads(json_acceptable_string)

  # Construct a BigQuery client object.
  client = bigquery.Client()

  # Set table_id to the ID of table to append to.
  # table_id = "your-project.your_dataset.your_table"
  dataset_ref = client.dataset('your_dataset')
  table_ref = dataset_ref.table('your_table')
  table = client.get_table(table_ref)
  
  # Make an API request.
  errors = client.insert_rows_json(table,[d], row_ids=[None] * len(y))
  if not errors:
      print('Data successfully loaded in table')
  else:
      print('Errors:')
      for error in errors:
          print(error)

  # Acknowledge the receipt of the message to Pub/Sub          
  message.ack()

subscriber.subscribe(subscription_path, callback=callback)

# The subscriber is non-blocking. We must keep the main thread from
# exiting to allow it to process messages asynchronously in the background.
print('Currently listening for  messages on {}'.format(subscription_path))
while True:
  time.sleep(60)