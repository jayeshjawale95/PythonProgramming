def func():
    return 1


print func()
s = 'This is a global variable'


def func():
    print locals()


print func()
print globals().keys()
print globals()['s']


def hello(name='Jake'):
    return 'hello ' + name


print hello()

greet = hello
print greet

del hello
# hello()
print greet()
