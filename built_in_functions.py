# map()
def fahrenheit(Temperature):
    return (9.0 / 5) * Temperature + 32


print fahrenheit(0)
temperature = [0, 22.5, 40, 100]

print map(fahrenheit, temperature)

print map(lambda T: (9.0 / 5) * T + 32, temperature)

lambda x, y: x + y

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

print map(lambda x, y, z: x + y + z, a, b, c)

print map(lambda num: num * -1, a)


# reduce()
lst = [34, 23, 24, 24, 100, 2333, 2, 11]
print max(lst)
max_find = lambda a, b: a if (a > b) else b


def max_find_func(a, b):
    if (a > b):
        return a
    else:
        return b


print max_find_func(12, 100)


print reduce(max_find, lst)


# filter

def even_check(num):
    if num % 2 == 0:
        return True
    else:
        return False


print even_check(35)

lst = range(10)
print lst

print filter(even_check, lst)

print filter(lambda num: num % 2 == 0, lst)
print filter(lambda num: num > 3, lst)


# zip()
x = [1, 2, 3]
y = [4, 5, 6]
print zip(x, y)

a = [1, 2, 3, 4, 5]
b = [2, 2, 10, 1, 1]

for pair in zip(a, b):
    print max(pair)

print map(lambda pair: max(pair), zip(a, b))


x = [1, 2, 3]
y = [4, 5, 6, 7, 8]

print zip(x, y)

d1 = {'a': 1, 'b': 2}
d2 = {'c': 4, 'd': 5}

print zip(d1, d2)
for i in d1:
    print i

print zip(d2, d1.itervalues())


def switcharoo(d1, d2):
    dout = {}
    for d1key, d2val in zip(d1, d2.itervalues()):
        dout[d1key] = d2val
    return dout


print d1

print d2

print switcharoo(d1, d2)


# enumerate
lst = ['a', 'b', 'c']

for count, item in enumerate(lst):
    print count
    print item

print "--------------------"
for i, item in enumerate(lst):
    if i >= 2:
        break
    else:
        print item


# all() and any()

lst = [True, True, True, False, False, False]
print any(lst)
print all(lst)

# complex()
print complex(2, 3)
print complex('10+2j')
