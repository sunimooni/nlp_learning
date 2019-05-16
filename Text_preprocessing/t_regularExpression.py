'''
	정규 표현식 정리
	. 한 개의 임의의 문자
	? 앞의 문자 존재하거나 존재하지 않거나
	* 앞의 문자가 무한개존재 존재하지 않거나
	+ 앞의 문자가 최소 한개이상
	^ 뒤의 문자로 문자열이 시작
	$ 앞의 문자로 문자열이 끝남
	{숫자} 숫자만큼 반복
	{숫자1, 숫자2} 숫자 1이상, 숫자 2이하만큼 반복
	{숫자,} 숫자 이상만큼 반복
	[a-zA-Z] 대괄호 안의 문자들중 한개와 매칭
	[^]해당문자를 제외한 문자 매치
	A|B  A또는 B의 의미를 가진다
	\\ 역슬래쉬 문자 자체
	\d 모든 숫자 [0-9]
	\D 모든 숫자 제외한 [^0-9]
	\s 공백을 의미 [\t\n\r\f\v]
	\S 공백 제외
	\w 문자 또는 숫자를 의미
	\W 문자 또는 숫자 제외
'''
'''
	import re
	re.complie() 사용하는 패턴이 비슷할 경우 컴파일
	re.search() 문자열 전체에 대해서 정규표현식과 매치되는지 검색
	re.match() 문자열의 처음이 정규 표현식과 매치되는지 검색
	re.split() 정규 표현식을 기준으로 문자열을 분리하여 리스트로 리턴
	re.findall() 문자열에서 정규표현식 매칭되는거 모두 찾아 리턴 리스트형태
	re.finditer() 정규표현식과 매칭되는 모든 경우의 문자열 iter 객체
	re.sub() 문자열에서 정규 표현식과 일치하는 부분 다른 문자열로 대체
'''
'''
	정규표현식을 이용한 치환
	RegexpTokenizer 안에 정규 표현식 이용 토큰화
'''
import nltk
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer("[\w]+")
print(tokenizer.tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop"))

tokenizer = RegexpTokenizer("[\s]+",gaps=True)
print(tokenizer.tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop"))






