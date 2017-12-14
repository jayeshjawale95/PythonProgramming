def my_addtion_func(arg1, arg2):
    """
    Here is my docstring
    """
    print arg2 + arg1


my_addtion_func(1, 2)


def say_hello():
    print "hello"


say_hello()


def greeting(name):
    print "hello " + name


greeting("joseph")


def add_num(num1, num2):
    return num1 + num2


print add_num(3, 2)


def is_prime(num):
    """
    INPUT: A number
    OUTPUT: A print statement whether or not the number is prime
    """
    for n in range(2, num):
        if num % n == 0:
            print "not prime"
            break
    else:
        print "The number is prime"


is_prime(12)
