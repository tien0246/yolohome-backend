from app.core.mqtt_manager import *
import time
class MQTTService:
    def __init__(self):
        self.client = get_mqtt_client()
    def start(self):
        while True:
            try:
                self.client.connect()
                self.client.loop_background()
            except Exception as e:
                print(f"Error connecting to MQTT broker: {e}")
            time.sleep(10)

    def stop(self):
        self.client.disconnect()
        print("MQTT client disconnected")
    def publish(self, feed_id, data):
        with published_lock:
            published_internal.add((feed_id, str(data)))
        self.client.publish(feed_id, data)