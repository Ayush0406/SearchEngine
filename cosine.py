#!/usr/bin/env python
import math

class cosine_sim:

	def unit_vector(self,vector):
		unit_vector_query=0;
		for word in vector:
			unit_vector_query += vector[word]*vector[word];
		unit_vector_query = math.sqrt(unit_vector_query);
		return unit_vector_query

	def cosine_value(self,doc_vector,query_vector):
		value=0;i=0;
		unit_vector_query=self.unit_vector(query_vector);
		unit_vector_doc=self.unit_vector(doc_vector);
		iterate=0
		for word in query_vector:
			if word in doc_vector:
				value+=query_vector[word]*doc_vector[word]
		value = value/(unit_vector_query*unit_vector_doc);
		return value

#cos = cosine_sim()
#res = [1,1,4]
#hello=[4,5,6]
#s = cos.cosine_value(hello,res)
#print(s)