import json
import logging
import googleapiclient.discovery
from googleapiclient.errors import HttpError

def load_config(filename="config.json"):
  """Loads configuration from a JSON file."""
  with open(filename, 'r') as f:
    return json.load(f)

def get_youtube_subscriptions(api_key):
  """Retrieves a list of the authenticated user's subscriptions."""
  try:
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=api_key)

    request = youtube.subscriptions().list(
        mine=True,
        part="snippet,id"
    )
    response = request.execute()

    return response
  except HttpError as e:
    # Check for specific error codes and provide more informative messages
    if e.resp.status in [401, 403]:
      logging.error(f"Authentication Error: {e}")
    elif e.resp.status == 403:
      logging.error(f"Quota Limit Reached: {e}")
    else:
      logging.error(f"An error occurred: {e}")
    return None

def save_subscriptions_to_json(subscriptions_data, filename="subscriptions.json"):
  """Saves the YouTube channel subscription data to a JSON file.

  Args:
      subscriptions_data: A dictionary containing the YouTube subscription data.
      filename (str, optional): The filename to save the JSON data to. 
          Defaults to "subscriptions.json".
  """
  with open(filename, 'w') as f:
    json.dump(subscriptions_data, f, indent=2)

if __name__ == "__main__":
  # Configure logging
  logging.basicConfig(level=logging.INFO)

  # Load API key from config file
  config = load_config()
  api_key = config.get("api_key")

  if not api_key:
    logging.error("API key not found in config.json")
    exit(1)

  subscriptions_data = get_youtube_subscriptions(api_key)
  if subscriptions_data:
    save_subscriptions_to_json(subscriptions_data)
    logging.info("Subscriptions exported to subscriptions.json")
