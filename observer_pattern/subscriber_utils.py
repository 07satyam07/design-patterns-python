from messages import Messages
from subscriber import Subscriber

class SubscriberUtils(Messages):
    def __init__(self) -> None:
        super().__init__()
        self.subscribers = set()
    
    @property
    def messages(self):
        return self._messages
    
    @messages.setter
    def messages(self, messages):
        self._messages = messages
        self.refresh()
    
    def refresh(self):
        for subscriber in self.subscribers:
            subscriber.messages = self.messages

    def update_subscriber(self, subscriber: Subscriber):
        subscriber.messages = self.messages

    def add_subscriber(self, subscriber: Subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.add(subscriber)
            self.update_subscriber(subscriber)
    
    def remove_subscriber(self, subscriber: Subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)
