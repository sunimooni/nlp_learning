'''
	Lemmantization : 표제어 추출=> 코퍼스에 있는 단어의 개수를 줄이는 기법
	Stemming : 어간 추출
	=> 눈으로 봤을 대 서로 다른 단어들을, 하나의 단어로 일반화시키는 작업.
	=> 문서 내의 단어 수를 줄이는 작업, 코퍼스로부터 복잡성을 줄이는 작업.
'''
'''
	어간 추출 : 정해진 규칙만 보고 단어의 어미를 자르는 어림짐작의 작업이다.
		=> 어간 추출 알고리즘 중 하나인 포터 알고리즘에
'''
import nltk
from nltk.stem import PorterStemmer, LancasterStemmer
from nltk.tokenize import word_tokenize

s = PorterStemmer() # 어간 추출 알고리즘 중 하나인 포터 알고리즘
l = LancasterStemmer() # 랭커스터 스태머 알고리즘

text="This was not the map we found in Billy Bones's chest, but an accurate copy, complete in all things--names and heights and soundings--with the single exception of the red crosses and the written notes."

var = ['formalize','allowance','electricial']

words = word_tokenize(text)
print(words)
print([s.stem(w) for w in words])

print (var)
print([s.stem(w) for w in var])

comp = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']

print(comp)
print([s.stem(w) for w in comp])
print([l.stem(w) for w in comp])

