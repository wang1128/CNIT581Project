__author__ = 'penghao'




from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import csv

ckey = '9PeXML0SJib7ALGYvlyG9eVTH'
csecret = 'w1E7OFBCMYY0LbXNGynlx43ZDfzSrqHRZzYqdxQ1T8sugfJL7J'
atoken = '273809152-lr82uKL4jwRZNFsMPDymFx1r31mDIradM2i9qfRg'
asecret = 'ACgsdyBXD3jdA3FaV37KRnkmdsS4JxVM1CA4RZ5Hbjvmr'
csvFile = open('result.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
class listener(StreamListener):

    def on_data(self, data):
    	#csvWriter.writerows(data)
        f.write(data + '\n')
        print(data)
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

csvFile = open('result.csv', 'a')
csvWriter = csv.writer(csvFile)

f = open('workfile.txt', 'w')


twitterStream = Stream(auth, listener())
twitterStream.filter(track=['refugee'])


f.close()
csvFile.close()