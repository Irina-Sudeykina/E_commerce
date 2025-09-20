import os
from pathlib import Path

from src import utils

# Задаём корневой путь проекта.
root_path = Path(__file__).resolve().parents[1]
file_of_names = os.path.join(root_path, "data\\products.json")
bad_json_file = os.path.join(root_path, "data\\bad_json_file.json")


def test_read_json(category_json_file: str) -> None:
    """
    Проверка работы функции read_json,
    которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях
    :param category_json_file: Фикстура списка словарей из json файла с финансовыми операциями
    :return: список словарей с данными о финансовых транзакциях
    """
    assert utils.read_json(file_of_names) == category_json_file

    assert os.path.exists(file_of_names)

    assert utils.read_json("test") == []
    assert utils.read_json(bad_json_file) == []


def test_create_objects_from_json(category_json_file: list) -> None:
    """
    Проверка работы функции create_objects_from_json,
    которая принимает список словарей с категориями товаров
    и формирует список экземпляров класса Category
    :param category_json_file: Фикстура списка словарей из json файла с финансовыми операциями
    :return: список экземпляров класса Category
    """
    result = utils.create_objects_from_json(category_json_file)
    assert result[0].name == "Смартфоны"
    assert len(result) == 2
    assert result[0].category_count == 11
    assert result[0].product_count == 26
