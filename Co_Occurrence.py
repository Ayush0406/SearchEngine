import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker
# from main import df


ps = PorterStemmer()
stop_words = set(stopwords.words("english"))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
docFreq = {}    # A dictionary to store doc frequency of each unique word

class CoOccur:
    df = pd.DataFrame()

    def __init__(self, dataframe):
        self.df = dataframe

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
        result = [word for word in tokens if word not in stop_words] # remove stopwords
        for i in range(0, len(result)):
            word = result[i]
            result[i] = ps.stem(word)   # Porter Stemmer
            if word in docFreq:
                docFreq[word] += 1
            else:
                docFreq[word] = 1
        # print(result)
        return result

    def construct_matrix(self, tokenized, tfidf_result):
        print()
        for docindex in tfidf_result:
            doc = self.df['text'][docindex]

    def find(self):
        global_dict = set()
        count = 0
        for row in self.df.index:
            article = self.df['article'][row]
            tokenized = self.tokenize(article)  # tokenize article

            """for word in tokenized:
                if word not in global_dict:
                    global_dict.add(word)
                    count = count + 1"""
            global_list = list(docFreq.keys())
            """for word in global_dict:
                global_list.append(word)"""

        return global_list

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



# find root words = done
# find doc freq of each root word = done
