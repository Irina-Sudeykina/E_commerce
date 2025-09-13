class CategoryIterator:
    def __init__(self, categoty_obj):
        self.category = categoty_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
