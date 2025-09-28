import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawn_grass import LawnGrass
from src.order import Order
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def product1():
    """
    Фикстура экземпляра класса Product - 1
    """
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def product2():
    """
    Фикстура экземпляра класса Product - 2
    """
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def product3():
    """
    Фикстура экземпляра класса Product - 3
    """
    return Product(name='65" TCL 65C7K', description="черный [4K UltraHD, Wi-Fi]", price=99999.0, quantity=3)


@pytest.fixture
def category1():
    """
    Фикстура экземпляра класса Category - 1
    """
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def category2():
    """
    Фикстура экземпляра класса Category - 2
    """
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )


@pytest.fixture
def category_json_file():
    """
    Фикстура списка словарей из json файла с категориями товаров
    :return: список финансовых операций
    """
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации,"
            + " но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром,"
            + " станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]


@pytest.fixture
def category_iterator(category1):
    """
    Фикстура экземпляра сласса CategoryIterator для класса Category - 1
    """
    return CategoryIterator(category1)


@pytest.fixture
def smartphone1():
    """
    Фикстура экземпляра класса Smartphone - 1
    """
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый",
    )


@pytest.fixture
def smartphone2():
    """
    Фикстура экземпляра класса Smartphone - 2
    """
    return Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space",
    )


@pytest.fixture
def lawn_grass1():
    """
    Фикстура экземпляра класса LawnGrass - 1
    """
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )


@pytest.fixture
def lawn_grass2():
    """
    Фикстура экземпляра класса LawnGrass - 2
    """
    return LawnGrass(
        name="Газонная трава 2",
        description="Выносливая трава",
        price=450.0,
        quantity=15,
        country="США",
        germination_period="5 дней",
        color="Темно-зеленый",
    )


@pytest.fixture
def order1():
    """
    Фикстура экземпляра класса Order - 1
    """
    return Order(Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14), 2)


@pytest.fixture
def category_without_product():
    """
    Фикстура экземпляра класса Category без продуктов
    """
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[],
    )
