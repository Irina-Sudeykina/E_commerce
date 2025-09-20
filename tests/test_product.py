import pytest
from unittest.mock import patch

from src.product import Product


def test_product_init(product1, product2) -> None:
    """
    Проверка инициации экземпляра сласса Product
    :param product1: фикстура экземпляра класса Product - 1
    :param product2: фикстура экземпляра класса Product - 2
    :return: Ничего не возвращает
    """
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 210000.0
    assert product2.quantity == 8


def test_product_create() -> None:
    """
    Проверка создания нового экземпляра сласса Product
    :return: Ничего не возвращает
    """
    product = Product('65" TCL 65C7K', "черный [4K UltraHD, Wi-Fi]", 99999.0, 3)
    assert product.name == '65" TCL 65C7K'
    assert product.description == "черный [4K UltraHD, Wi-Fi]"
    assert product.price == 99999.0
    assert product.quantity == 3


def test_product_new_product() -> None:
    """
    Проверка метода new_product сласса Product
    :return: Ничего не возвращает
    """
    new_product = Product.new_product(
        {
            "name": '65" LG OLED65C4RLA',
            "description": "коричневый [4K UltraHD, Wi-Fi]",
            "price": 164999.0,
            "quantity": 3,
        }
    )
    assert new_product.name == '65" LG OLED65C4RLA'
    assert new_product.description == "коричневый [4K UltraHD, Wi-Fi]"
    assert new_product.price == 164999.0
    assert new_product.quantity == 3

    new_product = Product.new_product(
        {
            "name": '65" TCL 65C7K',
            "description": "черный [4K UltraHD, Wi-Fi]",
            "price": 100999.0,
            "quantity": 3,
        }
    )
    assert new_product.name == '65" TCL 65C7K'
    assert new_product.description == "черный [4K UltraHD, Wi-Fi]"
    assert new_product.price == 100999.0
    assert new_product.quantity == 6

    Product.delete_all_instances()

    new_product = Product.new_product(
        {
            "name": '65" LG OLED65C4RLA',
            "description": "коричневый [4K UltraHD, Wi-Fi]",
            "price": 164999.0,
            "quantity": 3,
        }
    )
    assert new_product.name == '65" LG OLED65C4RLA'
    assert new_product.description == "коричневый [4K UltraHD, Wi-Fi]"
    assert new_product.price == 164999.0
    assert new_product.quantity == 3


def test_product_update_price(capsys, product1) -> None:
    """
    Проверка изменения свойства price сласса Product
    :param product1: фикстура экземпляра класса Product - 1
    :return: Ничего не возвращает
    """
    product1.price = -800
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product1.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product1.price = 195000.0
    assert product1.price == 195000.0

    with patch("builtins.input", return_value="y"):
        product1.price = 165000.0  # Попытка снизить цену
        assert product1.price == 165000.0  # Цена успешно снижена

    with patch("builtins.input", return_value="n"):
        product1.price = 145000.0  # Попытка снизить цену
        assert product1.price == 165000.0  # Цена не снижена


def test_product_str(product1) -> None:
    """
    Проверка строкового представления сласса Product
    :param product1: фикстура экземпляра класса Product - 1
    :return: Ничего не возвращает
    """
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product1, product2) -> None:
    """
    Проверка сложения объектов сласса Product
    :param product1: фикстура экземпляра класса Product - 1
    :param product2: фикстура экземпляра класса Product - 2
    :return: Ничего не возвращает
    """
    assert product1 + product2 == 2580000.0


def test_product_add_err(product1) -> None:
    """
    Проверка сложения объектов экземпляра сласса Product c чем-то еще
    :param product1: фикстура экземпляра класса Product - 1
    :return: Ничего не возвращает
    """
    with pytest.raises(TypeError):
        result = product1 + 1
