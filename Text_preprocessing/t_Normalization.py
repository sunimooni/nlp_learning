'''
	정규화: 표현 방법이 다른 단어들 통합 같은 단어로 만들어준다.
	정제  : 코퍼스로부터 노이즈 데이터 제거
	불필요한 단어의 제거
	=> 등장 빈도가 적은 단어(Removing Rare Words)
	=> 길이가 짧은 단어
		-영어 단어의 평균 길이는 6~7, 한국어 단어의 평균 길이는 2~3.
'''
import re

text = "I was wondering if anyone out there could enlighten me on this car."
shortword = re.compile(r'\W*\b\w{1,2}\b')
print(shortword.sub('',text))

