from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

try:
    import json
except ImportError:
    import simplejson as json

class TweetFetch:
   
    def fetchFromFile(self):
        t_file = open("tweets.txt",'r')
        for line in t_file:
            tweet = line.strip()
        return tweet

    def status(self):
        
        ACCESS_TOKEN = '704014440409108480-lCPbJXuHznMhKqrs5eawZ4UIUNMUVzE'
        ACCESS_SECRET = '4R9B8kGQVwkedwCp5JnL9AT5jGWQI3Revx1h7eYPt6GRf'
        CONSUMER_KEY = 'Gpd8ogDa5nDpxPTwk1uBoMxPy'
        CONSUMER_SECRET = 'H7UI3cEBa9ES5oifTrSEbuk0jnNmlGkSOX4SotJeERKJzLonjI'

        oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
        twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
        iterator = twitter_stream.statuses.sample()
         
        tweet_count = 1
        t_file = open("tweets.txt",'w')
        for tweet in iterator:
            t_file.write(json.dumps(tweet))
            t_file.close()
            tweet_count-=1
            if(tweet_count<=0):
                break
        return 'Fetched'

    def fetchFromTwitter(self):

        t_file = open("tweets.txt",'r')
        for line in t_file:
            tweet = json.loads(line.strip())
            if 'text' in tweet: # only messages contains 'text' field is a tweet
                return tweet['text'] # content of the tweet
                t_file.close()
