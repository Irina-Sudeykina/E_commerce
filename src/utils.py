import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> list[dict]:
    """
    Функция принимает путь к JSON-файлу
    и возвращает список словарей с категорями товаров
    :param path: строка - путь к JSON-файлу
    :return: список словарей с категорями товаров
    """
    try:
        full_path = os.path.abspath(path)
        with open(full_path, "r", encoding="UTF-8") as file:
            try:
                data = json.load(file)
            except Exception:
                data = []
    except FileNotFoundError:
        data = []
    return data


def create_objects_from_json(data: list[dict]) -> list:
    """
    Функция принимает список словарей с категориями товаров
    и формирует список экземпляров класса Category
    :param data: список словарей с категориями товаров
    :return: список экземпляров класса Category
    """
    categories = []
    for category in data:
        praducts = []
        for product in category["products"]:
            praducts.append(Product(**product))
        category["products"] = praducts
        categories.append(Category(category["name"], category["description"], category["products"]))
    return categories
