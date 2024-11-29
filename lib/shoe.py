#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Brand must be a non-empty string.")
        self._brand = value.strip()

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")  # Removed period
            return
        self._size = value

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Condition must be a non-empty string.")
        self._condition = value.strip()

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
