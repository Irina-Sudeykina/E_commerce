from src.order import Order
from src.product import Product


def test_order_init(order1):
    """
    Проверка инициализации класса Order
    :param order1: фикстура экземпляра класса Order - 1
    :return: ничего не возвращает
    """
    assert order1.name == "Заказ №1"
    assert order1.product.name == "Xiaomi Redmi Note 11"
    assert order1.product.description == "1024GB, Синий"
    assert order1.product.price == 31000.0
    assert order1.product.quantity == 14
    assert order1.quantity == 2
    assert order1.total_cost == 62000.0
    assert order1.orders_count == 1


def test_order_str(order1):
    """
    Проверка строкового представления класса Order
    :param order1: фикстура экземпляра класса Order - 1
    :return: ничего не возвращает
    """
    assert str(order1) == "Заказ №2. Продукт: Xiaomi Redmi Note 11, кол-во: 2, итого: 62000.0 руб."


def test_order_custom_exception(capsys, order1):
    """
    Проверка обработки пользовательской ошибки ZeroQuantityProduct класса Order
    :param order1: фикстура экземпляра класса Order - 1
    :return: ничего не возвращает
    """
    Order(Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14), 0)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Нельзя добавить заказ с нулевым количеством продукта!"
    assert message.out.strip().split("\n")[-1] == "Обработка создания заказа звершена"

    Order(Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14), 2)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Заказ создан успешно"
    assert message.out.strip().split("\n")[-1] == "Обработка создания заказа звершена"
