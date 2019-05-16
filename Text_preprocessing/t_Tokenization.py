import nltk  # nltk : 영어 코퍼스를 토큰화 하기위한 도구
from nltk.tokenize import word_tokenize, WordPunctTokenizer, TreebankWordTokenizer, sent_tokenize

var = "Don't be fooled by the dark sounding name-T, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."

var_w = word_tokenize(var)
print(var_w,'\n')

var_wp = WordPunctTokenizer().tokenize(var)
print(var_wp,'\n')

'''
	TreebankWordTokenizer : 하이픈 같은건 한단어로 취급, '는 접어가 함께 분리
'''

var_wt = TreebankWordTokenizer().tokenize(var)
print(var_wt,'\n')

'''
	문장 토큰화 Sentence Tokenization
	=> Binary Classifier : 두개의 클래스로 구분=> 약어사전 or 머신러닝
	1. 온점이 단어의 일부일 경우
	2. 온점이 문장의 구분자일경우
'''

text1 ="His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some reeds. He looked about, to mae sure no one was near."
text2 ="I am actively looking for Ph.D. students. and you are a Ph.D student."

print(sent_tokenize(text1),'\n')
print(sent_tokenize(text2),'\n')



