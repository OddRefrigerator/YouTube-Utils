import googleapiclient.discovery
from googleapiclient.errors import HttpError
import json
import logging
import os

def configure_logging():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

def get_youtube_subscriptions(api_service_name, api_version, credentials):
    try:
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials)

        request = youtube.subscriptions().list(
            mine=True,
            part="snippet,id"
        )
        response = request.execute()

        return response
    except HttpError as e:
        logging.error(f"An error occurred retrieving subscriptions: {e}")
        return None

def save_subscriptions_to_json(subscriptions_data, filename="subscriptions.json"):
    with open(filename, 'w') as f:
        json.dump(subscriptions_data, f, indent=2)

def load_data_from_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Error loading JSON file: {e}")
        return None

def extract_channel_ids(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            # Check if 'items' key exists before accessing it
            if 'items' in data:
                channel_ids = [item['snippet']['resourceId']['channelId'] for item in data['items'] if 'channelId' in item['snippet']['resourceId']]
                return channel_ids
            else:
                logging.error("Missing 'items' key in JSON data")
                return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Error loading JSON file: {e}")
        return []

def load_config(filename="config.json"):
    try:
        client_secret = os.environ.get("YOUTUBE_CLIENT_SECRET")
        if not client_secret:
            raise KeyError("Missing YOUTUBE_CLIENT_SECRET environment variable.")

        with open(filename, 'r') as f:
            logging.info("Loaded config JSON file.")
            data = json.load(f)
            # Access other config data here if needed
            return data

    except (FileNotFoundError, json.JSONDecodeError, PermissionError, KeyError) as e:
        logging.error(f"Error loading configuration: {e}")
        return None

def main():

    configure_logging()
    logging.info("Configured logging.")

    config = load_config()

    if not config:
        logging.error("Failed to load config. Exiting.")
        return

    credentials = config['installed']['client_secret']

    # Check if 'client_secret' key exists before accessing it
    if not credentials:
        logging.error("Missing 'client_secret' key in config. Exiting.")
        return

    subscriptions = get_youtube_subscriptions("youtube", "v3", credentials)

    if subscriptions:
        logging.info("Successfully retrieved subscriptions.")
        save_subscriptions_to_json(subscriptions, "subscriptions.json")
    else:
        logging.error("Failed to retrieve subscriptions.")

if __name__ == "__main__":
    main()
