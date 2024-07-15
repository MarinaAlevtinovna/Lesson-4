#Разработать программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики,
# такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store,
# который можно будет использовать для создания различных магазинов.

class Store:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_store(self, name, address):
        print(f'Магазин {self.name} по адресу {self.address}')

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f'Добавлен товар: {item_name} с ценой {price}')

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f'Товар {item_name} удален из ассортимента')
        else:
            print(f'Товар {item_name} не найден в ассортименте')

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f'Цена товара {item_name} обновлена до {new_price}')
        else:
            print(f'Товар {item_name} не найден в ассортименте')

store1 = Store('Чебурашка', 'улица Ленина, 5')
store2 = Store('Помидорка', 'улица Путина, 79')
store3 = Store('Капот', 'улица Попова, 44, помещение 5')

store1.add_store('Чебурашка', 'Ленина, 5')
store1.add_item('Кукла Маша', 2000)
store1.add_item('Машинка Синий трактор', 1500)
store1.add_item('Мяч', 300)
store1.add_item('Коляска', 5000)

store1.get_price('Кукла Маша')
store1.remove_item('Коляска')
store1.update_price('Мяч', 500)
store1.get_price('Танк')
store1.update_price('Танк', 500)

store2.add_store('Помидорка', 'улица Путина, 79')
store2.add_item('Курица', 250)