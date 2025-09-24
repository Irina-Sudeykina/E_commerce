import pytest


def test_category_init(category1, category2) -> None:
    """
    Проверка инициализации класса Category
    :param category1: фикстура экземпляра класса Category - 1
    :param category2: фикстура экземпляра класса Category - 2
    :return: ничего не возвращает
    """
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products_in_list) == 3

    assert category2.name == "Телевизоры"
    assert (
        category2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(category2.products_in_list) == 1

    assert category1.category_count == 2
    assert category2.product_count == 4


def test_category_products_property(category1) -> None:
    """
    Проверка вывода свойства products класса Category
    :param category1: фикстура экземпляра класса Category - 1
    :return: ничего не возвращает
    """
    print(category1.products)
    assert category1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_category_add_product(category2, product3) -> None:
    """
    Проверка геттера add_product класса Category
    :param category2: фикстура экземпляра класса Category - 2
    :param product3: Фикстура экземпляра класса Product - 3
    :return: ничего не возвращает
    """
    assert len(category2.products_in_list) == 1
    category2.add_product(product3)
    print(category2.products)
    assert len(category2.products_in_list) == 2


def test_category_str(category1) -> None:
    """
    Проверка строкового представления класса Category
    :param category1: фикстура экземпляра класса Category - 1
    :return: ничего не возвращает
    """
    assert str(category1) == "Смартфоны, количество продуктов: 27 шт."


def test_product_iterator(category_iterator) -> None:
    """
    Проверка класса CategoryIterator
    :param category_iterator: Фикстура экземпляра сласса CategoryIterator
    :return: ничего не возвращает
    """
    iter(category_iterator)
    category_iterator.index == 0
    assert next(category_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(category_iterator).name == "Iphone 15"
    assert next(category_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(category_iterator)


def test_category_add_product_err(category2) -> None:
    """
    Проверка геттера add_product класса Category
    :param category2: фикстура экземпляра класса Category - 2
    :return: ничего не возвращает
    """
    with pytest.raises(TypeError):
        category2.add_product(1)


def test_category_add_product_smartphone(category1, smartphone1):
    """
    Проверка геттера add_product класса Smartphone
    :param category1: фикстура экземпляра класса Category - 1
    :param smartphone1: фикстура экземпляра класса Smartphone - 1
    :return: ничего не возвращает
    """
    category1.add_product(smartphone1)
    assert category1.products_in_list[-1].name == "Samsung Galaxy S23 Ultra"


def test_category_add_product_lawn_grass(category2, lawn_grass1):
    """
    Проверка геттера add_product класса LawnGrass
    :param category2: фикстура экземпляра класса Category - 2
    :param lawn_grass1: фикстура экземпляра класса LawnGrass - 1
    :return: ничего не возвращает
    """
    category2.add_product(lawn_grass1)
    assert category2.products_in_list[-1].name == "Газонная трава"


def test_category_calculate_total(category1):
    """
    Проверка метода calculate_total класса Category
    :param category1: фикстура экземпляра класса Category - 1
    :return: ничего не возвращает
    """
    assert category1.calculate_total() == 27
