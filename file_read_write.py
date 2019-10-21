import timeit
import sys
import json
import os
from pathlib import Path
import pandas as pd

class file_read_write:
    """
    This class contains the methods for performing reading and writing
    operations on text files
    """
    def cache_reader(self,query_refined,start):
        """
        This method checks if the user query has already been answered
        in the past.If the results already exist in cache.txt,then
        results are directly given and unnecessary computations saved.
        :param query_refined: list of tokenized user input strings
        :param start: float value which references the starting time of running the main file
        :return:None
        """
        cache_file_reader = open('cache.txt')
        line_iterator = 1
        while True:
            line = cache_file_reader.readline()  # read line
            if line_iterator % 2 != 0 and line.strip() == str(query_refined):
                print(cache_file_reader.readline())
                stop = timeit.default_timer()
                print('Time: ', stop - start)
                cache_file_reader.close()
                sys.exit()
            line = cache_file_reader.readline()  # move to next line
            if not line:  # check if line is not empty
                break
        cache_file_reader.close()

    def dataset_reader(self):
        """
        This method reads all the text files present in the dataset and
        adds them to a dataframe which contains columns namely
        ['headline', 'brief', 'article', 'type', 'filename']
        :return: returns a dataframe of the read documents
        """
        workingDirectory = os.getcwd()  # gets the current working directory
        directory = os.path.join(workingDirectory, "dataset\\bbc")  # concatenates
        print(directory)
        data = []  # list to store each news article
        folders = os.listdir(directory)  # list of all files in the directory
        for folder in os.listdir(directory):
            if os.path.isdir(os.path.join(directory, folder)) is True:
                for file in os.listdir(os.path.join(directory, folder)):
                    filePath = os.path.join(directory, folder, file)
                    txt = Path(filePath).read_text()
                    headline, brief, article = txt.split('\n\n', 2)
                    newsArticle = list()  # current news article
                    newsArticle.append(headline)
                    newsArticle.append(brief)
                    newsArticle.append(article)
                    newsArticle.append(folder)
                    newsArticle.append(file)
                    data.append(newsArticle)

        df = pd.DataFrame(data, columns=['headline', 'brief', 'article', 'type', 'filename'])
        return df
