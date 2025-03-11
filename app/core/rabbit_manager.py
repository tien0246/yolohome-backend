import pika
from app.utils.config import config

class RabbitConnection:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.URLParameters(config.rabbitmq_url))
        self.channel = self.connection.channel()
    def publish(self, queue_name, message):
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.channel.basic_publish("", queue_name, message, pika.BasicProperties(delivery_mode=2))
    def close(self):
        self.connection.close()
