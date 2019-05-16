Tokenization 	토큰화
Cleaning	정제
Normalization	정규화

corpus -> token [토큰화] by NLTK, KoNLPy

1. 기초
. , ? ; ! => 구두점 : puncutation 정제 후 space 단위 토큰화

온점 . 문장의 경계를 알 수 있는 중요한 단서.
+ PH.D 나 AT&T, 01/02/06 $45.45 등 의미있는 구두점들이 많다.
=> 필요에 따라 구두점도 하나의 단어로 인식해야한다.

nltk.download('averaged_perceptron_tagger') # 품사 태깅
nltk.download('punkt') # 토큰화
