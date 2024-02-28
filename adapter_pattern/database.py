class DbConnection:
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.db_conn="connected"

    def write_currency(self,amount):
        print(f"Wrote 1 row of  ${amount}")

db=DbConnection()