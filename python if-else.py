import pandas as pd
import re

from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet

data = pd.read_csv('data/train.csv',
                   usecols = ['Id', 'ProductId', 'UserId', 'HelpfulnessNumerator', 'Score', 'Time', 'Summary', 'Text'],
                   dtype = {'HelpfulnessNumerator': "int8", "Score": "float16"},
                   chunksize=30000
                   )

dataset = data.get_chunk(30000)

# Converting Time column into YYYY-MM-DD format of object type
dataset['Time'] = pd.to_datetime(dataset['Time']).dt.date

# for chunk in data:
#     chunk['Time'] = pd.to_datetime(chunk['Time']).dt.date


# Preprocessing Text Column
def clean(text):
    text = re.sub('[^A-Za-z]+', ' ', str(text))
    
    return text

    # Step 1: Cleaning the Text
dataset['Text'] = dataset['Text'].apply(clean)

    # Step 2, 3, 4: Tokenization, POS Tagging, Stop words removal

# POS tagger dictionary
pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}

def token_stop_pos(text):
    tags = pos_tag(word_tokenize(text))
    newlist = []
    for word, tag in tags:
        if word.lower() not in set(stopwords.words('english')):
            newlist.append(tuple([word, pos_dict.get(tag[0])]))
    return newlist

dataset['Text'] = dataset['Text'].apply(token_stop_pos)

    # Step 5: Lemmatizer
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

def lemmatize(pos_data):
    lemma_rew = " "
    for word, pos in pos_data:
        if not pos:
            lemma = word
            lemma_rew = lemma_rew + " " + lemma
        else:
            lemma = wordnet_lemmatizer.lemmatize(word, pos=pos)
            lemma_rew = lemma_rew + " " + lemma
    
    return lemma_rew

dataset['Text'] = dataset['Text'].apply(lemmatize)


from textblob import TextBlob

# function to calculate subjectivity
def getSubjectivity(review):
    return TextBlob(review).sentiment.subjectivity

# function to calculate polarity
def getPolarity(review):
    return TextBlob(review).sentiment.polarity

# function to analyze the reviews
def analysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'

fin_data = pd.DataFrame(dataset['Text'])

# fin_data['Subjectivity'] = fin_data['Lemma'].apply(getSubjectivity) 
fin_data['Polarity'] = fin_data['Lemma'].apply(getPolarity) 
fin_data['Analysis'] = fin_data['Polarity'].apply(analysis)


for chunk in data:
    # Converting into Date
    chunk['Time'] = pd.to_datetime(chunk['Time']).dt.date
    
    # Cleaning the text
    chunk['Text'] = chunk['Text'].apply(clean)
    
    # Tokenization
    chunk['Text'] = chunk['Text'].apply(word_tokenize)
    
    



MemoryError: Unable to allocate 961. GiB for an array with shape (1397461, 92332) and data type float64




