def hello(name="Jake"):
    print 'the hello() function has been executed'

    def greet():
        return '\tThis is inside the greet function'

    def welcome():
        return '\tThis is inside the welcome function'

    if name == "Jake":
        return greet
    else:
        return welcome

    # print greet()
    # print welcome()
    # print "Now we are back inside hello function"


g = hello()
print g()
