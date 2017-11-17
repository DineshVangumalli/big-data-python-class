# %load code/twitter_streaming_sports_DV.py


#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "131711504-uteEX6y8zoi0v4miLzEjZefg22ZZ8TgukyU9bHYW"
access_token_secret = "UH3dk5s00euTgzJ92xveSSi7b84Aw2rrrtFeHelV5rmIv"
consumer_key = "7lKe94q4mhbeINgp1hFWmpdGj"
consumer_secret = "T46JL4SAhMK3EmiXpCFzSVwQ6ipvQ0xfqHBGbAUbPBVjtbDDp1"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):        
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'cricket', 'soccer', 'basketball', 'baseball', 'tennis'
    stream.filter(track=['cricket', 'soccer', 'basketball', 'baseball', 'tennis'])