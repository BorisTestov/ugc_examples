import logging
import os
import time

from kafka import KafkaConsumer, KafkaProducer

logging.basicConfig(level=logging.WARNING)

if os.environ.get("LOCAL", "true") == "false":
    time.sleep(5)  # Raw wait until kafka is ready
    topic = "docker-messages"
    bootstrap_servers = ["kafka-0:9092"]
else:
    topic = "local-messages"
    bootstrap_servers = ["localhost:9093"]

logging.basicConfig(level=logging.INFO)

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
)

logging.warning("Sending message to Kafka")
future = producer.send(topic, value=b"my message from python", key=b"python-message")
result = future.get(timeout=60)

logging.warning("Message sent to Kafka")

producer.close()

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset="earliest",
    group_id="echo-messages-to-stdout",
)

logging.warning("Consuming messages from Kafka")

try:
    for message in consumer:
        decoded_message = message.value.decode("utf-8")
        logging.warning(f"Message: {decoded_message}")
        break
except Exception as e:
    logging.exception(e)
finally:
    consumer.close()
    logging.warning("Consumer closed")
