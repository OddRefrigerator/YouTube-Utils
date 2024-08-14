# Python Script for Retrieving YouTube Subscriptions
This Python script retrieves a list of the authenticated user's YouTube subscriptions and optionally saves them to a JSON file.

## Features:

Connects to the YouTube Data API v3.
Retrieves a list of the user's subscriptions with basic information (channel ID and title).
Handles potential errors during the API call.
Provides functions to save retrieved subscriptions to a JSON file and extract channel IDs from a saved JSON file.
Configurable via a JSON file (credentials and other options).

## Requirements:

Python 3
Google API Client libraries (google-api-python-client)

## Usage:

Install the required libraries: pip install google-api-python-client
Configure a JSON file named config.json with your OAuth 2.0 credentials (refer to Google API documentation for details).
Run the script: python channel-manager.py

## Optional:

Modify the main function to process the retrieved subscriptions data (dictionary format).

## Note:

Replace the placeholder for accessing credentials from the config file with the actual key in your implementation.

This script provides a basic framework for managing YouTube subscriptions programmatically. You can extend it further to perform additional tasks based on your needs.