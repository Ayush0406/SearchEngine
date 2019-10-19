from Co_Occurrence import CoOccur
# from cosine import cosine_sim
from tf_idf import tf_idf
import pandas as pd
from Co_Occurrence import docFreq
import pickle
import math
import json
import os
from pathlib import Path

query = input()
all_words = {}

workingDirectory = os.getcwd()      # gets the current working directory
directory = os.path.join(workingDirectory, "dataset\\test")     # concatenates
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
			data.append(newsArticle)

df = pd.DataFrame(data, columns=['headline', 'brief', 'article'])

tokenize_obj = CoOccur(df)
all_words = tokenize_obj.find() 	# list of all words in corpus
print(all_words)

"""df1 = pd.DataFrame(all_words)
df1.to_csv('all_words.csv')"""

query_tf = tf_idf()
query_refined = tokenize_obj.tokenize(query)
query_final = query_tf.tf_idf_query(query_refined, all_words,docFreq,4514)
print(query_final)


"""tf_idf_vector_list = []  # list of dictonares of every doc
for row in df.index:                        # iterate through row
	article = df['text'][row]
	tokenized = tokenize_obj.tokenize(article)
	doc_tf = tf_idf()
	lis = doc_tf.tf_doc_specific(tokenized, all_words)  # dictionary storing tf score of doc
	tf_idf_vector_list.append(lis)
	# for words in lis:


df = pd.DataFrame(tf_idf_vector_list)
df.to_csv('file1_1.csv')
with open('dict.json', 'w') as fout:
	json.dump(tf_idf_vector_list, fout)

"""
"""""
cosine_obj = cosine_sim()
df = pd.read_csv('file1_1.csv')
# df1 = pd.read_pickle('all_words.pickle')
count = 0
cosine_sums = {}
itea= 1
print(len(df.columns))
for rows in df.itertuples():
	temp_dict = {}
	for i in range(0, len(rows)-1):
		# print(i)
		word = (df.columns[i])
		if math.isnan(rows[i]) is False:  # var stores tf idf score
			temp_dict[word] = float(rows[i])
	# print(temp_dict)
	su = cosine_obj.cosine_value(temp_dict, query_final)
	cosine_sums[itea+1] = su
	itea=itea+1

print(cosine_sums) """

"""for index in range(len(tf_idf_vector_list)):
	val=0
	for i in range(len(query)):
		if query[i] in tf_idf_vector_list[index]:
			val+="""
#print(docFreq['said'])