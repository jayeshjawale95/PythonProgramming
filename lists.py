# lists are mutable
my_list = [1,2,3]
print my_list
my_list = ['string',24,2.1,'o']
print my_list
print len(my_list)

my_list = ['one', "two", "three", 3, 5]
print my_list[0]
print my_list[1:]
print my_list[:2]

my_list = my_list + ['new item']
print my_list
#print my_list*2


l = [1,2,3]
print l
l.append('append me!')
print l

x = l.pop(0)
print x
print l
new_list = ['a','b','x','r','g','h']

print new_list
new_list.reverse()
print new_list
new_list.sort()
print new_list

l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]

matrix = [l_1, l_2, l_3]
print matrix
print matrix[2][0]

first_col = [row[0] for row in matrix]
print first_col
