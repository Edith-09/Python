# #polymorphism
# class animal:
#     def __init__(self, name=None, age=None):
#         self.name = name
#         self.age = age

# class dog(animal):
#     def speak(self):
#         return "bark"

# class cat(animal):
#     def speak(self):
#         return "meow"

# class lion(animal):
#     def speak(self):
#         return "roar"

# animals = [dog("Rex", 3), cat("Whiskers", 2), lion("Simba", 5)]
# for animal in animals:
#     print(animal.speak())
#     print(f"Name: {animal.name}, Age: {animal.age}")
# #operator overloading
# class matrix:
#     def __init__(self, data):
#         self.data = data
#     def __add__(self, other):
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # Overload the - operator
#     def __sub__(self, other):
#         return Point(self.x - other.x, self.y - other.y)

# p1 = Point(5, 3)
# p2 = Point(4, 1)

# result = p1 - p2
# print(result.x, result.y)


