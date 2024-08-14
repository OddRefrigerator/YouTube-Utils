import googleapiclient.discovery
from googleapiclient.errors import HttpError
import json
import logging

# Configure logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def get_youtube_subscriptions(api_service_name, api_version, credentials):
  """Retrieves a list of the authenticated user's subscriptions.

  This function retrieves subscriptions and handles potential errors
  during the API call.

  Args:
    api_service_name: The name of the YouTube Data API service ("youtube").
    api_version: The version of the YouTube Data API to use ("v3").
    credentials: The user's OAuth 2.0 credentials.

  Returns:
    A dictionary containing the subscription data on success, None on error.
  """
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
    logging.error(f"An error occurred: {e}")
    return None

def save_subscriptions_to_json(subscriptions_data, filename="subscriptions.json"):
  """Saves the subscriptions data to a JSON file.

  This function saves the subscription data retrieved from the API to a JSON file.

  Args:
    subscriptions_data: A dictionary containing the subscription data.
    filename: The name of the output JSON file (defaults to "subscriptions.json").
  """
  with open(filename, 'w') as f:
    json.dump(subscriptions_data, f, indent=2)

def extract_channel_ids(json_file):
  """Extracts channel IDs from a JSON file containing subscription data.

  This function parses the saved JSON file and extracts a list of channel IDs.

  Args:
    json_file: The path to the JSON file containing subscription data.

  Returns:
    A list of channel IDs extracted from the JSON file.
  """

  try:
    with open(json_file, 'r') as f:
      data = json.load(f)

    channel_ids = []
    for item in data['items']:
      try:
        # Handle potential missing channel ID key
        channel_id = item['snippet']['resourceId']['channelId']
        channel_ids.append(channel_id)
      except KeyError:
        logging.warning(f"Skipping item: Channel ID missing")

    return channel_ids
  except FileNotFoundError:
    logging.error(f"JSON file not found: {json_file}")
    return []

# Replace with your API credentials and setup
api_service_name = "youtube"
api_version = "v3"
credentials = # Your OAuth 2.0 credentials

# Get subscriptions and handle errors
subscriptions_data = get_youtube_subscriptions(api_service_name, api_version, credentials)
if not subscriptions_data:
  exit()

# Save subscriptions to JSON
save_subscriptions_to_json(subscriptions_data)
logging.info("Subscriptions exported to subscriptions.json")

# Extract channel IDs from the saved JSON
json_file = 'subscriptions.json'
channel_ids = extract_channel_ids(json_file)

# Print extracted channel IDs with error handling
logging.info("Extracted channel IDs:")
for channel_id in channel_ids:
  print(channel_id)
