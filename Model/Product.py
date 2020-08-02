from typing import Dict


class Product():

    def __init__(
        self,
        name: str,
        description: str,
        quantity: int,
        price: float,
        id: int = None
    ):
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price

    def get(self):
        return "test passed"

    def getDict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "quantity": self.quantity,
            "price": self.price
        }
