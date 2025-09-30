from src.base_entity import BaseEntity
from src.exceptions import ZeroQuantityProduct
from src.product import Product


class Order(BaseEntity):
    """
    Представляет заказ покупателя.
    """

    orders_count = 0

    def __init__(self, product: Product, quantity: int):
        super().__init__(name=f"Заказ №{Order.orders_count + 1}")
        self.product = product
        try:
            if quantity <= 0:
                raise ZeroQuantityProduct("Нельзя добавить заказ с нулевым количеством продукта!")
        except ZeroQuantityProduct as e:
            print(str(e))
        else:
            self.quantity = quantity
            self.total_cost = self.calculate_total()
            Order.orders_count += 1
            print("Заказ создан успешно")
        finally:
            print("Обработка создания заказа звершена")

    def __str__(self):
        return f"{self.name}. Продукт: {self.product.name}, кол-во: {self.quantity}, итого: {self.total_cost} руб."

    def calculate_total(self):
        """
        Подсчет итоговой стоимости заказа.
        """
        return self.product.price * self.quantity
