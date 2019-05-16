'''
	한국어 토큰화 문제점
	=> 1. 조사문제
	=> 2. 한국어는 띄어쓰기가 영어보다 잘 지켜지지 않는다.

	품사 부착 (part-of-speech tagging)
	=> 단어는 품사에 따라 의미가 달라지기도 한다.
	=> ex) 못=> 못하다, 못
	
	PRP 인칭 대명사
	VBP 동사
	RB 부사
	VBG 현재 부사
	IN 전치사
	NNP 고유 명사
	NNS 복수형 명사
	CC 접속사
	DT 관사
'''
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

text = "I am actively looking for Ph.D. students. and you are a Ph.D. student."
token = word_tokenize(text)
tag = pos_tag(token)

print(token,'\n')
print(tag,'\n')

'''
	형태소 분석기KoNLPy 파이썬 패키지
	Okt(Open Korea Text), 메캅(Mecab), 코모란(Komoran), 한나눔(Hannanum), 꼬꼬마(Kkma)
	=> 형태소(morpheme) 단위 토큰화
	
	Okt
		- morphs : 형태소 추출
		- pos : 품사 부착
		- nouns : 명사 추출
'''

from konlpy.tag import Okt
okt = Okt()
var = "열심히 코딩한 당신, 연휴에는 여행을 가봐요"

print("okt")
print(okt.morphs(var),'\n')
print(okt.pos(var),'\n')
print(okt.nouns(var),'\n')


from konlpy.tag import Kkma

kkma = Kkma()
print("kkma")
print(kkma.morphs(var),'\n')
print(kkma.pos(var),'\n')
print(kkma.nouns(var),'\n')











