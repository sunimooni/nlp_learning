'''
	Integer Encoding
	=> 단어: 정수 mapping
'''
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter # 빈도수 계산

vocab = Counter()
stop_words = set(stopwords.words('english'))

text="A barber is a person. a barber is good person. a barber is huge person. he Knew A Secret! The Secret He Kept is huge secret. Huge secret. His barber kept his word. a barber kept his word. His barber kept his secret. But keeping and keeping such a huge secret to himself was driving the barber crazy. the barber went up a huge mountain."

text = sent_tokenize(text)

sentences =[]

for i in text:
	sentence = word_tokenize(i)
	result = []

	for word in sentence:
		word = word.lower() # 소문자
		if word not in stop_words:
			if len(word) > 2:
				result.append(word)
				vocab[word] = vocab[word] + 1 # 해당 단어의 빈도 추가
	sentences.append(result)

print(sentences,'\n')
print(vocab,'\n')
vocab_sorted = sorted(vocab.items(), key=lambda x:x[1], reverse=True)
print(vocab_sorted)

word_to_index = {}
i = 0
for (word,frequency) in vocab_sorted :
	if frequency > 1 :
		i = i + 1
		word_to_index[word] = i

print(word_to_index)















