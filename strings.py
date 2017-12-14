print 'hello world'
print "hello world"
print "'hello world'"
print '"hello world"'
print 'Here is a new line \nand here is the second line'

s = "hello world"
print len(s)
print s[0]
print s[1]

# indexing
print s[:3] # grab everything upto 3rd index
print s[3:] # grab everything after 3rd index
print s[:] # grab everything
print s[:-1] # grab everything except last

print s[::1] # step by 1
print s[::2] # step by 2
print s[::-1] # reverse the string

letter = "z"
print letter*10

print s.upper()
print s.lower()
print s.split()
print s.split('e')
