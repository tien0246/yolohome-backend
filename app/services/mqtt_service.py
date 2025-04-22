from app.core.mqtt_manager import *
class MQTTService:
    def __init__(self):
        self.client = get_mqtt_client()
    def start(self):
        self.client.connect()
        self.client.loop_background()
    def stop(self):
        self.client.disconnect()
        print("MQTT client disconnected")
    def publish(self, feed_id, data):
        with published_lock:
            published_internal.add((feed_id, str(data)))
        self.client.publish(feed_id, data)