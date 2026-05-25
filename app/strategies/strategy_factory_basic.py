from app.strategies.email_strategy import EmailStrategy
from app.strategies.sms_strategy import SMSStrategy
from app.strategies.push_strategy import PushStrategy

class StrategyFactory:

    @staticmethod
    def get_strategy(notification_type: str):
        strategies = {
            "EMAIL": EmailStrategy(),
            "SMS": SMSStrategy(),
            "PUSH": PushStrategy(),
        }

        strategy = strategies.get(notification_type)
        if not strategy:
            raise ValueError(f"Unknown notification type: {notification_type}")
        return strategy
