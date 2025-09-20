import pytest

def test_smartphone_init(smartphone1, smartphone2) -> None:
    """
    Проверка инициации экземпляра сласса Smartphone
    :param smartphone1: фикстура экземпляра класса Smartphone - 1
    :param smartphone2: фикстура экземпляра класса Smartphone - 2
    :return: Ничего не возвращает
    """
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"

    assert smartphone2.name == "Iphone 15"
    assert smartphone2.description == "512GB, Gray space"
    assert smartphone2.price == 210000.0
    assert smartphone2.quantity == 8
    assert smartphone2.efficiency == 98.2
    assert smartphone2.model == "15"
    assert smartphone2.memory == 512
    assert smartphone2.color == "Gray space"


def test_smartphone_add(smartphone1, smartphone2) -> None:
    """
    Проверка сложения объектов сласса Smartphone
    :param smartphone1: фикстура экземпляра класса Smartphone - 1
    :param smartphone2: фикстура экземпляра класса Smartphone - 2
    :return: Ничего не возвращает
    """
    assert smartphone1 + smartphone2 == 2580000.0


def test_smartphone_add_err(smartphone1) -> None:
    """
    Проверка сложения объектов сласса Smartphone с чем-то еще
    :param smartphone1: фикстура экземпляра класса Smartphone - 1
    :return: Ничего не возвращает
    """
    with pytest.raises(TypeError):
        result = smartphone1 + 1
