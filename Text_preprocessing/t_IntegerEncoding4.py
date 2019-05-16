'''
	nltk => freqdist
	=> 토큰들의 빈도를 손쉽게 셀 수 있도록 빈도수 계산 클래스
'''
from nltk import FreqDist

test_list = ['barber', 'barber', 'person', 'barber', 'good', 'person']
fdist = FreqDist(test_list)

fdist.N() # 전체 단어 개수 출력
fdist.freq("barbar") # barbar 라는 단어의 확률
fdist["barbar"] # 단어의 빈도
fdist.most_common(2) # 등장 빈도수 높은 상위 2개의 단어만 출력
