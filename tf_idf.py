#!/usr/bin/env python for index in range(len(list)):
import math
from cosine import cosine_sim
from Co_Occurrence import docFreq


class tf_idf:
	"""
	This class contains methods which generate the tf-idf scores
	for query string and the documents of the dataset.
	"""

	def tf_doc_specific(self, myList, global_word):
		"""
		This method is used to find the tf-idf score of the specific document which has been passed as an argument
		:param myList: The list of words obtained from an individual document
		:param global_word: The list of all the words in the entire corpus
		:return: a dictionary which maps the tf-idf scores of the words in the specific document
		"""
		word_count = {}
		for index in range(len(myList)):
			if myList[index] in word_count.keys():
				word_count[myList[index]] = word_count[myList[index]]+1
			else:
				word_count[myList[index]] = 1
		for word in word_count:
			count = word_count[word]
			word_count[word] = (1+math.log(count, 10))
		return_vector = []
		"""for index in range(len(global_word)):
			if global_word[index] in word_count:
				return_vector.append(word_count[global_word[index]]);
			else:
				return_vector.append(0);
		iterate = 0"""
		"""for index in range(len(global_word)):
			if global_word[index] in myList: 
				print(global_word[index] + ' ' + str(return_vector[index]))"""
		return word_count

	def tf_idf_query(self,Query,global_word,doc_freq,doc_count):
		"""
		This method is responsible for computing the tf-idf score of the user query
 		:param Query: list of strings present in the user query
		:param global_word: list of all the words present in the corpus
		:param doc_freq: dictionary which maps each word of the corpus to the number of documents it appears in
		:param doc_count: integer denoting total number of documents in the corpus
		:return: dictionary of user query words mapped on to the corresponding tf-idf scores
		"""
		word_tf = {}
		for index in range(len(Query)):
			if Query[index] in word_tf.keys():
				word_tf[Query[index]] = word_tf[Query[index]]+1
			else:
				word_tf[Query[index]] = 1
		for word in word_tf:
			count = word_tf[word] 	# term frequency of the word in query
			word_tf[word] = float(1+math.log(count, 10))
		return_vector = []
		"""for word in global_word:
			if word in word_count:
				return_vector.append(word_tf[word])
			else:
				return_vector.append(0);"""
		for word in word_tf:
			if word in global_word:
				word_tf[word] *= math.log(doc_count/docFreq[word], 10)
			else:
				word_tf[word] = 0
		return word_tf
