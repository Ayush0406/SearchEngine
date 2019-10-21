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
    """
    This class contains methods for updating the document frequency and
    tokenizing the article.
    """
    df = pd.DataFrame()

    def __init__(self, dataframe):
        """
        This is the constructor for this class which initialises the instance
        variable.
        :param dataframe: This is a pandas dataframe storing every news article.
        """
        self.df = dataframe

    def tokenize(self, article):
        """
        This method tokenises a string into important words.It first case folds
        the string, creates tokens, removes stop words and then stems word using
        Porter Stemmer.
        :param article: It is a news article in form of  string.
        :return: It returns a list of tokenized words.
        """
        article = article.lower()
        tokens = word_tokenize(article)

        result = [word for word in tokens if word not in stop_words]    # remove stopwords

        for i in range(0, len(result)):
            word = result[i]
            result[i] = ps.stem(word)   # Porter Stemmer

        # print(result)
        return result


    def find(self):
        """
        This method updates the document frequency by iterating through each
        document in the dataframe.
        :return: It returns a list which contains all unique words across all
                 documents(document corpus).
        """
        global_set = set()
        global_list = list()
        testTokenized = 0
        for row in self.df.index:
            article = self.df['article'][row]
            tokenized = self.tokenize(article)  # list of tokenize article

            uniqueWords = set(tokenized)
            testTokenized += len(uniqueWords)
            for word in uniqueWords:
                if word in docFreq.keys():
                    docFreq[word] += 1
                else:
                    docFreq[word] = 1

            for word in uniqueWords:
                if word not in global_set:
                    global_set.add(word)

            # global_list = list(docFreq.keys())
        for word in global_set:
            global_list.append(word)
        print("docfrq size:", len(docFreq))
        print("global list", len(global_list))
        print("uniquewords :", testTokenized)
        return global_list

    def spell_check(self, query):
        """
        This method checks for spelling errors in the query, and updates any
        misspelt word.It uses the python library 'pyspellchecker'
        :param query: query is a list of words which may contain misspelt words.
        :return: It returns a list which contains correct words in query
                 as well as the incorrect words which have now been modified.
        """
        spell = SpellChecker()
        misspelled = spell.unknown(query)                       # list of misspelled words in query
        #print(misspelled)
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
        #print(query)        # query with correct spellings
        return query


# find root words = done
# find doc freq of each root word = done
