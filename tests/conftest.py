import pytest

from src.product import Product
# from src.user import User


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


# @pytest.fixture
# def task():
    # return Task("Купить огурцы", "Купить огурцы для салата",created_at="20.04.2024")
