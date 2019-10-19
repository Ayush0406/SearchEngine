from Co_Occurrence import CoOccur
from cosine import cosine_sim
from tf_idf import tf_idf
import pandas as pd
from Co_Occurrence import docFreq
import pickle
import math
import json
import os
from pathlib import Path
import timeit


start = timeit.default_timer()
query = input()
all_words = {}

workingDirectory = os.getcwd()      # gets the current working directory
directory = os.path.join(workingDirectory, "dataset\\bbc")     # concatenates
print(directory)
data = [] 	# list to store each news article
folders = os.listdir(directory)    # list of all files in the directory
for folder in os.listdir(directory):
	if os.path.isdir(os.path.join(directory, folder))is True:
		for file in os.listdir(os.path.join(directory, folder)):
			filePath = os.path.join(directory, folder, file)
			txt = Path(filePath).read_text()
			headline, brief, article = txt.split('\n\n', 2)
			newsArticle = list() 	# current news article
			newsArticle.append(headline)
			newsArticle.append(brief)
			newsArticle.append(article)
			newsArticle.append(folder)
			newsArticle.append(file)
			data.append(newsArticle)

df = pd.DataFrame(data, columns=['headline', 'brief', 'article', 'type', 'filename'])
tokenize_obj = CoOccur(df)
all_words = tokenize_obj.find() 	# list of all words in corpus
print(len(all_words))

"""df1 = pd.DataFrame(all_words)
df1.to_csv('all_words.csv')"""

query_tf = tf_idf()
# query_refined = tokenize_obj.spell_check(query)
# print(query)
query_refined = tokenize_obj.tokenize(query)  # tokenize query,stem and remove stop words
query_final = query_tf.tf_idf_query(query_refined, all_words, docFreq, len(df))
print(query_final)


tf_idf_vector_list = []  # list of dictionaries of every doc
for row in df.index:                        # iterate through row
	article = df['article'][row]
	tokenized = tokenize_obj.tokenize(article)
	doc_tf = tf_idf()
	lis = doc_tf.tf_doc_specific(tokenized, all_words)  # dictionary storing tf score of doc
	tf_idf_vector_list.append(lis)
#print(docFreq['xyz'])
"""""
df = pd.DataFrame(tf_idf_vector_list)
df.to_csv('file1_1.csv')"""
#with open('dict.json', 'w') as fout:
#	json.dump(tf_idf_vector_list, fout)



cosine_obj = cosine_sim()
#df = pd.read_csv('file1_1.csv')
# df1 = pd.read_pickle('all_words.pickle')
count = 0
cosine_sums = {}
itea= 0
#print(len(df.columns))
for dictionary in tf_idf_vector_list:
	# print(i)
	sum = cosine_obj.cosine_value(dictionary, query_final) # result of dot product of doc and query
	cosine_sums[(df['type'][itea], df['headline'][itea], df['filename'][itea])] = sum
	itea=itea+1
cosine_sums=sorted(cosine_sums.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)[:10]
print(cosine_sums)

"""for index in range(len(tf_idf_vector_list)):
	val=0
	for i in range(len(query)):
		if query[i] in tf_idf_vector_list[index]:
			val+="""
#print(docFreq['said'])

stop = timeit.default_timer()

print('Time: ', stop - start)

"""
testing queries:
1)firm
2)
"""