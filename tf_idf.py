#!/usr/bin/env python for index in range(len(list)):
import math
from cosine import cosine_sim
from Co_Occurrence import docFreq

class tf_idf:
	def tf_doc_specific(self, myList, global_word):
		word_count = {}
		for index in range(len(myList)):
			if myList[index] in word_count:
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
		word_tf = {}
		for index in range(len(Query)):
			if Query[index] in word_tf:
				word_tf[Query[index]] = word_tf[Query[index]]+1
			else:
				word_tf[Query[index]] = 1
		for word in word_tf:
			count = word_tf[word] # term frequency of the word in query
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





globa = ['Wishing','former', 'cricketer', 'Zaheer', 'Khan', 'on', 'the', 'occasion', 'of', 'his', '41st', 'birthday', 'Team', 'India', 'all-rounder' ,'Hardik', 'Pandya', 'shared', 'a', 'video', 'him','trolls','the fuck']
test = ['former','Wishing', 'cricketer', 'Zaheer', 'Khan', 'on', 'the', 'occasion', 'of', 'his', '41st', 'birthday', 'Team', 'India', 'all-rounder' ,'Hardik', 'Pandya', 'shared', 'a', 'video', 'of', 'him','Pandya','Pandya','trolls','Zaheer','Khan']
#query = ['cricketer','Zaheer']
#gl = ['cricketer']
tr = tf_idf()
tr.tf_doc_specific(test, globa)

#res = [1,1,4]
#hello=[4,5,6]
#cos = cosine_sim()
#s = cos.cosine_value(hello,res)
#print(s)
