# class Fruit:
#     def __init__(self, name):
#         self.name = name
#
#     def is_ready(self):
#         print(f"This {self.name} is ready to use")
#
#
# my_fruit = Fruit("apple")
# my_fruit.is_ready()
# my_fruit = Fruit("banana")
# my_fruit.is_ready()


#
# class TrafficLight:
#     def __init__(self):
#         # Устанавливаем начальный цвет светофора
#         self.current_color = "красный"
#         print(f"Светофор создан. Текущий цвет: {self.current_color}")

# def change_color(self):
#     # Проверяем текущий цвет и меняем его
#     if self.current_color == "красный":
#         self.current_color = "желтый"
#     elif self.current_color == "желтый":
#         self.current_color = "зеленый"
#     elif self.current_color == "зеленый":
#         self.current_color = "красный"
#
#     # Выводим новый цвет
#     print(f"Светофор теперь: {self.current_color}")


# Создаем объект "Светофор"
# my_light = TrafficLight()

# Меняем цвет несколько раз
# my_light.change_color()  # Должен стать желтым
# my_light.change_color()  # Должен стать зеленым
# my_light.change_color()  # Должен стать красным
# my_light.change_color()  # Должен стать желтым снова

# class Counter:
#     def __init__(self):
#         self.current_value = 0
#         print(f"the value is {self.current_value}")
#
#     def increment(self):
#         self.current_value += 1
#         print(f"The current value is {self.current_value}")
#
#
# my_value = Counter()
# my_value.increment()
# my_value.increment()
# my_value.increment()

# class Greeter:
#     def __init__(self, greeting_word):
#         self.word = greeting_word
#         print(f"The word will be {self.word}")
#     def say_hello(self, name):
#         self.name = name
#         print(f"{self.word}, {self.name}")
# first_greeter = Greeter("Good day")
# first_greeter.say_hello("Roman")
# first_greeter.say_hello("Avi")
# first_greeter.say_hello("Nian")
# second_greeter = Greeter("Hello")
# second_greeter.say_hello("Yulia")
# second_greeter.say_hello("Dana")
# second_greeter.say_hello("Eva")

class Message:
    def __init__(self, text):
        self.message_text = text
    def show_message(self):
        print(self.message_text)
first_message = Message("I love you")
first_message.show_message()

class PiggyBank:
    def __init__(self):
        self.balance = 0
        print(f"The start balance is {self.balance}")
    def add_money(self, amount):
        self.balance += amount
        print(f"Added {amount}. The total is {self.balance}")
my_piggy_bank = PiggyBank()
my_piggy_bank.add_money(10)
my_piggy_bank.add_money(5)
my_piggy_bank.add_money(20)
my_piggy_bank.add_money(2)

class Product:
    def __init__(self, name, price):
        self.product_name = name
        self.product_price = price
    def display_product(self):
        print(f"The product is {self.product_name}, the price is {self.product_price}")

first_product = Product("t-shirt",15.99)
first_product.display_product()

class Player:
    def __init__(self, name, initial_level):
        self.player_name = name
        self.level = initial_level
    def level_up(self):
        self.level += 1
        print(f"The player {self.player_name} reached level {self.level}")
player_one = Player("Roman", 5)
player_one.level_up()
player_one.level_up()
player_one.level_up()


