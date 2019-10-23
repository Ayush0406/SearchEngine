# News Article Search Engine 


#### A text based search engine
This search engine works on a BBC news article dataset of approximately 2200 documents.It preprocesses documents and indexes it for future use.Vector Space Model is used to retrieve top 10 articles based on the input query.We have used tf-idf ranking method to compute the vector for every document and query. 


## Prerequisites
We have chosen a dataset of  BBC news articles ,divided into 5 categories : 
1. Tech
2. Business
3. Entertainment
4. Politics
5. Sports

You are free to chose to select your own dataset, but correspondingly the modification has to be done in *reader.py* file.
If you wish to use the code without changing the dataset make sure the .txt file is in this format
```
<Headline>
 ----- 				(An empty line)
<Brief>
----- 				(An empty line)
<Article> 			(Actual news article)

```

## Getting Started
First step involves cloning this repository into your destination folder.
```sh
$ cd 'destPath' 
$ git clone https://github.com/smit-1999/SearchEngine
```

This code is tried and tested to run in versions of Python 3 and above.
For python packages below the specified version,please upgrade using
```sh
$ sudo apt-get install python3.5
```

After installation of the proper python version:
* Run the main.py file
* Enter your input query of words
* Voila! You have your results.


## Authors
* [Smit Shah](https://github.com/smit-1999)
* [Saarthak Jain](https://github.com/saarthakjain001)
* [Dhruv Gupta](https://github.com/coderdhruv)
* [Ayush Laddha](https://github.com/Ayush0406)
