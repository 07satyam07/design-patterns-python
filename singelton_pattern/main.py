class Singleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if self._instance is not None:
            raise Exception("Singleton instance already exists.")
        # Initialization code here

# Client Code
if __name__ == "__main__":
    singleton1 = Singleton.get_instance()
    singleton2 = Singleton.get_instance()

    print(singleton1 is singleton2)  # Output: True
