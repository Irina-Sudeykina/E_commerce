# Проект "E_commerce" - электронная коммерция

## Описание:
 Проект "E_commerce" - это проект на Python, 
 содержащий ядро для интернет-магазина
 
## Установка:
 1. Клонируйте репозиторий:
 ```
 git clone https://github.com/Irina-Sudeykina/E_commerce.git
 
 ```

 1. Установите зависимости:
 ```
 pip install -r requirements.txt
 ```

## Использование:
  
 ### Класс **Product**
 Для класса Product определены следующие свойства: 
     название (name),
     описание (description),
     цена (price),
     количество в наличии (quantity).

 #### Пример использования: 
 ```
from src.product import Product

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

print(product1.name)
print(product1.description)
print(product1.price)
print(product1.quantity)
 ```
 #### Пример работы:
 ```
Samsung Galaxy S23 Ultra
256GB, Серый цвет, 200MP камера
180000.0
5
 ```


 ### Класс **Category**
 Для класса Category определены следующие свойства: 
     название (name),
     описание (description),
     список товаров категории (products).
 А так же:
     количество категорий (category_count),
     количество товаров (product_count)

 #### Пример использования: 
 ```
from src.product import Product
from src.category import Category

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

print(category1.name)
print(category1.description)
print(len(category1.products))
print(category1.category_count)
print(category1.product_count)
 ```
 #### Пример работы:
 ```
Смартфоны
Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни
3
1
3
 ```


 ### Класс **Smartphone**
 Наследник класса Product
 Класс Smartphone расширен атрибутами: 
     производительность (efficiency),
     модель (model),
     объем встроенной памяти (memory),
     цвет (color).

 #### Пример использования: 
 ```
from src.smartphone import Smartphone

smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )

print(smartphone1.name)
print(smartphone1.description)
print(smartphone1.price)
print(smartphone1.quantity)
print(smartphone1.efficiency)
print(smartphone1.model)
print(smartphone1.memory)
print(smartphone1.color)
 ```
 #### Пример работы:
 ```
Samsung Galaxy S23 Ultra
256GB, Серый цвет, 200MP камера
180000.0
5
95.5
S23 Ultra
256
Серый
 ```


 ### Класс **LawnGrass**
 Наследник класса Product
 Класс LawnGrass расширен атрибутами: 
     страна-производитель (country),
     срок прорастания (germination_period),
     цвет (color).

 #### Пример использования: 
 ```
from src.lawn_grass import LawnGrass

grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

print(grass1.name)
print(grass1.description)
print(grass1.price)
print(grass1.quantity)
print(grass1.country)
print(grass1.germination_period)
print(grass1.color)
 ```
 #### Пример работы:
 ```
Газонная трава
Элитная трава для газона
500.0
20
Россия
7 дней
Зеленый
 ```


 ### Функция **read_json**(path: str) -> list[dict]
 Функция принимает путь к JSON-файлу
 и возвращает список словарей с категорями товаров

 #### Пример использования: 
 ```
row_data = utils.read_json("data/products.json")
print(row_data)
 ```
 #### Пример работы:
 ```
[
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
 ```


 ### Функция **create_objects_from_json**(data: list[dict]) -> list
 Функция принимает список словарей с категориями товаров
 и формирует список экземпляров класса Category

 #### Пример использования: 
 ```
row_data = utils.read_json("data/products.json")

categories_data = utils.create_objects_from_json(row_data)
print(categories_data)
print(categories_data[0].name)
print(categories_data[0].products)
print(categories_data[0].products[0].name)
 ```
 #### Пример работы:
 ```
Смартфоны
[
    <src.product.Product object at 0x000002CEEF09BE10>, 
    <src.product.Product object at 0x000002CEEF6AE8D0>, 
    <src.product.Product object at 0x000002CEEF659D00>
]
Samsung Galaxy C23 Ultra
 ```


 ## Тестирование:
Проект покрыт тестами фреймворка pytest. Для их запуска выполните команду:
```
pytest
```
Для выгрузки отчета о покрытии проекта тестами выполните команду:
```
pytest --cov=src --cov-report=html
```


 ## Документация:

 ## Лицензия:
 Проект распространяется под [лицензией MIT](LICENSE).
 