import json

def extract_channel_ids(json_file):
  """Extracts channel IDs from a JSON file containing subscription data.

  Args:
    json_file: The path to the JSON file.

  Returns:
    A list of channel IDs.
  """

  with open(json_file, 'r') as f:
    data = json.load(f)

  channel_ids = []
  for item in data['items']:
    channel_id = item['snippet']['resourceId']['channelId']
    channel_ids.append(channel_id)

  return channel_ids

# Example usage:
json_file = 'subscriptions.json'
channel_ids = extract_channel_ids(json_file)
print(channel_ids)