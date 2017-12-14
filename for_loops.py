l = [1,2,3,4,5]
print l
for num in l:
  print "something! %r" %(num)

print 10%3

for num in l:
  if num % 2 == 0:
    print 'Here is an even %r' %(num)
  else:
    print 'odd number! %r' %(num)

list_sum = 0
for num in l:
  list_sum = list_sum + num
print list_sum

s = "This is a string"
for item in s:
  print item

tup = (1,2,3,4,5)
for item in tup:
  print item


l = [(2,4),(6,8),(10,12)]
print l
for tup in l:
  print tup

for (t1,t2) in l:
  print t1

d = {'k1':1,'k2':2,'k3':3}
for item in d:
  print item

# create a generator
# d.iteritems() ===>> creates tuples
for k,v in d.iteritems():
  print k

print "items"
for k,v in d.items():
  print k
