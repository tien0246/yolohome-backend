from app.core.mqtt_manager import get_mqtt_client
import random
class MQTTService:
    def __init__(self):
        self.client = get_mqtt_client()
    def start(self):
        self.client.connect()
        self.client.loop_background()
    def stop(self):
        self.client.disconnect()
    def publish(self, feed_id, data):
        value = random.randint(0, 100)
        print('Publishing {0} to {1}.'.format(value, feed_id))
        self.client.publish(feed_id, value)