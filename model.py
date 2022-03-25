import nltk
import os
from os import getcwd
import numpy as np
import pandas as pd
from nltk.corpus import twitter_samples

nltk.download('twitter_samples')
nltk.download('stopwords')

import json

dirnamePos = os.path.dirname(__file__)
filenamePos = os.path.join(dirnamePos, 'fildata/POSv2.json')

with open(filenamePos) as f:
  pos = json.load(f)

dirnameNeg = os.path.dirname(__file__)
filenameNeg = os.path.join(dirnameNeg, 'fildata/NEGv2.json')

with open(filenameNeg) as f:
  neg = json.load(f)


filePath = f"{getcwd()}/../tmp2/"

nltk.data.path.append(filePath)

stopwords_filipino = ["akin","aking","ako","alin","am","amin","aming","ang","ano","anumang","apat","at","atin","ating","ay","bababa","bago","bakit","bawat","bilang","dahil","dalawa","dapat","din","dito","doon","gagawin","gayunman","ginagawa","ginawa","ginawang","gumawa","gusto","habang","hanggang","hindi","huwag","iba","ibaba","ibabaw","ibig","ikaw","ilagay","ilalim","ilan","inyong","isa","isang","itaas","ito","iyo","iyon","iyong","ka","kahit","kailangan","kailanman","kami","kanila","kanilang","kanino","kanya","kanyang","kapag","kapwa","karamihan","katiyakan","katulad","kaya","kaysa","ko","kong","kulang","kumuha","kung","laban","lahat","lamang","likod","lima","maaari","maaaring","maging","mahusay","makita","marami","marapat","masyado","may","mayroon","mga","minsan","mismo","mula","muli","na","nabanggit","naging","nagkaroon","nais","nakita","namin","napaka","narito","nasaan","ng","ngayon","ni","nila","nilang","nito","niya","niyang","noon","o","pa","paano","pababa","paggawa","pagitan","pagkakaroon","pagkatapos","palabas","pamamagitan","panahon","pangalawa","para","paraan","pareho","pataas","pero","pumunta","pumupunta","sa","saan","sabi","sabihin","sarili","sila","sino","siya","tatlo","tayo","tulad","tungkol","una","walang"]
nltk.download('stopwords')

from nltk.corpus import stopwords

taglish = stopwords.words('english') + stopwords_filipino

# print(taglish)

import re
import string
import numpy as np

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer



def process_tweet(tweet):
    """Process tweet function.
    Input:
        tweet: a string containing a tweet
    Output:
        tweets_clean: a list of words containing the processed tweet
    """
    stemmer = PorterStemmer()
    stopwords_english = taglish
    # remove stock market tickers like $GE
    tweet = re.sub(r'\$\w*', '', tweet)
    # remove old style retweet text "RT"
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    # remove links
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
    # remove hashtags
    tweet = re.sub(r'#', '', tweet)
    # tokenize
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)

    tweets_clean = []
    for word in tweet_tokens:
        if (word not in stopwords_english and  # remove stopwords
                word not in string.punctuation):  # remove punctuation
            # tweets_clean.append(word)
            stem_word = stemmer.stem(word)  # stemming word
            tweets_clean.append(stem_word)

    return tweets_clean


def build_freqs(tweets, ys):
    """Build frequencies.
    Input:
        tweets: a list of tweets
        ys: an m x 1 array with the sentiment label of each tweet
            (either 0 or 1)
    Output:
        freqs: a dictionary mapping each (word, sentiment) pair to its
        frequency
    """
    # Convert np array to list since zip needs an iterable.
    # The squeeze is necessary or the list ends up with one element.
    yslist = np.squeeze(ys).tolist()

    # Start with an empty dictionary and provide data by looping all tweets
    freqs = {}
    for y, tweet in zip(yslist, tweets):
        for word in process_tweet(tweet):
            pair = (word, y)
            if pair in freqs:
                freqs[pair] += 1
            else:
                freqs[pair] = 1

    return freqs


all_positive_tweets = pos
all_negative_tweets = neg

# print(len(all_positive_tweets))
# print(len(all_negative_tweets))

test_pos = all_positive_tweets[2400:]
train_pos = all_positive_tweets[:3000]
test_neg = all_negative_tweets[2400:]
train_neg = all_negative_tweets[:3000]

train_x = train_pos + train_neg 
test_x = test_pos + test_neg

# print(len(test_pos))
# print(len(train_pos))
# print(len(test_neg))
# print(len(train_neg))
# print(process_tweet(train_x[4]))
# print(train_x)

train_y = np.append(np.ones((len(train_pos), 1)), np.zeros((len(train_neg), 1)), axis=0)
test_y = np.append(np.ones((len(test_pos), 1)), np.zeros((len(test_neg), 1)), axis=0)

# print(train_y)
# print("train_y.shape = " + str(train_y.shape))
# print("test_y.shape = " + str(test_y.shape))

freqs = build_freqs(train_x, train_y)

# print("type(freqs) = " + str(type(freqs)))
# print("len(freqs) = " + str(len(freqs.keys())))
# print(freqs)
# print('raw data: \n', train_x[2])
# print('\nprocessed data: \n', process_tweet(train_x[2]))


# UNQ_C1 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
def sigmoid(z): 
    '''
    Input:
        z: is the input (can be a scalar or an array)
    Output:
        h: the sigmoid of z
    '''
    
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    # calculate the sigmoid of z
    h = 1/(1+np.exp(-z))
    ### END CODE HERE ###
    
    return h
if (sigmoid(0) == 0.5):
    print('sigmoid = goods')
else:
    print('err')

if (sigmoid(4.92) == 0.9927537604041685):
    print('sigmoid test2 = goods')
else:
    print('err')
-1 * (1 - 0) * np.log(1 - 0.9999) # loss is about 9.2

# UNQ_C2 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
def gradientDescent(x, y, theta, alpha, num_iters):
    '''
    Input:
        x: matrix of features which is (m,n+1)
        y: corresponding labels of the input matrix x, dimensions (m,1)
        theta: weight vector of dimension (n+1,1)
        alpha: learning rate
        num_iters: number of iterations you want to train your model for
    Output:
        J: the final cost
        theta: your final weight vector
    Hint: you might want to print the cost to make sure that it is going down.
    '''
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    # get 'm', the number of rows in matrix x
    m = x.shape[0]
    
    for i in range(0, num_iters):
        
        # get z, the dot product of x and theta
        z = np.dot(x,theta)
        
        # get the sigmoid of z
        h = sigmoid(z)
        
        # calculate the cost function
        J = -1./m * (np.dot(y.transpose(), np.log(h)) + np.dot((1-y).transpose(),np.log(1-h)))
        # print(J)
        # update the weights theta
        theta = theta - (alpha/m) * np.dot(x.transpose(),(h-y))
        
    ### END CODE HERE ###
    J = float(J)
    return J, theta

# using numpy PRNG functions
np.random.seed(1)

# X input is 10 x 3 with ones for the bias terms
tmp_X = np.append(np.ones((10, 1)), np.random.rand(10, 2) * 2000, axis=1)

# Y Labels are 10 x 1
tmp_Y = (np.random.rand(10, 1) > 0.35).astype(float)

# gradient descent
tmp_J, tmp_theta = gradientDescent(tmp_X, tmp_Y, np.zeros((3, 1)), 1e-8, 700)

# print(f"The cost for training is {tmp_J:.8f}.")
# print(f"The resulting vector of weight is {[round(t, 8) for t in np.squeeze(tmp_theta)]}")

# UNQ_C3 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)

def extract_features(tweet, freqs):
    '''
    Input: 
        tweet: a list of words for one tweet
        freqs: a dictionary corresponding to the frequencies of each tuple (word, label)
    Output: 
        x: a feature vector of dimension (1,3)
    '''
    # process_tweet tokenizes, stems, and removes stopwords
    word_l = process_tweet(tweet)
    
    # 3 elements in the form of a 1 x 3 vector
    x = np.zeros((1, 3)) 
    
    #bias term is set to 1
    x[0,0] = 1 
    
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    
    # loop through each word in the list of words
    for word in word_l:
        
        # increment the word count for the positive label 1
        x[0,1] += freqs.get((word, 1.0),0)
        
        # increment the word count for the negative label 0
        x[0,2] += freqs.get((word, 0.0),0)
        
    ### END CODE HERE ###
    assert(x.shape == (1, 3))
    return x


#test 1
# tmp1 = extract_features(train_x[0], freqs)
# print(tmp1)
# test 2
# tmp2 = extract_features('blorb bleeeeb bloooob', freqs)

# print(tmp2)
# print(np.zeros((3, 1)))

X = np.zeros((len(train_x), 3))#array structure
for i in range(len(train_x)):#loop through train x to extract features on each
    X[i, :]= extract_features(train_x[i], freqs)

Y = train_y # training labels

J, theta = gradientDescent(X, Y, np.zeros((3, 1)), 1e-9, 1500)

# print(f"The cost after training is {J:.8f}.")

# print(f"The resulting vector of weights is {[round(t, 8) for t in np.squeeze(theta)]}")

def predict_tweet(tweet, freqs, theta):
    '''
    Input: 
        tweet: a string
        freqs: a dictionary corresponding to the frequencies of each tuple (word, label)
        theta: (3,1) vector of weights
    Output: 
        y_pred: the probability of a tweet being positive or negative
    '''
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    
    # extract the features of the tweet and store it into x
    x = extract_features(tweet,freqs)
    
    # make the prediction using x and theta
    y_pred =sigmoid(np.dot(x,theta))
    
    ### END CODE HERE ###
    
    return y_pred


# for tweet in ['ako ay masayang masaya', 'ikaw ay masama', 'talgang natuwa ako', 'salamat', 'salamat salamat', 'salamat salamat salamat']:
#     print( '%s -> %f' % (tweet, predict_tweet(tweet, freqs, theta)))

# positive = 'masaya ako ngayon'
# predict_tweet(positive, freqs, theta)

# negative = 'galit ako ngayon'
# predict_tweet(negative, freqs, theta)


# UNQ_C5 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
def test_logistic_regression(test_x, test_y, freqs, theta):
    """
    Input: 
        test_x: a list of tweets
        test_y: (m, 1) vector with the corresponding labels for the list of tweets
        freqs: a dictionary with the frequency of each pair (or tuple)
        theta: weight vector of dimension (3, 1)
    Output: 
        accuracy: (# of tweets classified correctly) / (total # of tweets)
    """
    
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    
    # the list for storing predictions
    y_hat = []
    
    for tweet in test_x:
        # get the label prediction for the tweet
        y_pred = predict_tweet(tweet, freqs, theta)
        
        if y_pred > 0.5:
            # append 1.0 to the list
            y_hat.append(1)
        else:
            # append 0 to the list
            y_hat.append(0)

    # With the above implementation, y_hat is a list, but test_y is (m,1) array
    # convert both to one-dimensional arrays in order to compare them using the '==' operator
    accuracy = (y_hat==np.squeeze(test_y)).sum()/len(test_x)
    print(f"Total True Prediction: {(y_hat==np.squeeze(test_y)).sum()}")
    print(f"total number of predictions: {len(test_x)}")

    ### END CODE HERE ###
    
    return accuracy

def test_precision(test_x, test_y, freqs, theta):
    
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    
    # the list for storing predictions
    y_hat = []
    x_hat = []
    
    for tweet in test_x:
        # get the label prediction for the tweet
        y_pred = predict_tweet(tweet, freqs, theta)
        
        if y_pred > 0.5 and tweet in test_pos: #true positive
            y_hat.append(1)
        else:
            # append 0 to the list
            y_hat.append(0)

    for tweet in test_x:
        # get the label prediction for the tweet
        y_pred = predict_tweet(tweet, freqs, theta)
        
        if y_pred > 0.5 and tweet in test_pos: #true positive
            x_hat.append(1)
        
        if y_pred > 0.5 and tweet not in test_pos: #false positive
            x_hat.append(1)

        else:
            # append 0 to the list
            x_hat.append(0)
            
    # With the above implementation, y_hat is a list, but test_y is (m,1) array
    # convert both to one-dimensional arrays in order to compare them using the '==' operator
    presision = (sum(y_hat)/sum(x_hat))
    print(f"TRUE positives: {sum(y_hat)}")
    print(f"total predicted positives: {sum(x_hat)}")

    ### END CODE HERE ###
    
    return presision

def test_recall(test_x, test_y, freqs, theta):
    
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    
    # the list for storing predictions
    y_hat = []
    x_hat = []
    
    for tweet in test_x:
        # get the label prediction for the tweet
        y_pred = predict_tweet(tweet, freqs, theta)
        
        if y_pred > 0.5 and tweet in test_pos: #true positive
            y_hat.append(1)
        else:
            # append 0 to the list
            y_hat.append(0)

    for tweet in test_x:
        # get the label prediction for the tweet
        y_pred = predict_tweet(tweet, freqs, theta)
        
        if y_pred > 0.5 and tweet in test_pos: #true positive
            x_hat.append(1)
        
        if y_pred < 0.5 and tweet not in test_neg: #false negative
            x_hat.append(1)

        else:
            # append 0 to the list
            x_hat.append(0)
            
    # With the above implementation, y_hat is a list, but test_y is (m,1) array
    # convert both to one-dimensional arrays in order to compare them using the '==' operator
    recall = (sum(y_hat)/sum(x_hat))
    print(f"TRUE positives: {sum(y_hat)}")
    print(f"total actual positive: {sum(x_hat)}")

    ### END CODE HERE ###
    
    return recall

########### PERFORMANCE TESTS #################

# tmp_recall = test_recall(test_x, test_y, freqs, theta)
# print(f"Logistic regression model's recall = {tmp_recall:.4f}")

# tmp_precision = test_precision(test_x, test_y, freqs, theta)
# print(f"Logistic regression model's precision = {tmp_precision:.4f}")

# tmp_accuracy = test_logistic_regression(test_x, test_y, freqs, theta)
# print(f"Logistic regression model's accuracy = {tmp_accuracy:.4f}")

########### PERFORMANCE TESTS #################

# print('Label Predicted Tweet')
# for x,y in zip(test_x,test_y):
#     y_hat = predict_tweet(x, freqs, theta)

#     if np.abs(y - (y_hat > 0.5)) > 0:
#         print('Raw data:', x)
#         print('Processed data:', process_tweet(x))
#         print('%d\t%0.8f\t%s' % (y, y_hat, ' '.join(process_tweet(x)).encode('ascii', 'ignore')))

# tweet = 'online class'
# print(process_tweet(tweet))
# y_hat = predict_tweet(tweet, freqs, theta)
# print(y_hat)
# if y_hat > 0.5:
#     print('Positive sentiment')
# else: 
#     print('Negative sentiment')