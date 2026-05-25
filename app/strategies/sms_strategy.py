from app.strategies.base import NotificationStrategy


class SMSStrategy(NotificationStrategy):
    def send(self, recipient, message):
        """

        :param recipient:
        :param message:
        :return:
        """
        return {
            "status": "SUCCESS",
            "channel": "SMS",
            "recipient": recipient,
            "message": f"SMS sent: {message}"
        }