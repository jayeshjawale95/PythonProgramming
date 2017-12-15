lst = [1, 2, 3]
print lst.count(2)

print type(1)


def square(num):
    return num ** 2


print type(square)


class Sample(object):
    pass


x = Sample()
print type(x)


class Dog(object):
    # class object attribute
    species = 'mammal'

    def __init__(self, breed, name, fur=True):
        self.breed = breed
        self.name = name
        self.fur = fur


sam = Dog(breed='Huskie', name="Sammy")

print sam.breed, sam.species, sam.fur


class Circle(object):

    # class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        pass

    def area(self):
        return (self.radius**2) * self.pi

    def set_radius(self, new_radius):
        """
        method takes in a radius and resets the radius of the circle
        """
        self.radius = new_radius

    def get_radius(self):
        return self.radius


c = Circle(radius=10)

print c.pi, c.radius, c.area()

c.set_radius(100)

print c.radius, c.area()

print c.get_radius()


class Animal(object):
    def __init__(self):
        print "Animal Created"
        pass

    def whoAmI(self):
        print "Animal"

    def eat(self):
        print "Eating"


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print "Dog Created"

    def whoAmI(self):
        print "Dog"

    def bark(self):
        print "woof"


a = Animal()
d = Dog()

d.whoAmI()
d.eat()
d.bark()


class Book(object):
    def __init__(self, title, author, pages):
        print "A book has been created"
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages %s " %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print "A book is gone"


b = Book("Python", "James", 100)
print b
print len(b)
del b


class Line(object):
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return float((y2 - y1)) / (x2 - x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print li.distance()
print li.slope()


class Cylinder(object):
    """docstring for Cylinder"""
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * (3.14) * (self.radius)**2

    def surface_area(self):
        top = (3.14) * (self.radius)**2
        return 2 * top + 2 * 3.14 * self.radius * self.height


c = Cylinder(2, 3)
print c.volume()
print c.surface_area()
