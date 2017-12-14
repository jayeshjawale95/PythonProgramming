def square(num):
    result = num**2
    return result


print square(2)


def square(num):
    return num**2


print square(2)


square = lambda num: num**2

print square(2)

# check if a number is even
even = lambda num: num % 2 == 0

print even(4)


def even(num):
    return num % 2 == 0


print even(5)

# grabs the first character of a string
first = lambda s: s[0]


print first("hello")


def adder(x, y):
    return x + y


adder = lambda x, y: x + y

print adder(30,30)


length_str = lambda strin: len(strin)

print len("jayesh jawale")
