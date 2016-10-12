from __future__ import division  # Python 2 users only
import nltk, re, pprint
import sys
from nltk import word_tokenize
from nltk.stem.porter import *
import pandas as pd
import numpy as np

# Put all that in a function!
def get_cliche_rating(lyrics, df):
    # Lyrics is a string
    
    # Tokenize, stem, count
    tokens = word_tokenize(lyrics)
    stemmer = PorterStemmer()
    stems = [stemmer.stem(token.lower()) for token in tokens if token.isalnum()]
    fd = nltk.FreqDist(stems)
    
    # Cast into format we can work with
    [keys, counts] = zip(*fd.items()) # clever unzipping from http://stackoverflow.com/questions/12974474/how-to-unzip-a-list-of-tuples-into-individual-lists
    keys = np.asarray(keys)
    counts = np.asarray(counts)
    
    # calculate weighted average of cliche ratings
    avg_cliche = 0
    for stem in stems:
        sub_df = df.cliche[df.stem==stem]
        if sub_df.empty:
            continue
        avg_cliche = avg_cliche + df.cliche[df.stem==stem].iloc[0]
    avg_cliche = avg_cliche / len(stems)
    return avg_cliche

if __name__ == "__main__":
	df = pd.read_csv('cliche_words.tsv', sep='\t')
	lyrics = ""
	# See if arg is file
	try:
		with open(sys.argv[1], 'r') as f:
		    lyrics = f.read()
	except:
		lyrics = sys.argv[1]
	print get_cliche_rating(lyrics, df)
