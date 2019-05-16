from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical

t = Tokenizer()

text = "나랑 점심 먹으러 갈래 점심 메뉴는 햄버거 갈래 갈래 햄버거 최고야"

t.fit_on_texts([text]) # t 변수에 text를fit on

vocab_size = len(t.word_index) # 단어 집합의 크기.

print(t.word_index)
print(t.word_counts)
print(t.texts_to_sequences([text]))
print(t.texts_to_sequences([text])[0])
x = t.texts_to_sequences([text])[0]

x = to_categorical(x,num_classes = vocab_size+1) 
# class 개수 1 추가 => t.fit_on_texts() 는 인덱스 1부터 부여 하기때문에

print(x)
