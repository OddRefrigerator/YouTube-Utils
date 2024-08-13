import googleapiclient.discovery
from googleapiclient.errors import HttpError
import json

def get_youtube_subscriptions(api_service_name, api_version, credentials):
  """Retrieves a list of the authenticated user's subscriptions."""
  try:
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.subscriptions().list(
        mine=True,
        part="snippet,id"
    )
    response = request.execute()

    return response
  except HttpError as e:
    print(f"An error occurred: {e}")
    return None

def save_subscriptions_to_json(subscriptions_data, filename="subscriptions.json"):
  """Saves the subscriptions data to a JSON file."""
  with open(filename, 'w') as f:
    json.dump(subscriptions_data, f, indent=2)

# Replace with your API credentials and setup
api_service_name = "youtube"
api_version = "v3"
credentials = # Your OAuth 2.0 credentials

subscriptions_data = get_youtube_subscriptions(api_service_name, api_version, credentials)
if subscriptions_data:
  save_subscriptions_to_json(subscriptions_data)
  print("Subscriptions exported to subscriptions.json")
