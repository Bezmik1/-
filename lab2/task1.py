def greet(name):
    print("Привет,",name+"!")
n=input("Ваше имя: ")
greet(n)

def square(number):
    return number**2
n=int(input("Введите число:"))
print("Квадрат числа:",square(n))

def max_of_two(x, y):
    return max(x,y)
x=int(input("Введите первое число:"))
y=int(input("Введите второе число:"))
print("Большее число:",max_of_two(x,y))