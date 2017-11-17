
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\D+')

with open('data/tweepy_sports_train.txt') as f:
    for word in f:
        if word.strip()!='' and len(word.split())>=3:
            word_list=tokenizer.tokenize(word.lower().replace('"text":','').replace('\\u','').replace('https','').replace('\\','').replace('//','')\
                                         .replace('/','').replace('\\','').replace('"','').split(',')[3])
           
            for word_ in word_list:
                if word_ not in stopwords.words('english') and not(word_.startswith('u30')) and len(word_.strip())>2:
                    print(word_.split())