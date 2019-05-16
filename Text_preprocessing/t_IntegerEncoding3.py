'''
	by enumerate
'''

test=[8, 2, 5, 1, 3, 7, 9, 4, 6, 10]
for index, value in enumerate(test):
	print("index : {}, value:{}".format(index,value))

# 문장 토큰화 되어있는 형태
text=[['barber', 'person'], ['barber', 'good', 'person'], ['barber', 'huge', 'person'], ['knew', 'secret'], ['secret', 'kept', 'huge', 'secret'], ['huge', 'secret'], ['barber', 'kept', 'word'], ['barber', 'kept', 'word'], ['barber', 'kept', 'secret'], ['keeping', 'keeping', 'huge', 'secret', 'driving', 'barber', 'crazy'], ['barber', 'went', 'huge', 'mountain']]

vocab = sum(text,[])
print(set(vocab))

vocab_sorted = sorted(set(vocab))
print(vocab_sorted)


word_to_index = {word : index + 1 for index, word in enumerate(vocab_sorted)}

print(word_to_index)
