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
