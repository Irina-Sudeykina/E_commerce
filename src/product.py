class Product:
    instances: list = []  # Список для хранения всех экземпляров класса

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.instances.append(self)  # Добавляем каждый новый экземпляр в список

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
                    if instance.price < new_product.get("price", 0):
                        instance.price = new_product
                    instance.quantity += new_product.get("quantity", 0)
                return instance

            return cls(
                new_product.get("name", ""),
                new_product.get("description", ""),
                new_product.get("price", 0),
                new_product.get("quantity", 0),
            )
