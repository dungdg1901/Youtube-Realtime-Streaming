# Project Overview

## Goal

The goal of this project is to stream data changes from a YouTube playlist, such as likes, comments, and views, and push notifications to Telegram when these changes occur. The data will be fetched using the YouTube Data API from Google Cloud Platform (GCP), then streamed to Kafka via Confluent Console.

## Technologies Used

- YouTube Data API
- Google Cloud Platform (GCP)
- Kafka
- Confluent Console
- Telegram API

# Steps

## 1. Setup YouTube Data API Access

- Obtain API credentials from Google Cloud Platform.
- Set up access to the YouTube Data API.

## 2. Fetch Data from YouTube Playlist

- Use the YouTube Data API to fetch data from the specified playlist.
- Extract relevant information such as likes, comments, views, etc.

## 3. Set Up Kafka and Confluent Console

- Install and configure Kafka.
- Set up Confluent Console for streaming data.

## 4. Stream Data to Kafka

- Develop a script to stream data fetched from the YouTube Data API to Kafka.
- Ensure proper handling of errors and retries.

## 5. Push Notifications to Telegram

- Use the Telegram API to set up a bot for sending notifications.
- Develop logic to trigger notifications based on changes in the streamed data.

## 6. Testing and Deployment

- Test the entire pipeline to ensure data is being streamed correctly.
- Deploy the solution to a production environment.

## 7. Monitoring and Maintenance

- Implement monitoring for the streaming pipeline to detect and handle any issues.
- Regularly maintain and update the system as needed.

# Conclusion

This project aims to demonstrate the process of streaming data from YouTube playlists to Kafka and sending notifications to Telegram based on changes in the data. By following these steps, you can achieve real-time monitoring of YouTube playlist activities and receive timely notifications on your Telegram account.
