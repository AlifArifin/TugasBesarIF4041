# library
from random import random, randint
import json
import time

# import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# variables that contains the user credentials to access Twitter API 
access_token = "726598427123970048-wIxNMJMIGdJoaEseYz8k3JAHAKHyyo5"
access_token_secret = "84EQCNgCkrsIKFMLGGXGmlitSjN6IR6TjP4wev3V8qU8q"
consumer_key = "f5SPtkc7DOMNEpHAKLVIM2AlF"
consumer_secret = "GQCnikaCWAZuLLPBQpKDr2eBPwkSoF0dPFkgndhHquQLXCjRlQ"

class SamplingDataStream() :
    def __init__(self, max_sample = 200) :
        # for sampling purpose
        self.counter = 0 # for counting the order of the tweet
        self.max_sample = max_sample # maximum size of sample

        # list of tweets sample
        self.samples = [] # container for sample
        self.fill_sample = [] # container for index sample

    def reservoir(self, tweet) :
        # random sample of fixed size
        # using reservoir sampling
        self.counter += 1

        # count the probability of tweet being accepted
        if (self.counter <= self.max_sample) :
            prob = 1
        else :
            prob = self.max_sample/self.counter
        # end if
        
        rand_num = random()

        if (prob >= rand_num) :
            if (len(self.samples) < self.max_sample) :
                # if samples is not full yet
                self.samples.append(json.loads(tweet))
                self.fill_sample.append(self.counter)
            else :
                # find random number between 0 - 199 (because index is start from 0)
                # then, change the tweet in that index with the new tweet
                rand_index = randint(0, self.max_sample - 1)
                self.samples[rand_index] = json.loads(tweet)
                self.fill_sample[rand_index] = self.counter
            # end if
        # end if
        # if not then the tweet will be ignored

# TweetStreaming class
class TweetStreaming(StreamListener):
    def __init__(self, time_limit = 60) :
        super().__init__()

        # only stream tweet for time_limit (in seconds)
        self.start_time = time.time()
        self.limit = time_limit
        self.all = []

        # class sampling
        self.sampling = SamplingDataStream(200)

        # file
        self.outfile = None
        self.allfile = None

    # get the data (tweet)
    def on_data(self, data):
        # if still in range (time)
        if (time.time() - self.start_time) < self.limit :
            # do sampling (call sampling algorithm)
            self.sampling.reservoir(data)
            self.all.append(json.loads(data))
            # for the feedback to makesure that the code is running
            print (self.sampling.counter)
            return True
        else :
            # if time already run out write sample to file
            self.write_file()
            return False

    def on_error(self, status):
        print("Error: ", str(status))
        # write the sample to file
        self.write_file()
        return False

    def write_file(self) :
        self.outfile = open('sample.json', 'w')
        json.dump(self.sampling.samples, self.outfile, indent=4)
        self.outfile.close()

        self.allfile = open('all-sample.json', 'w')
        json.dump(self.all, self.allfile, indent=4)
        self.allfile.close()

        print ("Lama waktu streaming: ", str(self.limit), " detik") 
        print ("Data stream yang didapatkan: ", str(len(self.all)), " tweets")
        print ("Data stream yang masuk ke dalam sample: ", str(len(self.sampling.samples)), " tweets")
        print ("Isi sampel (isi array merupakan index dari data stream)")
        for index in self.sampling.fill_sample :
            print("%03d" % index, end=" ")
            
if __name__ == '__main__':

    # this handles Twitter authetification and the connection to Twitter Streaming API
    l = TweetStreaming(10 * 60)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # this line filter Twitter Streams to capture data by the spesific keywords
    stream.filter(track=['tech'])