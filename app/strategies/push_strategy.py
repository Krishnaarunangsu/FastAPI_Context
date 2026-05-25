from app.strategies.base import NotificationStrategy


class PushStrategy(NotificationStrategy):

    def send(self, request_data):

        return {
            "status": "SUCCESS",
            "channel": "PUSH",
            "recipient": request_data.recipient,
            "message": f"Push sent: {request_data.message}",
            "extra_context": {
                "clothes": request_data.clothes
            }
        }