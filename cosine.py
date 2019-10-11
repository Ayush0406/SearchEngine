#!/usr/bin/env python
import math

class cosine_sim:

	def unit_vector(self,vector):
		unit_vector_query=0;
		for word in query_vector:
			unit_vector_query += query_vector[word]*query_vector[word];
		unit_vector_query = math.sqrt(unit_vector_query);
		return unit_vector_query

	def cosine_value(self,doc_vector,query_vector):
		value=0;i=0;
		unit_vector_query=unit_vector(query_vector);
		unit_vector_doc=unit_vector(doc_vector);
		for word in query_vector:
			value+=doc_vector[word]*query_vector[word];
		value = value/(unit_vector_query*unit_vector_doc);
		return value;