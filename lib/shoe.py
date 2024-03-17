#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self._brand = brand
        self._size = size
    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, value):
        self._brand = value
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        self._size = value
        if not isinstance(value,int):
            print("size must be an integer")
            return
        self._size = value
    def cobble(self):
        print("Your shoe is as good as new!")    
        self.condition = "New"    
            

    