# YouTube Utilities

This Python script collection provides tools for managing YouTube subscriptions.

## Current functionalities:

Export Subscriptions (subscriptions.py): Exports your YouTube subscriptions to a JSON file.
Extract Channel IDs (extract_channel_ids.py): (Optional) Extracts channel IDs from a JSON file containing subscription data (useful for further processing or manual subscription).

## Important Notes:

Directly importing subscriptions to another YouTube account using the YouTube Data API v3 is currently not supported due to security limitations.
This repository provides functionalities for exporting subscriptions and (optionally) extracting channel IDs. Manual subscription or exploration of alternative methods might be required for import.

## Getting Started:

Install required libraries (googleapiclient).
Replace the placeholder for your OAuth 2.0 credentials in the scripts.
Run subscriptions.py to export your subscriptions.

## Disclaimer:

Third-party tools or manual subscription might be required for import functionalities. Use such methods with caution and at your own risk.
