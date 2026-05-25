from app.strategies.base import NotificationStrategy


class EmailStrategy(NotificationStrategy):

    def send(self, recipient, message):

        return {
            "status": "SUCCESS",
            "channel": "EMAIL",
            "recipient": recipient,
            "message": f"Email sent: {message}"
        }