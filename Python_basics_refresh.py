
print('Hello There!1')
print('Hello There!2')
print('Hello There!3')
'''
print('Hello There!4')
print('Hello There!5')
print('Hello There!6')
print('Hello There!7')'''


##################################

def print_name (first_name = 'First', last_name='Last'):
    print(first_name+last_name)

a = print_name

print(a())

##################################

def my_numbers(a):    
    global x
    x=7
    print(x)    
    print('My fav number is ', x)

x = 10
print(my_numbers(a=2))
print(x)

# ##################################

# # The variable a defined in outer function is global to the nested function, without being passed to the nested
def display_message(message):
    'outer function'
    a= 4
    def message_sender():
        'nested function'
        print(a)
    message_sender()
    print(a)

display_message('Python is good')

##################################

a = lambda b: b+4
print(a(4,5,6))

##################################

def ghost_number(n):
    print(n)
    return lambda f: f*n

double_num = ghost_number(2)

print(double_num(20))

##################################

# #Doc strings
def add_numbers(d,e):
    ''' Adding two numbers.

    The values must be integers'''

    return d + e

print(add_numbers(4,5))

print(add_numbers.__doc__)

##################################

# Decorators: used to add new functionality to existing objects like functions, methods and classes without modifying it's structure.

def my_decorator(function):
    def wrapper():
        myfunc = function()
        convert_uppercase = myfunc.upper()
        return convert_uppercase
    return wrapper

@my_decorator
def say_hello():
    return "hello world"

# decorate = my_decorator(say_hello) # comment this if using @my_decorator

print(say_hello())

##################################

class Instructors:
    companyName = 'Blue'

    def __init__ (self, course):
        self.course = course
        # print(self.course)
        # print(self.companyName)
        # print(Instructors.companyName)

    def printinfo(self):
        print('My company name is ', self.companyName)
        print('My course name is ', self.course)

elearning = Instructors('Python')
bls = Instructors('Django')

elearning.printinfo()
bls.printinfo()

print(elearning.course)
print(bls.course)

bls.course = 'Flask'
print(bls.course)

# del bls.course

##################################

# # Parent class
class Person:
    def __init__ (self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname (self):
        print(self.firstname, self.lastname)


florist = Person('Jane', 'Flowers')
florist.printname()

# # Child class
class Lawyers (Person):
    def __init__ (self, fname, lname, casetype):
        super().__init__(fname, lname) # or Person.__init__(self, fname, lname)
        self.casetype = casetype
        # self.firstname = fname
        # self.lastname = lname

    def printinfo (self):
        print('Hello my name is ', self.firstname, self.lastname)

happy_lawyers = Lawyers('Jack', 'Smiley', 'land')
happy_lawyers.printinfo()
happy_lawyers.printname()

print(happy_lawyers.casetype)


# Polymorphism

#E.g.
print(len('Hello'))
print(len([20,40,80]))

#E.g.
def addNumbers(a,b,c=1):
    return a + b + c

print(addNumbers(8,9))
print(addNumbers(8,9,4))

# #E.g.
class UK():
    def capital_city(self):
        print("London is the capital of UK")

    def language(self):
        print("English is the primary language ")

class Spain():
    def capital_city(self):
        print("Madrid is the capital of Spain")

    def language(self):
        print("Spanish is the primary language ")

queen = UK()
queen.capital_city()

zara = Spain()
zara.capital_city()

for country in (queen, zara):
    country.capital_city()
    country.language()


def europe(eu):
    eu.capital_city()

europe(queen)
europe(zara)



# Encapsulation

# Without encapsulation all methods are public, speed can be changed
class Cars:
    def __init__ (self, speed, color):
        self.speed = speed
        self.color = color

    def set_speed (self, value):
        self.speed = value

    def get_speed (self):
        return self.speed

ford = Cars(250, 'green')
nissan = Cars(300, 'red')
toyota = Cars(350, 'blue')


ford.set_speed(450)
print(ford.get_speed())
ford.speed = 500
print(ford.get_speed())

# With encapsulation methods can be made private, prefix like self.__

class Cars:
    def __init__ (self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_speed (self, value):
        self.__speed = value

    def get_speed (self):
        return self.__speed

ford = Cars(250, 'green')
nissan = Cars(300, 'red')
toyota = Cars(350, 'blue')

# print(ford.speed)
print(ford.get_speed())
ford.speed = 500 # doesn't changes value of speed
ford.__speed = 500 # doesn't changes value of speed
print(ford.get_speed())
ford.set_speed(500) # this changes value of speed
print(ford.get_speed())


# Abstraction

#Without abstraction
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Square (Shape):
    def __init__(self, side):
        self.side = side

myshape = Shape()

# With abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square (Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side
    
    def perimeter(self):
        return 4*self.__side

# myshape = Shape() # cannot be instantiated because of abstraction

mysquare = Square(5)
print(mysquare.area())
print(mysquare.perimeter())


##################################

# Package 'healthy'

import healthy.foo
healthy.foo.fruits('Apples')

from healthy import foo
foo.fruits('Apples')

import healthy
m = dir(healthy)
print(m)

##################################

# Exception handling

#E.g.
x=2
try:
    print(x)

except:
    print('Variable is not defined')

else: # Runs if no error
    print('Printed successfully')

finally: # Runs regardless of whether an error or not
    print('You might have got an error')

#E.g.
try:
    n = int('incorrect input')
except ValueError:
    print('No valid integer provided')

#E.g.
try:
    n = 12/int(input('Enter a whole number: '))
    print('The value of your number is ', n)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
finally:
    print('Hope you entered a valid whole number')

##################################

