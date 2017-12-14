st = "print only the words that start with s in this sentence"

for word in st.split():
    if word[0] == 's':
        print word

lst = [number for number in range(0, 11, 2)]
print lst

lst = [number for number in range(1, 50) if number % 3 == 0]
print lst

st = "print every word in this sentence that has an even number of letter"
for word in st.split():
    if len(word) % 2 == 0:
        print word + "  <<--- has even length"

st = 'create a list of the first letters of every word in this string'
lst = [word[0] for word in st.split()]
print lst
