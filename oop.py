# # objectorientedprograming
# class Fruits:
#     def __init__(self):
#         self.name = "apple"
#         self.color = "red"
#
# fruits = Fruits()
# fruits.name = "mango"
#
# print(fruits.name)
# print(fruits.color)


class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color


fruit1 = Fruits("apple","red")
fruit2 = Fruits("banana", 'yellow')

print(f"First fruit name is: {fruit1.name}")
print(f"First fruit color is: {fruit1.color}")
print(f"Second fruit name is: {fruit2.name}")
print(f"Second fruit color is: {fruit2.color}")