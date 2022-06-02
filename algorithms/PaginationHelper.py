import math


class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return math.ceil(PaginationHelper.item_count(self) / self.items_per_page)

    def page_item_count(self, page_index):
        try:
            if page_index > 0:
                lst = []
                for i in range(0, len(self.collection), self.items_per_page):
                    lst.append(self.collection[i:i + self.items_per_page])
                return len(lst[page_index])
            else:
                return -1
        except IndexError:
            return -1

    def page_index(self, item_index):
        if 0 <= item_index < PaginationHelper.item_count(self):
            return math.floor(item_index / self.items_per_page)
        else:
            return -1
