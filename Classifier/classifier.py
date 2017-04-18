import nltk 
from textblob.classifiers import NaiveBayesClassifier
from new_lists import first_level

from new_lists import EduTech
from new_lists import Leisure
from new_lists import Places

from new_lists import Education
from new_lists import Technology
from new_lists import News
from new_lists import Entertainment
from new_lists import Lifestyle
from new_lists import Sports

from new_lists import Exams
from new_lists import Educational_Institution
from new_lists import Devices
from new_lists import Automobiles
from new_lists import Social_Media
from new_lists import Movies
from new_lists import Shows
from new_lists import Fashion
from new_lists import Food
from new_lists import Festival
from new_lists import Business
from new_lists import Indoor_Sports
from new_lists import Outdoor_Sports


class Classify:
    
    def get_tweet(self):
        tfile = open("tweets.txt",'r')  #Tweet from twitter saved in file
        for line in tfile:
            tweet = line.strip()
        tfile.close()
        return tweet

    def classify_r1(self):
        
        lists = first_level                 #main categories
        cfy = NaiveBayesClassifier(lists)
        tweet = self.get_tweet()
        one = cfy.classify(tweet)
        return one

    def classify_r2(self,one):              #second level

        if(one=='EduTech'):
            lists = EduTech
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            two = cfy.classify(tweet)
            return two
        elif(one=='Leisure'):
            lists = Leisure
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            two = cfy.classify(tweet)
            return two
        else:
            lists = Places
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            two = cfy.classify(tweet)
            return two

    def classify_r3(self,two):          #third level
        
        if(two=='Education'):               #edtech categories
            lists = Education
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            three = cfy.classify(tweet)
            return three
        elif(two=='Technology'):
            lists = Technology
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            three = cfy.classify(tweet)
            return three
        elif(two=='News'):
            lists = News
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            three = cfy.classify(tweet)
            return three

        elif(two=='Entertainment'):                 #Leisure
            lists = Entertainment
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            three = cfy.classify(tweet)
            return three
        elif(two=='Lifestyle'):
            lists = Lifestyle
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            three = cfy.classify(tweet)
            return three
        elif(two=='Sports'):
            lists = Sports
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            three = cfy.classify(tweet)
            return three

    def classify_r4(self,three):  #fourth level
        
        if(three=='Exams'):     #Education sub categories
            lists = Exams
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            four = cfy.classify(tweet)
            return four
        elif(three=='Educational_Institution'):
            lists = Educational_Institution 
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            four = cfy.classify(tweet)
            return four
       
        elif(three=='Devices'):         #Technology sub Categories   
            lists = Devices
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            four = cfy.classify(tweet)
            return four
        elif (three=='Automobiles'):
            lists = Automobiles
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            four = cfy.classify(tweet)
            return four
        elif (three=='Social_Media'):
            lists = Social_Media
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            two = cfy.classify(tweet)
            return four

        elif (three=='Business'):              #News sub Category
            lists = Business
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            four = cfy.classify(tweet)
            return four
        elif (three=='Politics'):             
            lists = Politics
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            four = cfy.classify(tweet)
            return four
        
        elif (three=='Movies'):              #Entertainment sub category
            lists = Movies
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            four = cfy.classify(tweet)
            return four
       
        elif (three=='Shows'):                  
            lists = Shows
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            four = cfy.classify(tweet)
            return four


        elif (three=='Fashion'):              #Lifestyle sub Category
            lists = Fashion
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            four = cfy.classify(tweet)
            return four
        elif (three=='Food'):                
            lists = Food
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            four = cfy.classify(tweet)
            return four
        elif (three=='Festival'):              
            lists = Festival
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            four = cfy.classify(tweet)
            return four


        elif (three=='Indoor Sports'):              #Sports sub category
            lists = Indoor_Sports
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            four = cfy.classify(tweet)
            return four
        elif (three=='Outdoor Sports'):             
            lists = Outdoor_Sports
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            four = cfy.classify(tweet)
            return four
        elif (three=='Competitions'):             
            lists = Competitions
            cfy = NaiveBayesClassifier(lists)
            tweet = self.get_tweet()
            four = cfy.classify(tweet)
            return four

        
  


    

