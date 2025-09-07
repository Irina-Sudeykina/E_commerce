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
