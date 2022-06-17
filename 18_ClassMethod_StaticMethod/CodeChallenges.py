class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    def __repr__(self):
        return f"{self.name}"

    @classmethod
    def franchise(cls, store):
        return cls(f"{store.name} - Franchise")
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        return f"{store.name}, total stock price: {store.stock_price()}"
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'


store = Store("Amazon")
store.add_item("Keyboard",160)

print(Store.franchise(store))

print(Store.store_details(store))


store2 = Store("JL")
store2.add_item("Mouse",200)

print(Store.franchise(store2).name)

print(Store.store_details(store2))