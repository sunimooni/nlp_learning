'''
	[불용어 : stopword]
	=> 의미가 없는 단어.
'''
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example ="Family is not an important thing. It's everything."
stop_words = list(stopwords.words('english'))

word_tokens = word_tokenize(example)
result = []

for w in word_tokens:
	if w not in stop_words:
		result.append(w)

print(word_tokens)
print(result)
