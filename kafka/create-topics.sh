#!/bin/bash

# Kafka broker address
KAFKA_BROKER="kafka-0:9092"

# Function to create a Kafka topic
create_topic() {
    TOPIC_NAME=$1
    kafka-topics --create --if-not-exists --bootstrap-server $KAFKA_BROKER --partitions 3 --replication-factor 1 --topic $TOPIC_NAME
    echo "Created topic $TOPIC_NAME"
}

# Wait for Kafka to be ready
echo "Waiting for Kafka to be ready..."
cub kafka-ready -b $KAFKA_BROKER 1 20

# Create topics
create_topic "docker-messages"
create_topic "local-messages"
