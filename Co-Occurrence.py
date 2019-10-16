import pandas as pd
import nltk, string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker

ps = PorterStemmer()
stop_words = set(stopwords.words("english"))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
docFreq = {}    # A dictionary to store doc frequency of each unique word

class CoOccur:

    def tokenize(self, article):
        article = article.lower()
        tokens = word_tokenize(article)
        """pattern = r'''(?x)
                  ([A-Z]\.)+
                 |\d+:\d+
                 |(https?://)?(\w+\.)(\w{2,})+([\w/]+)?
                 |[@\#]?\w+(?:[-']\w+)*
                 |\$\d+(\.\d+)?%?
                 |\\[Uu]\w+
                 |\.\.\.
                 |[!?]+
             '''

        nltk.regexp_tokenize(article, pattern)
        result = article.translate(str.maketrans('', '', string.punctuation))
        print(result)"""
        result = [word for word in tokens if word not in stop_words]
        for i in range(0, len(result)):
            word = result[i]
            result[i] = ps.stem(word)   # Porter Stemmer
            if word in docFreq:
                docFreq[word] += 1
            else:
                docFreq[word] = 1
        return result

    def construct_matrix(self, tokenized):
        print()
        # matrix to be constructed with adjacent words

    def find(self):
        for row in df.index:                        # iterate through row
            article = df['text'][row]
            tokenized = self.tokenize(article)      # tokenize article
            self.construct_matrix(tokenized)

    def spell_check(self, query):
        spell = SpellChecker()
        misspelled = spell.unknown(query)                       # list of misspelled words in query
        for i in range(0, len(query)):
            if query[i] in misspelled:
                candidate_found = False
                for candidate in spell.candidates(query[i]):    # possible candidates
                    if candidate in docFreq:
                        query[i] = candidate
                        candidate_found = True
                        break
                if candidate_found is False:
                    query[i] = spell.correction(query[i])   # Get the one `most likely` answer
        print(query)        # query with correct spellings


df = pd.read_csv('news_summary.csv', sep=',', encoding='latin-1')
features = (col for col in df.columns)
c = CoOccur()
# c.find(['1', '2'])
query = ['aple', 'astnaut', 'bnna']
c.spell_check(query)

# find root words = done
# find doc freq of each root word = done

