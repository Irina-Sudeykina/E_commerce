from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    instances: list = []  # Список для хранения всех экземпляров класса

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.instances.append(self)  # Добавляем каждый новый экземпляр в список
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) == Product:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def delete_all_instances(cls):
        while len(cls.instances) > 0:
            cls.instances.pop()  # Прямой вызов pop(), без переменной

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        else:
            if self.__price > new_price:
                is_update_price = input("Подтвердите понижение цены (y/n):\n")
                if is_update_price.lower() == "y":
                    self.__price = new_price
                else:
                    return
            else:
                self.__price = new_price

    @classmethod
    def new_product(cls, new_product: dict):
        if not cls.instances:
            return cls(
                new_product.get("name", ""),
                new_product.get("description", ""),
                new_product.get("price", 0),
                new_product.get("quantity", 0),
            )
        else:
            for instance in cls.instances:
                if instance.name == new_product.get("name", ""):
                    if instance.__price < new_product.get("price", 0):
                        instance.__price = new_product.get("price", 0)
                    instance.quantity += new_product.get("quantity", 0)
                    return instance

            return cls(
                new_product.get("name", ""),
                new_product.get("description", ""),
                new_product.get("price", 0),
                new_product.get("quantity", 0),
            )
