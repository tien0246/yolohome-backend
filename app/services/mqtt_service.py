from app.core.mqtt_manager import get_mqtt_client

class MQTTService:
    def __init__(self):
        self.client = get_mqtt_client()
    def start(self):
        self.client.on_connect()
        self.client.loop_background()
    def stop(self):
        self.client.disconnect()
    def publish(self, feed_id, data):
        print(f"Publishing to {feed_id}: {data}")
        feed = self.client.feeds(feed_id)
        self.client.send_data(feed.key, data)