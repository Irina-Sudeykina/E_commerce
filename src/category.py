from src.base_entity import BaseEntity
from src.exceptions import ZeroQuantityProduct
from src.product import Product


class Category(BaseEntity):
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        full_cnt = 0
        for product in self.__products:
            full_cnt += product.quantity

        return f"{self.name}, количество продуктов: {full_cnt} шт."

    @property
    def products_in_list(self):
        return self.__products

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    def add_product(self, product: Product):
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityProduct("Нельзя добавить продукт с нулевым количеством!")
            except ZeroQuantityProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Продукт добавлен успешно")
            finally:
                print("Обработка добавления продукта звершена")
        else:
            raise TypeError("Переданный аргумент не является объектом Product!")

    def calculate_total(self):
        """
        Подсчет суммарного количества продуктов в категории.
        """
        return sum([p.quantity for p in self.__products]) if self.__products else 0

    def middle_price(self):
        """
        Подсчет среднего ценника всех товаров
        """
        try:
            return round(sum(product.price for product in self.__products) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
