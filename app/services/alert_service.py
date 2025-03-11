from app.core.rabbit_manager import RabbitConnection

class AlertService:
    def __init__(self):
        self.conn = RabbitConnection()
    def send_alert(self, message: str):
        self.conn.publish(message)
