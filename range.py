# range()

x = range(10)
print x
x = range(2,10)
print x
print type(x)

start = 0
stop = 20
print range(start,stop,2) # step size

l = [1,2,3,4,5]
# xrange doesn't save in memory, it just generates
for num in xrange(1,6):
  print num

print list(xrange(1,6))
