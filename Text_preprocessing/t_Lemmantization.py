'''
	Lemmantization : 표제어 추출=> 코퍼스에 있는 단어의 개수를 줄이는 기법
	Stemming : 어간 추출
	=> 눈으로 봤을 대 서로 다른 단어들을, 하나의 단어로 일반화시키는 작업.
	=> 문서 내의 단어 수를 줄이는 작업, 코퍼스로부터 복잡성을 줄이는 작업.
'''
'''
	Lamma => '표제어', '기본 사전형 단어' 단어들로 부터 표제어 찾는 과정
	뿌리 단어 찾기 과정!! ex) am,are,is => be
	1. 형태학적 파싱 == 형태소부터 단어들을 만들어간다.
	2. 형태소
		-stem(어간, 단어의 의미를 담고 있는 핵심부분) 	
		-affix(접사, 단어에 추가적인 의미주는 부분)

	표제어 추출은 품사정보를 보존한다.
	어간 추출은 품사 정보를 보존하지 않는다.

'''
import nltk
from nltk.stem import WordNetLemmatizer

n = WordNetLemmatizer()

words = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']

print(words)

print([n.lemmatize(w) for w in words])

print('dies',n.lemmatize('dies','v'))
print('watched',n.lemmatize('watched','v'))
print('has',n.lemmatize('has','v'))



