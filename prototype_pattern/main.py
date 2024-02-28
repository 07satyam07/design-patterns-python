import copy


class Archers:
    def __init__(self):
        self.arrows=100
        self.bow=2
        self.shelds=1

    def __str__(self):
        return f"Archer with {self.bow} bow , {self.arrows} arrows and {self.shelds} shields"


class ProtoType:
    def __init__(self,archer):
        self.archer=archer

    def get(self):
        return  copy.deepcopy(self.archer)

archer1=Archers()
prototype=ProtoType(archer1)

archer2=prototype.get()
archer3=prototype.get()

print(archer1)
print(archer2)
print(archer3)