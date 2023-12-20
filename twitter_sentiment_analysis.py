# -*- coding: utf-8 -*-
"""Twitter Sentiment Analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zFt5fIedlOQ6r-tLH39Lsvkd5VvMlCtG
"""

#Installing the Kaggle Library
! pip install kaggle

"""Upload your Kaggle.json file"""

# configuring the path of Kaggle.json file
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# API to fetch the dataset from kaggle
!kaggle datasets download -d kazanova/sentiment140

"""Importing Twitter Sentiment Dataset"""

#extracting the compressed dataset

from zipfile import ZipFile
dataset = '/content/sentiment140.zip'

with ZipFile(dataset,'r') as zip:
  zip.extractall()
print ('The dataset is extracted')

! pip install kaggle

"""Uploading your Kaggle.json file"""

# configuring the path of Kaggle.json file
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

"""Importing Twitter Sentiment Dataset"""

# API to fetch the dataset from google
!kaggle datasets download -d kazanova/sentiment140

#extracting the compressed dataset

from zipfile import ZipFile
dataset = '/content/sentiment140.zip'

with ZipFile(dataset,'r') as zip:
  zip.extractall()
print ('The dataset is extracted')

import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import nltk
nltk.download('stopwords')

#printing the stopwords in english
print (stopwords.words('english'))

#loading the data from csv file to pands dataframe
twitter_data = pd.read_csv("/content/training.1600000.processed.noemoticon.csv",encoding = 'ISO-8859-1')

# checking the number of rows and colums
twitter_data.shape

#printing the first 5 rows of the dataframe
twitter_data.head()

# naming the columns and reading the dataset again

column_names = ['target', 'id', 'date', 'flag','user','text']
twitter_data = pd.read_csv ('/content/training.1600000.processed.noemoticon.csv', names=column_names, encoding  = 'ISO-8859-1')

# checking the number of rows and colums
twitter_data.shape

#printing the first 5 rows of the dataframe
twitter_data.head()

#counting the number of missing values in the dataset
twitter_data.isnull().sum()

# checking the distribution of target cloumn
twitter_data['target'].value_counts()

twitter_data.replace({'target':{4:1}}, inplace=True)

# checking the distribution of target cloumn
twitter_data['target'].value_counts()

port_stem = PorterStemmer()

def stemming (content):

  stemmed_content = re.sub('[^a-zA-Z]','',content)
  stemmed_content = stemmed_content.lower()
  stemmed_content = stemmed_content.split()
  stemmed_content = [port_stem.stem(word)for word in stemmed_content if not word in stopwords.words('english')]
  stemmed_content = ' ',join(stemmed_content)

  return stemmed_content

import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

def stemming(text):
    return " ".join([stemmer.stem(word) for word in text.split()])

twitter_data['stemmed_content'] = twitter_data['text'].apply(stemming)

twitter_data.head()

print(twitter_data['stemmed_content'])

print(twitter_data['stemmed_content'])

print(twitter_data['target'])

#separating the data and label
X = twitter_data['stemmed_content'].values
Y = twitter_data['target'].values

print(X)

print(Y)

"""splitting the data to training data and test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, stratify=Y,  random_state=2)

print(X.shape, X_train.shape, X_test.shape)

print(X_train)

print(X_test)

"""Feature extraction vectorizer"""

# converting textual data to numarical data

vectorizer = TfidfVectorizer()

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

print(X_train)

print(X_test)

"""Training the Machine Learning Model"""

model = LogisticRegression(max_iter=1000)

model.fit(X_train, Y_train)

"""Model Evaluation

Accuracy score
"""

#accuracy score on the training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)

print('Accuracy score on the training data :', training_data_accuracy)

# accuracy score on the test data
 X_test_predection = model.predict(X_test)
 test_data_accuracy = accuracy_score(Y_test, X_test_predection)

print('Accuracy score on the training data :', test_data_accuracy)

"""Model Accuracy is 79.8 %

Saving the Trained Model
"""

import pickle

filename = 'trained_model.sav'
pickle.dump(model,open(filename,'wb'))

"""Using the saved model for future predections"""

#loading the saved model
Loaded_model = pickle.load(open('/content/trained_model.sav','rb'))

X_new = X_test[200]
print(Y_test[200])

prediction = model.predict(X_new)
print(prediction)

if (prediction[0] ==0 ):
   print('Negative Tweet')

else:
  print ('Positive Tweet')

X_new = X_test[3]
print(Y_test[3])

prediction = model.predict(X_new)
print(prediction)

if (prediction[0] ==0 ):
   print('Negative Tweet')

else:
  print ('Positive Tweet')