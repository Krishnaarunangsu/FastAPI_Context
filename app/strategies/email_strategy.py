from app.strategies.base import NotificationStrategy


class EmailStrategy(NotificationStrategy):

    def send(self, request_data):

        return {

            "status": "SUCCESS",

            "channel": "EMAIL",
            "recipient": request_data.recipient,
            "message": f"Email sent: {request_data.message}",
            "extra_context": {
                "weather": request_data.weather,
                "color": request_data.color
            }
        }