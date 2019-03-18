#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
consumer_key = "W7d93p1DX6GXdbyIsxDf3YkNB"
consumer_secret = "ZXFpIZICi6B4AWsJIlcr1QGrVL2VBiD7zNgpHVJtbOz6wJGeP9"
access_key = "1060120750164631553-dgB0toYcHAPGZbI95OgdDOuiNgoJIV"
access_secret = "JmrOXgOWEvCR2kQwtKV8zDtS4F97bJTq5oHJgNuqy3aEH"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

        #This handles Twitter authetification and the connection to Twitter Streaming API
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        stream = Stream(auth, l)

        #This line filter Twitter Streams to capture data by the keywords:stop words are used as they would span most tweets
        stream.filter(languages=["en"], track=['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'could', 'did', 'do', 'does','doing','down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have', 'having', 'he', 'he\'d', 'he\'ll', 'he\'s', 'her', 'here', 'here\'s', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'how\'s', 'I', 'i', 'I\'d', 'I\'ll', 'Ill', 'ill', 'I\'m', 'Im', 'im', 'I\'ve','Ive', 'ive', 'if', 'in', 'into', 'is', 'it', 'it\'s', 'its', 'itself', 'let\'s', 'lets', 'me', 'more', 'most', 'my', 'myself', 'nor', 'of', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', 'she', 'she\'d', 'shed' ,'she\'ll', 'she\'s', 'shes', 'should', 'so', 'some', 'such', 'than', 'that', 'that\'s', 'thats', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'there\'s', 'theres', 'these', 'they', 'they\'d', 'theyd','they\'ll', 'theyll', 'they\'re', 'theyre', 'they\'ve', 'theyve', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'u', 'very', 'was', 'we', 'we\'d','wed', 'we\'ll', 'well', 'we\'re', 'we\'ve', 'were', 'what', 'what\'s','whats', 'when', 'when\'s', 'whens', 'where', 'where\'s', 'wheres', 'which', 'while', 'who', 'who\'s', 'whos', 'whom', 'why', 'why\'s', 'whys', 'with', 'would', 'you', 'you\'d', 'youd', 'you\'ll', 'youll', 'you\'re', 'youre', 'you\'ve', 'youve', 'your', 'yours', 'yourself', 'yourselves'])
