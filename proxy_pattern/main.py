from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self,lol):
        print(f"RealSubject: Handling request.{lol}")

class Proxy(Subject):
    def __init__(self):
        self._real_subject = None

    def request(self,lol):
        if self._real_subject is None:
            self._real_subject = RealSubject()
        self._real_subject.request(lol)

if __name__ == "__main__":
    proxy = Proxy()
    proxy.request(5)
    proxy.request(6)
