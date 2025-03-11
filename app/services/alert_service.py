from app.core.rabbit_manager import RabbitConnection

class AlertService:
    def __init__(self):
        self.conn = RabbitConnection()
    def send_alert(self, user_id: int, message: str):
        queue_name = f"alert_queue_{user_id}"
        self.conn.publish(queue_name, message)
