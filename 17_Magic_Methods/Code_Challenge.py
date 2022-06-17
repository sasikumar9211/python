class Store:
    def __init__(self,name):
        self.name=name
        self.items=[]
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    
    def add_item(self, name, price):
        item = {"name": name,"price":price}
        self.items.append(item)
        return f"Items added successfully"
        # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        return sum(item["price"] for item in self.items)
        # Add together all item prices in self.items and return the total.
    
    def __str__(self):
        return (f"Store name is:{self.name}")

store = Store("Wait_Rose")
print(store)

print(store.add_item("Egg",34))
print(store.add_item("Rice",60))

print(store.items)

print(store.stock_price())


