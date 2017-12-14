lst = []
for letter in 'word':
    lst.append(letter)
print lst

# list comprehension
lst = [letter for letter in 'word']
print lst

lst = [x**2 for x in xrange(0, 11)]
print lst

lst = []
for number in range(11):
    if number % 2 == 0:
        lst.append(number)
print lst

l = [number for number in xrange(0,11) if number%2 == 0]
print l

celsius = [0,10,20.1,34.5]

fahrenheit = [ (temp*(9/5.0) + 32) for temp in celsius]
print fahrenheit
