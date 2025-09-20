import pytest


def test_lawn_grass_init(lawn_grass1, lawn_grass2) -> None:
    """
    Проверка инициации экземпляра сласса LawnGrass
    :param lawn_grass1: фикстура экземпляра класса LawnGrass - 1
    :param lawn_grass2: фикстура экземпляра класса LawnGrass - 2
    :return: Ничего не возвращает
    """
    assert lawn_grass1.name == "Газонная трава"
    assert lawn_grass1.description == "Элитная трава для газона"
    assert lawn_grass1.price == 500.0
    assert lawn_grass1.quantity == 20
    assert lawn_grass1.country == "Россия"
    assert lawn_grass1.germination_period == "7 дней"
    assert lawn_grass1.color == "Зеленый"

    assert lawn_grass2.name == "Газонная трава 2"
    assert lawn_grass2.description == "Выносливая трава"
    assert lawn_grass2.price == 450.0
    assert lawn_grass2.quantity == 15
    assert lawn_grass2.country == "США"
    assert lawn_grass2.germination_period == "5 дней"
    assert lawn_grass2.color == "Темно-зеленый"


def test_lawn_grass_add(lawn_grass1, lawn_grass2) -> None:
    """
    Проверка сложения объектов сласса LawnGrass
    :param lawn_grass1: фикстура экземпляра класса LawnGrass - 1
    :param lawn_grass2: фикстура экземпляра класса LawnGrass - 2
    :return: Ничего не возвращает
    """
    assert lawn_grass1 + lawn_grass2 == 16750.0


def test_lawn_grass_add_err(lawn_grass1) -> None:
    """
    Проверка сложения объектов сласса LawnGrass с чем-то еще
    :param lawn_grass1: фикстура экземпляра класса LawnGrass - 1
    :return: Ничего не возвращает
    """
    with pytest.raises(TypeError):
        print(lawn_grass1 + 1)
