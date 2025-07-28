# Пример создания класса и объекта
# class Dog: # Всё что ниже - это схема класса Dog
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         print(f"{self.name} лает: 'Гав-гав!'")
#
# # Создание экземпляра класса Dog
# my_dog = Dog("Бобик", 3)
#
# # Вызов метода объекта
# my_dog.bark()
# print(f"{my_dog.name} имеет {my_dog.age} года.")

# class Car:
#     def __init__(self, brand, year): # это параметры функции init
#         self.car_brand = brand # это атрибуты будущего объекта my_car1
#         self.car_year = year
#
#     def start(self): # метод start
#         print(f"Машина {self.car_brand} заведена! Она у меня {self.car_year} года!")
#     def age(self):
#         current_age = 2025 - self.car_year
#         print(f"The current age of {self.car_brand} is {current_age} years")
#
# my_car1 = Car("Toyota", 2020)# это объект, значения которого предаются в параметры
# my_car1.start()
# my_car1.age()

class Book:
    def __init__(self, book, author):
        self.book_title = book
        self.book_author = author
    def display_info(self):
        print(f"The name of this book: {self.book_title}, the author - {self.book_author} ")

my_book = Book("War and Peace", "Tolstoy")
my_book.display_info()

class Point:
    def __init__(self, x, y):
        self.coord_x = x
        self.coord_y = y
        print(f"Точка создана в ({self.coord_x}, {self.coord_y})")
    def move_by(self, dx, dy):
        self.coord_x += dx
        self.coord_y += dy
        print(f"Точка перемещена на ({dx}, {dy}).")

    def get_coordinates(self):
        return (self.coord_x, self.coord_y)
my_point= Point(5,10)
my_point.move_by(2,-3)
current_coords = my_point.get_coordinates()
print(f"Новые координаты точки: {current_coords}")







