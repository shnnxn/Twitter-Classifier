import nltk 
from textblob.classifiers import NaiveBayesClassifier
from preprocessed_tweets import first_level
from preprocessed_tweets import Technology

class Classify:
    
    
    def classify_r1(self):
        
        lists = first_level

        cfy = NaiveBayesClassifier(lists)
        tfile = open("tweets.txt",'r')
        for line in tfile:
            tweet = line.strip()
        one = cfy.classify(tweet)
        
        tfile.close()
        
        return one

    def classify_r2(self,one):
        if(one=='Technology'):
            
            lists = Technology

            cfy = NaiveBayesClassifier(lists)
            tfile = open("tweets.txt",'r')
            for line in tfile:
                tweet = line.strip()
            two = cfy.classify(tweet)
        
            tfile.close()
        
            return two
        
 

    

