import string


# volume of sphere
def vol(rad):
    return (4.0 / 3) * (3.14) * (rad**3)


print vol(6)


# checks whether a number is in a given range
def ran_check(num, low, high):
    if num in range(low, high):
        print " %s is in the range " % str(num)
    else:
        print "The number is outside the range"


print ran_check(4, 0, 8)


def ran_bool(num, low, high):
    return num in range(low, high)


print ran_bool(3, 1, 10)


# function that accepts a string and calculate
# the number of upper case and lower case letters

# Sample string: "Hello Mr. Rogers, how are you this fine Tuesday?"

def up_low(s):
    dict = {"upper": 0, "lower": 0}
    for c in s:
        if c.isupper():
            dict["upper"] += 1
        elif c.islower():
            dict["lower"] += 1
        else:
            pass
    print "Original String: ", s
    print "no. of upper case characters: ", dict["upper"]
    print "no. of lower case characters: ", dict["lower"]


s = "Hello Mr. Rogers, how are you this fine Tuesday?"
print up_low(s)

# Sample list : [1,1,1,1,1,3,3,2,2,4,5,6,6,6]
# unique list: [1,3,2,4,5,6]


def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x


print unique_list([1, 1, 1, 1, 1, 3, 3, 2, 2, 4, 5, 6, 6, 6])

# python function to multiply all functions in the list


def multiply(numbers):
    '''
    multiplies numbers in the list
    '''
    total = numbers[0]
    for x in numbers:
        total *= x
    return total


print multiply([1, 2, 3, -4])


# python function that checks whether pallindrome or not


def pallindrome(s):
    '''
    checks pallindrome or not
    '''
    return s == s[::-1]


print pallindrome("hellehhelleh")


# function to check whether a string is pangram or not
# pangrams are words or sentences containing every
# letter of the alphabet at least once

str = "The quick brown fox jumps overt the lazy dog"


def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())


print ispangram(str)
