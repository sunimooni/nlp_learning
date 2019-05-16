'''
	one-hot encoding
	=> 단어 집합의 크기를 벡터 차원으로 표현
'''

from konlpy.tag import Okt

okt = Okt()
token = okt.morphs("나는 자연어 처리를 배운다") # 형태소 토큰화

word2index = {}

for voca in token:
	if voca not in word2index.keys():
		word2index[voca] = len(word2index)


def one_hot_encoding(word, word2index):
	one_hot_vector = [0]*(len(word2index))
	index = word2index[word]
	one_hot_vector[index] = 1
	return one_hot_vector

var = one_hot_encoding("자연어",word2index)
print(var)
