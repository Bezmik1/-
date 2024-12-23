def greet(name):
    print("Hello,",name+"!")
n=input("Введите своё имя: ")
greet(n)

def square(number):
    return number**2
n=int(input("Введите число:"))
print("Квадрат числа:",square(n))

def max_of_two(x, y):
    return max(x,y)
x=int(input("Введите 1 число:"))
y=int(input("Введите 2 число:"))
print("Большее число:",max_of_two(x,y))
