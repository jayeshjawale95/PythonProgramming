def word_length(phrase):
    return list(map(len, phrase.split()))


print word_length('How long are the words in this phrase')


def digits_to_num(digits):
    return reduce(lambda x, y: x * 10 + y, digits)


print digits_to_num([3, 4, 3, 2, 1])


def filter_words(word_list, letter):
    return filter(lambda word: word[0] == letter, word_list)


lst = ['hello', 'are', 'cat', 'dog', 'ham', 'hi', 'go', 'to', 'heart']
print filter_words(lst, 'h')


def concatenate(L1, L2, connector):
    return [word1 + connector + word2 for word1, word2 in zip(L1, L2)]


print concatenate(['A', 'B'], ['a', 'b'], '-')


def d_list(L):
    return {key: value for value, key in enumerate(L)}


print d_list(['a', 'b', 'c'])


def count_match_index(L):
    return len([num for i, num in enumerate(L) if num == i])


print count_match_index([0, 2, 2, 1, 5, 5, 6, 10])
