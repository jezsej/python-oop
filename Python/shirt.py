class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self._color = shirt_color
        self._size = shirt_size
        self._style = shirt_style
        self._price = shirt_price
    
    def change_price(self, new_price):
    
        self._price = new_price
        
    def discount(self, discount):

        return self._price * (1 - discount)