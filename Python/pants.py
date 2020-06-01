"""
Write a Pants class with the following characteristics:

the class name should be Pants
the class attributes should include
color
waist_size
length
price
the class should have an init function that initializes all of the attributes
the class should have two methods
change_price() a method to change the price attribute
discount() to calculate a discount
"""

class Pants:

    def __init__(self, color, waist_size,length,price):
        self._color = color
        self._waist_size = waist_size
        self._length = length
        self._price = price

    def change_price(self, new_price):
        self._price = new_price

    def discount(self, discount):
        return self._price * (1 - discount)