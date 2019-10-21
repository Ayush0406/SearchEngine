#!/usr/bin/env python
import math


class cosine_sim:
	"""
		This class contains methods to compute dot product
		of 2 vectors and normalise the vectors.
	"""

	def unit_vector(self,vector):
		"""
		This method computes the magnitude of the tf-idf vector passed as input
		:param vector:dictionary of words with corresponding tf-idf scores
		:return:float value which is the magnitude of the input vector
		"""
		unit_vector_query=0;
		for word in vector:
			unit_vector_query += vector[word]*vector[word];
		unit_vector_query = math.sqrt(unit_vector_query);
		return unit_vector_query

	def cosine_value(self,doc_vector,query_vector):
		"""
		This method finds the cosine similarity between 2 tf-idf value vectors
		:param doc_vector: dictionary of document tf-idf scores
		:param query_vector: dictionary of query tf-idf scores
		:return: float value which is the cosine similarity score
		"""
		value=0;i=0;
		unit_vector_query=self.unit_vector(query_vector);
		unit_vector_doc=self.unit_vector(doc_vector);
		iterate=0
		for word in query_vector:
			if word in doc_vector:
				value+=query_vector[word]*doc_vector[word]
		if unit_vector_query != 0:
			value = value/(unit_vector_query*unit_vector_doc)
		else:
			value = 0
		return value

#cos = cosine_sim()
#res = [1,1,4]
#hello=[4,5,6]
#s = cos.cosine_value(hello,res)
#print(s)