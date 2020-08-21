from functools import reduce

l1 = [1, 2, 3, 6, 8]
l2 = map(lambda x: x*x , l1)
l3 = filter(lambda x: x % 2 ==0 , l1)

print(list(l3))




sum = reduce( lambda x, y : x + y, l1, 0 )

print(sum)

words = ['Boss', 'a', 'Alfred', 'fig', 'Daemon', 'dig']
print("Sorting by default")
print(sorted(words))

print("Sorting with a lambda key")
print(sorted(words, key=lambda s: s.lower()))


print("Sorting with a method")
words.sort(key=str.lower, reverse=True)
print(words)

words.sort(key= str.lower, reverse=True)