# tuple is immutable

l = [1,2,3]
t = (1,2,3,4,3,3,3)

print t
print len(t)

print t[0]
print t[-1]

print t.index(3)
print t.count(3)
