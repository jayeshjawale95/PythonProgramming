x = 0
while x < 10:
  print 'x is currently: ',x
  x += 1

print "============"

x = 0
while x < 10:
  print 'x is currently: ', x
  x += 1
else:
  print 'all done!'

print "============"

# break, continue and pass
x = 0
while x < 10:
  print 'x is currently: ',x
  print 'x is still less than 10, adding 1 to x'
  x += 1
  if x==3:
    print 'hey x equals 3!'
    break
  else:
    print 'continuing...'
    continue
