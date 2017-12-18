# counter
from collections import Counter
# default dictionary
from collections import defaultdict
# ordered dictionary
from collections import OrderedDict
# namedtuple
from collections import namedtuple

lst = [1, 1, 1, 1, 12, 2, 2, 3, 4, 4]
print Counter(lst)

s = 'asssvavavaaaasssab'
print Counter(s)

s = "How many times does each word show up in this sentence how many times how many times"
words = s.split()
print Counter(words)

c = Counter(words)
print c.most_common(2)

print c.values()
# total of all counts
print sum(c.values())
# reset all counts
print c.clear()
# list unique elements
print list(c)
# convert to a set
print set(c)
# convert to a regular dictionary
print c.items()
# remove zero and negative counts
c += Counter()


print "----=========-==---------="
# default dict
d = {'k1': 1}
print d['k1']
# print d['k2']
d = defaultdict(object)
print d['one']
for item in d:
    print item

d = defaultdict(lambda: 0)
print d['one']

print d

# Order Dictionary

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d['f'] = 6

print d

for k, v in d.items():
    print k, v

# namedtuple
t = (1, 2, 3)
print t[0]


Dog = namedtuple('Dog', 'age breed name')

sam = Dog(age=2, breed="Lab", name="Sammy")
print sam.age, sam.breed, sam.name


Cat = namedtuple('Cat', 'fur claws name')
c = Cat(fur="fuzzy", claws=False, name="kitty")
print c.fur, c.claws, c.name
