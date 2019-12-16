# for x in range(0, 10):
#     print(x)

# for x in range(3):
#     print(x)

# x = 5
# while x > 0:
#     print(x)
#     x = x-1


# l = ["geeks", "for", "geeks"]
# for i in l:
#     print(i)

# Iterating over a String
# print("\nString Iteration")
# s = "Geeks"
# for x in range(len(s)):
#     print(x)


# list = ["geeks", "for", "geeks"]

# for i in range(len(list)):
#     print(list[i])

# for i in range(1, 5):
#     for j in range(i):
#         print(i, end=' ')
#     print()

# El statement continue rergesa al inicio del for loop
# for letter in 'geeksforgeeks':
#     if letter == 'e' or letter == 's':
#         continue
#     print('Current Letter :', letter)
#     var = 10

# for letter in 'geeksforgeeks':
#     # break the loop as soon it sees 'e'
#     # or 's'
#     if letter == 'e' or letter == 's':
#         break
#     print("actual", letter)

# print('Current Letter :', letter)


# for letter in 'esto es un ejemploK':
#     pass
# print('Last Letter :', letter)


# Exercise: How to print a list in reverse order (from last to first item) using while and for in loops.
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Rlista = []

# for x in lista:
#     temp = lista[len(lista) - x]
#     Rlista.append(temp)

# print(Rlista)


# dictFam = {
#     "Juan Mejia": {
#         "Nombre": "Juan Pérez Mejia",
#         "Edad": 59,
#         "Estatura": 1.68
#     },
#     "Lety Gonzalez": {
#         "Nombre": "Leticia Gonzalez Duarte",
#         "Edad": 58,
#         "Estatura": 1.55
#     }
# }
# #agregando item a un dict anidado
# dictFam["Denise"] = {"Denise", 39, 1.90}

# print(dictFam)


# print(0b1001)
# x = 3 + 4j
# print(x.imag)


# l = ["verde", "rojo", "azul"]

# if any(l) == "verde":
#     print("True")
# else:
#     print("false")

# s = "string"

# print(sorted(list(s)))


# L = [[1, 2, 3], [4, 5, 6], 7, 8, 9]
# # for list in L:
# #     for number in list:
# #         print(number, end=' ')
# nL = []

# for x in range(len(L)):
#     if type(L[x]) is list:
#         nL += L[x]
#     else:
#         nL.append(L[x])


# print(nL)


# L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], 10]
# for list in L:
#     for number in list:
#         print(number, end=' ')


# L = ['a', 'b', 'c', 'd', 'e']
# print(L[::-1])

# L = []
# L.append(0)
# L.append(1)
# L.append(4)
# L.append(9)
# L.append(16)
# print(L)

# L = [x**2 for x in range(5)]
# print(L)

# vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# L = []
# for list in vector:
#     for number in list:
#         L.append(number)

# print(L)

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# matrixT = []
# cont = 0
# for list in matrix:
#     for i in range(3):
#         print(matrix[i][cont], end=' ')
#     cont += 1
#     print()
# print(matrixT)


# L = [x**2 for x in range(5) if x**2 % 2 == 0]
# print(L)

# S = {'red', 'green', 'blue'}
# S.add('yellow')
# print(S)
# S.remove('red')
# print(S)
# randomValue = S.pop()
# print(randomValue)

# Los sets se usan basicamente para hacer operaciones como la union, interseccion, etc
# A = {'red', 'green', 'blue'}
# B = {'yellow', 'red', 'orange'}
# # interseccion
# #print(A & B)
# #Diferencia
# print(A - B)


# diccionarios

# D = {'name': 'Bob',
#      'age': 25,
#      'job': 'Dev'}

# for x in D:
#     print(x)


# carros = {
#     "Ford": {
#         "camoineta": "lobo",
#         "carro": "focus"
#     },

#     "Toyota": {
#         "camioneta": "Tacoma",
#         "carro": "camry"
#     }
# }

# print(carros["Toyota"]["camioneta"])


# for ids, modelos in carros.items():
#     print("Marca: ", ids)
#     for keys in modelos:
#         print(keys, ":", modelos[keys])


# for keys, tipos in carros.items():
#     print(keys)
#     for keys in tipos:
#         print(keys, ":", tipos[keys])
# for _ in range(-2, 4-2):
#     print(_)

# class D:
#     def __init__(self, a=2):
#         self.v = a


# d = D()

# print(d+3)


# dic = {x: x**2 for x in range(5)}
# print(dic)


# d = {x: x*3 for x in 'red'}
# print(d)

# L = ['ReD', 'GrEeN', 'BlUe']

# d = {s.lower(): s.upper() for s in L}

# print(d)

# sacando un sub diccionario

# from functools import wraps
# D = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
# selectedKeys = [0, 2, 5]

# newd = {}
# for key, values in D.items():
#     if key in selectedKeys:
#         newd.update({key: values})

# print(newd)

# Este fue mi intento
# newd = {key: values for key, values in D.items() if key in selectedKeys}
# print(newd)

# Esta es la version del tutorial
# x = {k: D[k] for k in selectedKeys}
# print(x)

# Remover elementos de un diccionario:

# D = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
# removeKeys = [0, 2, 5]

# x = {k: D[k] for k in D if k not in removeKeys}
# print(x)


# Reverse key : value

# D = {0: 'red', 1: 'green', 2: 'blue'}

# x = {D[k]: k for k in D}
# print(x)

# pasando una lista a diccionario con index como llave
# L = ['red', 'green', 'blue']
# x = {i: L[i] for i in range(len(L))}
# print(x)

# keys = ['red', 'green', 'blue']

# x = {k: 0 for k in keys}
# print(x)


# d = {(k, v): k+v for k in range(2) for v in range(2)}
# print(d)

# --------------------------------------------------------------Stings

# S = "We're open"		# Escape single quote
# print(S)
# S = "I said 'Wow!'"
# print(S)  # Escape single quotes
# S = 'I said "Wow!"'
# print(S)

# S = """String literals can
# span multiple lines.
# wow this cool"""
# print(S)

# name = "bob"
# age = 23

# print(name, " is at this point in time, ", age, " years old")


# colors = ['red', 'green', 'blue', 'yellow']
# for x in colors:
#     if x == 'blue':
#         continue
#     print(x)

# def func(a, b):
#     return a+b, a-b
# result = func(3, 2)
# print(type(result))

# name = ['Bob', 'Sam', 'Max']
# age = [25, 35, 30]

# for x, y in zip(name, age):
#     print(x, y)


# ---------------Funciones------------------

# def hello():
#     print("Hello there")


# print(hello())
# def hello(name):
#     print('Hello ', name, "!")


# print("Set name:")
# name = input()

# hello(name)

# def nameJob(name, job):
#     print(name, "works as", job)


# name = "Bob"
# job = "dev"

# nameJob(name, job)


# Keyword agruments

# def nameJob(name, job):
#     print(name, "work as", job)


# nameJob(job="dev", name="bob")


# def NargsFunc(*args):
#     L = 0
#     for i in range(len(args)):
#         L += args[i]

#     return L


# print(NargsFunc(1, 2, 3, 3, 4, 5, 6))


# t = (1, 2, 3)

# print(type(t[0]))


# def print_arguments(**kwargs):
#     print(kwargs)


# print_arguments(name='Bob', age=25, job='dev')


# def sumaresta(a, b, c, d):
#     return a+b, c-d

# #tuples unpacking
# suma, resta = sumaresta(2, 2, 2, 2)

# print(suma)


# print(print.__doc__)


# def outer(a, b):
#     def inner(c, d):
#         return c + d
#     return inner(a, b)


# result = outer(2, 4)

# print(result)

# def sumaFac(num):
#     if num:
#         return num + sumaFac(num-1)
#     else:
#         return 0


# sumaFac(5)


# x = 42          # global scope x


# def myfunc():
#     x = x + 1   # raises UnboundLocalError
#     print(x)


# myfunc()
# print(x)


# -------------------------CLAES y OBJETOS

# There are two types of attributes: Instance attributes and Class attributes.

# class Vehicule:
#     desc = "dis is a car"

#     def __init__(self, color="Amarillo"):
#         self.color = color


# class Car(Vehicule):

#     wheels = 4

#     # init con atributos para el objeto
#     def __init__(self, color="pistache", style="None"):
#         super().__init__(color)
#         self.style = style

#     # metodo de la clase carro

#     def changeColor(self, color):
#         self.color = color


# car = Car("Black", "Sedan")

# aceso y modificacion a los atributos de un objeto

# print(car.color)
# print(car.style)

# car.style = "SUV"

# print(car.style)

# car.changeColor("Rojo")

# truck = Car(style="truck")

# print(truck.color)


# ------------Decorators----------------------

# def greet():
#     def hello(name):
#         print("Hello", name)
#     return hello


# greet_user = greet()

# print(enumerate.__doc__)


# def decorate_it(func):
#     def wrapper():
#         print("Decorado antes de la funcion")
#         func()
#         print("Decorado despues de la funcion")

#     return wrapper


# @decorate_it
# def helloWorld():
#     print("Hello world!")


# ----Decorado manual
# hello_decorado = decorate_it(helloWorld)
# hello_decorado()

# helloWorld()


# ---------------------------Decorando argumentos-----------


# def decorate(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Decorada : ", end='')
#         result = func(*args, **kwargs)
#         return result
#     return wrapper


# def hello(name):
#     ''' Prints a hello + name'''
#     return "hello " + name


# print(hello.__doc___)
