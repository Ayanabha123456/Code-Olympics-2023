#this implementation assumes you have downloaded nltk and download the corpus in your local machines
from collections import Counter
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
data = []
file = open("pg100.txt",encoding="utf8")
for line in file:
    data.extend(line.split(' '))

tokens = nltk.word_tokenize(' '.join(data))

tokens = [token.lower() for token in tokens if token.isalpha() and token not in stop_words]

token_counts = dict(sorted(dict(Counter(tokens)).items(),key=lambda x:x[1],reverse=True))

count = 0

for key in token_counts.keys():
    print('Word: ',key,' Count: ',token_counts[key])
    count += 1
    if count == 100:
        break
