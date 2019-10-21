from Co_Occurrence import CoOccur
from cosine import cosine_sim
from tf_idf import tf_idf
from Co_Occurrence import docFreq
import json
import timeit
from file_read_write import file_read_write


query = input()
start = timeit.default_timer()
coOccur_obj = CoOccur(None)  # a coOccur temporary object to tokenize the query
query_tf = tf_idf()
query_list = list(query.split(" "))
query_list = coOccur_obj.spell_check(query_list)
empty_str = " "
query = empty_str.join(query_list)
query_refined = coOccur_obj.tokenize(query)  # tokenize query,stem and remove stop words
print(query_refined)
query_refined.sort()


file_reader_object = file_read_write()

# search query in cache
file_reader_object.cache_reader(query_refined, start)

# read dataset of .txt files into dataframe
df = file_reader_object.dataset_reader()

# df = pd.DataFrame(data, columns=['headline', 'brief', 'article', 'type', 'filename'])
tokenize_obj = CoOccur(df)

all_words = tokenize_obj.find() 	# list of all words in corpus
print("All words size:", len(all_words))


# query_refined = tokenize_obj.spell_check(query)
# print(query)

# compute the query vector
query_final = query_tf.tf_idf_query(query_refined, all_words, docFreq, len(df))
print(query_final)

# compute the document vector for each document in dataframe
tf_idf_vector_list = []  						# list of dictionaries of every doc
for row in df.index:                        	# iterate through row
	article = df['article'][row]
	tokenized = tokenize_obj.tokenize(article)
	doc_tf = tf_idf()
	lis = doc_tf.tf_doc_specific(tokenized, all_words)  # dictionary storing tf score of doc
	tf_idf_vector_list.append(lis)

# df = pd.read_csv('file1_1.csv')
# df1 = pd.read_pickle('all_words.pickle')
# compute dot product between two query vector and each document vector
cosine_obj = cosine_sim()
count = 0
cosine_sums = {}
itea = 0


for dictionary in tf_idf_vector_list:
	# print(i)
	sum = cosine_obj.cosine_value(dictionary, query_final) # result of dot product of doc and query
	cosine_sums[(df['type'][itea], df['headline'][itea], df['filename'][itea])] = sum
	itea=itea+1
cosine_sums = sorted(cosine_sums.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)[:10]
print(cosine_sums)

# write result in cache for further use
with open('cache.txt', 'a+') as file:
	file.write(str(query_refined))
	file.write('\n')
	file.write(json.dumps(cosine_sums))
	file.write('\n')
file.close()
stop = timeit.default_timer()

print('Time: ', stop - start)

"""
testing queries:
1)firm
2)pl : only one word across corpus
3)lpk : not present across corpus
"""
