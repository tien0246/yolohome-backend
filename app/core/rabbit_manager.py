import pika
from app.utils.config import config

class RabbitConnection:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.URLParameters(config.rabbitmq_url))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="alert_queue", durable=True)
    def publish(self, message: str):
        self.channel.basic_publish(exchange="", routing_key="alert_queue", body=message, properties=pika.BasicProperties(delivery_mode=2))
    def close(self):
        self.connection.close()
