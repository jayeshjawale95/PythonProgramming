l = [1,2,3]
print l[0]
my_dict = {'key1':'value','key2':'value2'}
print my_dict
print my_dict['key1']

my_dict = {'k1':123,'k2':3.4,'k3':'string'}

print my_dict
print my_dict['k3'].upper()

d = {}
d['animal'] = 'Dog'
d['answer'] = 42
print d
d = {'k1': {'nestkey': {'subnestkey': 'value'} } }
print d
print d['k1']['nestkey']['subnestkey'].upper()

d = {}
d['k1'] = 1
d['k2'] = 2
d['k3'] = 3
print d
print d.keys()
print d.values()
print d.items()
