'''
	by keras
	=> fit_on_texts() 리스트 기반 단어 빈도수 사전 만든다. 빈도수 순으로 인덱싱
'''
from keras.preprocessing.text import Tokenizer

text = ["A barber is a person. a barber is good person. a barber is huge person. he Knew A Secret! The Secret He Kept is huge secret. Huge secret. His barber kept his word. a barber kept his word. His barber kept his secret. But keeping and keeping such a huge secret to himself was driving the barber crazy. the barber went up a huge mountain."]

t = Tokenizer()
t.fit_on_texts(text)
print(t.word_index) # 부여된 인덱스 확인 방법
print(t.word_counts) # 단어당 부여된 개수
print(t.texts_to_sequences(text)) # => 각 단어를 word_index한 정해진 인덱스로 치환


'''
	모든 단어가 인식된다는 문제
'''
word_frequency = [w for w, c in t.word_counts.items() if c < 2]
for w in word_frequency:
	del t.word_index[w]
	del t.word_counts[w]

print(t.word_index)
