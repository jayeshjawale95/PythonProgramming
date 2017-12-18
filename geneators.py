# iterators and generators
import random


def gencubes(n):
    out = []
    for num in range(n):
        out.append(num ** 3)
    return out


for x in gencubes(10):
    print x

# to avoid huge memory utilisation use yield


def gencubes(n):
    for num in range(n):
        yield num ** 3


for x in gencubes(10):
    print x


print "======================"


def genfibonacchi(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        t = a
        a = b
        b += t


for num in genfibonacchi(10):
    print num

print "-------------"


def fibon(n):
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a, b = b, a + b
    return output


print fibon(10)
print "==================="


def simplegen():
    for x in range(3):
        yield x


g = simplegen()

print next(g)
print next(g)
print next(g)


s = "hello"
for let in s:
    print let

s_iter = iter(s)
print next(s_iter), next(s_iter)


n = iter([1, 2, 3, 4, 5])
print next(n)

print '-------------------------------'


def gensquares(N):
    for i in range(N):
        yield i ** 2


for x in gensquares(10):
    print x

print random.randint(1, 10)

print '====================-----------=============='


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print num


s = 'hello'

s = iter(s)

print next(s)


# generator comphrehension

my_list = [1, 2, 3, 4, 5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print item
