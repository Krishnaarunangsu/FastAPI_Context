from app.strategies.strategy_factory import StrategyFactory


class NotificationService:

    @staticmethod
    def process_notification(
        request_data,
        context
    ):

        strategy = StrategyFactory.get_strategy(
            request_data.type
        )

        result = strategy.send(
            request_data.recipient,
            request_data.message
        )

        # Tenant enrichment
        result["tenant"] = context["tenant"]

        # Premium logic
        if context["tenant"] == "PREMIUM":
            result["premium_support"] = True

        # Admin logic
        if context["role"] == "ADMIN":
            result["debug"] = {
                "strategy_used": request_data.type,
                "device": context["device"]
            }

        # Mobile optimization
        if context["device"] == "MOBILE":
            result["compact"] = True

        return result