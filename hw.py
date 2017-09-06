#Daniel RIch
#Homework 1
#This script parses out text files in a passed directory (pass as a string), and generates
#Two cumulative graphs. One without stopwords/punct, the other with.

import os
import sys
import nltk
import codecs
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt
import numpy as np

def main():
    if len(sys.argv) < 2:
        print("There is no directory argument passed in")
    print(sys.argv[1])
    fdist_cumulative = generate_freqdist()
    fdist_cumulative_no_punct_or_stopwords = generate_freqdist_without_stopwords_punctuation()
    create_freq_plot(fdist_cumulative,fdist_cumulative_no_punct_or_stopwords)



def generate_freqdist():
    fdist_cumulative = nltk.FreqDist()

    for root, dir, files in os.walk(sys.argv[1]): #Iterate through all files in given directory
        for file in files:
            if file.endswith(".txt"): #If it's a text file
                f = codecs.open(os.path.join(root,file), 'r', "utf-8")
                text = f.read() #Get the file text
                text = remove_newlines_make_lowercase(text)

                tokens = nltk.word_tokenize(text) #Tokenize the file text

                fdist = nltk.FreqDist(tokens) #Create frequency distribution from words
                #Print filename and 5 most common words
                print(f.name)
                print(fdist.most_common(5))
                fdist_cumulative+=fdist
                f = f.close()
    return fdist_cumulative


def generate_freqdist_without_stopwords_punctuation():
    fdist_cumulative = nltk.FreqDist()

    for root, dir, files in os.walk(sys.argv[1]): #Iterate through all files in given directory
        for file in files:
            if file.endswith(".txt"): #If it's a text file
                f = codecs.open(os.path.join(root, file), 'r', "utf-8")
                text = f.read() #Get the file text
                text = remove_newlines_make_lowercase_and_remove_punctuation(text)

                tokens = nltk.word_tokenize(text) #Tokenize the file text
                tokens = remove_stopwords(tokens)

                fdist = nltk.FreqDist(tokens) #Create frequency distribution from words
                #Print filename and 5 most common words
                print(f.name)
                print(fdist.most_common(5))
                fdist_cumulative+=fdist
                f = f.close()
    return fdist_cumulative


def remove_newlines_make_lowercase_and_remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation) #Translator to remove punctuation
    text = remove_newlines_make_lowercase(text)
    text = text.translate(translator)  # Remove punctuation
    return text


def remove_newlines_make_lowercase(text):
    text.replace('\n', ' ')  # Read the file and replace \n
    text = text.lower()  # Set to lowercase
    return text

def remove_stopwords(tokens):
    tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    return tokens

def create_freq_plot(data, data_no_stoporpunct):
    #data = data.most_common(50)
    #data_no_stoporpunct = data_no_stoporpunct.most_common(50)

    ax = data.plot(50, cumulative=True)
    ay = data_no_stoporpunct.plot(50, cumulative=True)


    plt.show()



if __name__ == '__main__':
  main()

