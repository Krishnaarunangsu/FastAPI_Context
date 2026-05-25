from app.strategies.base import NotificationStrategy


class PushStrategy(NotificationStrategy):
    def send(self, recipient, message):
        return {
            "status": "SUCCESS",
            "channel": "PUSH",
            "recipient": recipient,
            "message": f"PUSH sent: {message}"
        }