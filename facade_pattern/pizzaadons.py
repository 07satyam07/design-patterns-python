class PizzaAdons:
    _instance=None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance=cls()

        return cls._instance

    def __init__(self):
        if self._instance:
            raise Exception("Already an instance is present of this calss")

        self.crust=["thin","thick"]
        self.addons=["tomato","onion"]

    def get_menu(self):
        return f"Available addons : {'.'.join(self.addons)} and Available crust :{','.join(self.crust)}"





