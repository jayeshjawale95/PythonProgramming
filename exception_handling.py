try:
    print "sdsadasd"
    # 2 + '2'
    2 + 2
    print "asdasdsad"
except TypeError:
    print "There was a type error"
else:
    print "try was a success"
finally:
    print "finally this was printed"


def askint():
    while True:
        try:
            val = int(raw_input("Please enter in integer: "))
        except:
            print 'Looks like you did not enter an integer'
            continue
        else:
            print 'Correct, that is an integer'
            break
        finally:
            print "finally block executed!"
        print val


askint()
