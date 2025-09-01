import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def product1():
    """
    Фикстура экземпляра класса Product - 1
    """
    return Product(
        name = "Samsung Galaxy S23 Ultra",
        description = "256GB, Серый цвет, 200MP камера",
        price = 180000.0,
        quantity = 5
    )


@pytest.fixture
def product2():
    """
    Фикстура экземпляра класса Product - 2
    """
    return Product(
        name = "Iphone 15",
        description = "512GB, Gray space",
        price = 210000.0,
        quantity = 8
    )


@pytest.fixture
def category1():
    return Category(
        "Смартфоны", 
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products = [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        ]
    )


@pytest.fixture
def category2():
    return Category(
        "Телевизоры", 
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products = [
            Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
        ]
    )
