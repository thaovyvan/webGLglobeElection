import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#this is a test

consumerKey = 'SWv4JwjPAUDwfgI4BdxhOROvS'
consumerSecret = 'onxHRG5Hvj8jKK5qPqEl3tE24kdz8LjW80Wz00rGWSbN8QAvbt'
accessKey = '70789998-HTz3dnrVkoSeSfXP7OuJGDZ1ne043Y8w1ZbA0AZNH'
accessSecret = 'xlx7RwRinfyCEMRXcEohUblLopcus37c32Oe4FZIE1J0A'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth)

#geoTweetsHillary = api.search(q = '#ImWithHer', count = 1000)
#geoTweetsTrump = api.search(q = '#MakeAmericaGreatAgain', count = 1000)

newList = []
count = 0
		
class listener(StreamListener):
    def get_coordinates(self, status):
        global count
        if count <= 1000:
            json_status = json.loads(status)
            coords = json_status["coordinates"]
            if coords != None:
               print(coords["coordinates"])
               longitudeCoord = coords["coordinates"][0]
               latitudeCoord = coords["coordinates"][1]
               newList.append(json_status)
               file.write(str(lon) + ",")
               file.write(str(lat) + "\n")
               count += 1
            return True
        else:
            file.close()
            return False

    def on_error(self, status):
        print(status)

twitterStream = Stream(auth, listener())
geoTweetsHillary = twitterStream.filter(track=["#ImWithHer"])
geoTweetsDonald = twitterStream.filter(track=["#MakeAmericaGreatAgain"])
