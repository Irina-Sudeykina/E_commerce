from abc import ABC, abstractmethod


class BaseEntity(ABC):
    """Абстрактный базовый класс для представления общей логики."""

    def __init__(self, name=None):
        self.name = name

    @abstractmethod
    def calculate_total(self):
        """Метод для расчета стоимости (для разных сущностей отличается реализация)."""
        pass
