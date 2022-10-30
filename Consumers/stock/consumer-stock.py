import json
from kafka import KafkaConsumer

if __name__ == '__main__':
	consumer = KafkaConsumer('stock', bootstrap_servers = 'localhost:9092', api_version=(0, 10, 1), auto_offset_reset = 'earliest')
	while True:
		for message in consumer:
			print(json.loads(message.value))