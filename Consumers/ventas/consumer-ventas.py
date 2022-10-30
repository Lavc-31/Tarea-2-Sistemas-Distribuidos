import json
from kafka import KafkaConsumer


if __name__ == '__main__':
	consumer = KafkaConsumer('stock', bootstrap_servers = 'localhost:9092', api_version=(0, 10, 1), auto_offset_reset = 'earliest')
	f = open('ventas.txt', 'w')
	while True:
		for message in consumer:
			mensaje = json.loads(message.value.decode())
			print(mensaje)
			cliente = mensaje["cliente"]
			cantidad = mensaje["cantidad"]
			hora = mensaje["hora"]
			stock_s = mensaje["stock_s"]
			ubicacion = mensaje["ubicacion"]

			f.write(cliente+","+cantidad+","+ubicacion+"\n")
	f.close()
