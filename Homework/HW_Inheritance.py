# Create a class Product with properties name, price, and quantity. 
# Create a child class Book that inherits from Product and 
# adds a property author and a method called read that prints information about the book.

class Product(object):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f'Information about the book:\nName: {self.name},\nPrice: {self.price},\nQuantity: {self.quantity},\nAuthor: {self.author}')

new_book = Book('Harry Potter','700','2','Rowling')
new_book.read()


# Create a class Restaurant with properties name, cuisine, and menu. 
# The menu property should be a dictionary with
# keys being the dish name and values being the price. 

# Create a child class FastFood that inherits from Restaurant and adds a property drive_thru
# (a boolean indicating whether the restaurant has a drive-thru or not)
# and a method called order, which takes in the dish name and quantity
# and returns the total cost of the order.

# The method should also update the menu dictionary to subtract the ordered 
# quantity from the available quantity. 

# If the dish is not available or if the requested quantity is greater than 
# the available quantity, the method should return a message indicating that 
# the order cannot be fulfilled.

class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu

class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru
        drive_thru = bool

    def order(self, dish_name, quantity):
        if dish_name in self.menu:
            price = self.menu[dish_name]['price']
            available_quantity = self.menu[dish_name]['quantity']
            if quantity <= available_quantity:
                total_cost = price * quantity
                self.menu[dish_name]['quantity'] -= quantity
                return f'Total cost is {total_cost}'
            else:
                return f'{dish_name} is NOT available right now'
        else:
            return f'The {dish_name} is NOT on the menu'
    

menu =  {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5)) # 25
print(mc.order('burger', 15)) # Requested quantity not available
print(mc.order('soup', 5)) # Dish not available