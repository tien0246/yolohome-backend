from app.core.rabbit_manager import RabbitConnection

class AlertService:
    def __init__(self):
        self.conn = RabbitConnection()
    def send_alert(self, user_id, message):
        self.conn.publish(f"alert_queue_{user_id}", message)
