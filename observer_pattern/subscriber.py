class Subscriber:
    def __init__(self) -> None:
        self._messages=None
    
    @property
    def messages(self):
        return self._messages

    @messages.setter
    def messages(self,messages):
        self._messages=messages