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
 