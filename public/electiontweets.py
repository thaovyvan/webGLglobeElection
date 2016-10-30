import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
import csv

consumerKey = "a51rmH4LvKMx8YcNWlcZLZ6Hp"
consumerSecret = "XqEmmbzWqXOYF53rOmsSk6JE9qaxDSfDU12v06tkbnO6WaS58S"
accessKey = "39445982-9UFWSD9l6tXKZVaN3RcI3oLziA6Hbi643yKCkw1Qm"
accessSecret = "Ztitr2jqovae4nbkFO7jnBybS0GgDOJhsRAoJGknYIXxq"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.secure = True
auth.set_access_token(accessKey, accessSecret)

api = tweepy.API(auth)

data = []

class SListener(StreamListener):

	def __init__(self, api=None):
		super(SListener, self).__init__()
		self.num_tweets = 0

	def on_status(self, tweet):
		if(tweet.place):
			centroid = [0,0]
			box = tweet.place.bounding_box.coordinates[0]
			for i in range(0, len(box)):
				centroid[0] += box[i][0]
				centroid[1] += box[i][1]
				centroid[0] = centroid[0]/4
				centroid[1] = centroid[1]/4
				self.num_tweets += 1
				print(centroid)
				data.append(centroid)
			if self.num_tweets < 300:
				return True
			else:
				return False

l = SListener()
streamer = tweepy.Stream(auth=auth, listener=l)
setTerms = ['ImWithHer']
streamer.filter(track = setTerms)

with open('electiontweets_hillary.csv', 'wb') as csvfile:
	tweetwriter = csv.writer(csvfile, delimiter=',')
	tweetwriter.writerow(data)
