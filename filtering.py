# library
from bitarray import bitarray
import hashlib
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

class FilteringDataStream() :
    def __init__(self, keys) :
        # length of bit array
        self.n = 200
        self.keys = keys
        self.bit_array = bitarray(self.n)

        self.initialization()

    # have 3 hash function
    def hash_func_1 (self, data) :
        return (data * 392 // 13 * 11 + 13 * 4) % self.n

    def hash_func_2 (self, data) :
        return ((data // 381 * 7 + 32 * 4) // 19) % self.n

    def hash_func_3 (self, data) :
        return (data * 1219) % self.n

    def hash_func_4 (self, data) :
        return (data) % self.n

    # def hash_func (self, salt, data) :
    #     hash_obj = hashlib.sha256((str(data) + salt).encode())
    #     hex = hash_obj.hexdigest()
    #     return int(hex, 16) % self.n

    def initialization(self) :
        # keys is list of keys

        # init for bit_array first
        for i in range (0, self.n) :
            self.bit_array[i] = 0

        for key in self.keys :
            res_1 = self.hash_func_1(key)
            self.bit_array[res_1] = 1

            res_2 = self.hash_func_2(key)
            self.bit_array[res_2] = 1

            res_3 = self.hash_func_3(key)
            self.bit_array[res_3] = 1

            res_4 = self.hash_func_4(key)
            self.bit_array[res_3] = 1

    def runtime(self, data) :
        res_1 = self.hash_func_1(data)
        res_2 = self.hash_func_2(data)
        res_3 = self.hash_func_3(data)
        res_4 = self.hash_func_4(data)

        return self.bit_array[res_1] and self.bit_array[res_2] and self.bit_array[res_3] and self.bit_array[res_4]

class TweetStreaming(StreamListener):
    def __init__(self, keys, time_limit = 60) :
        super().__init__()

        # only stream tweet for time_limit (in seconds)
        self.start_time = time.time()
        self.limit = time_limit

        # list of tweets result of filtering
        self.filters = [] # container for result of filtering
        self.fill_filters = [] 
        self.all = []

        self.filtering = FilteringDataStream(keys)

        # file
        self.outfile = None

        # counter
        self.counter = 0 # for feedback only

    # get the data (tweet)
    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit :
            self.counter += 1
            print(self.counter)
            self.all.append(json.loads(data))

            # do filtering to key (userid)
            if (self.filtering.runtime(json.loads(data)['user']['id'])) :
                print('in')
                self.filters.append(json.loads(data))
                self.fill_filters.append(self.counter)
            return True
        else :
            # write the result of filtering to file
            self.write_file()
            return False

    def on_error(self, status):
        print("Error: ", str(status))
        # write the result of filtering to file
        self.write_file()
        return False

    def write_file(self) :
        self.outfile = open('filter.json', 'w')
        json.dump(self.filters, self.outfile, indent=4)
        self.outfile.close()

        print ("Lama waktu streaming: ", str(self.limit), " detik") 
        print ("Data stream yang didapatkan: ", str(len(self.all)), " tweets")
        print ("Data stream yang berhasil di-filter: ", str(len(self.filters)), " tweets")
        print ("Isi sampel (isi array merupakan index dari data stream)")
        for index in self.fill_filters :
            print("%03d" % index, end=" ")

if __name__ == '__main__':
    with open('listofkeys.json') as f:
        keys = json.load(f)

    # this handles Twitter authetification and the connection to Twitter Streaming API
    l = TweetStreaming(keys, 20 * 60)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # this line filter Twitter Streams to capture data by the spesific keywords
    stream.filter(track=['tech'])