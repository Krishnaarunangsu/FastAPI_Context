from abc import ABC, abstractmethod


class NotificationStrategy(ABC):

    @abstractmethod
    def send(self, recipient, message):
        pass