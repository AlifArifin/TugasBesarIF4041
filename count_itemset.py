import json
import math

file = open("streaming", "r")

def map_index(index):

    return math.log(index) / math.log(2)

num_items = 500
counter = 0
count_ruby = 0
count_javascript = 0
count_python = 0
counter = 0
window_size = 50
keyword = 'ruby'
timestamp = 1
count_keyword = 0
bucket_list = []
count_list = []
first_index = 0

def merge_bucket(bucket):

    goon = True
    index = 0

    while (goon):
        first = bucket[index][1]
        temp = max(first_index, index+1)
        #first_index = temp
        #first_index = max(first_index,index+1)
        bucket[index+1].append(first)
        bucket[index].pop(0)
        bucket[index].pop(0)
        count_list[index] = count_list[index] - 2
        count_list[index+1] = count_list[index+1] + 1
        
        if (count_list[index+1] > 2):
            index = index + 1
        else:
            goon = False

    return max(first_index, index+1)

for i in range(0, 20):
    count_list.append(0)
    bucket_list.append([])

first = True

for line in file:
    #print(line)
    if (line != '\n'):
        
        counter = counter + 1
        if (counter > num_items):
            break
        
        obj = json.loads(line)
        teks = obj["text"].lower()

        #print("bucket sebelum")
        #print(bucket_list)

        #print("timestamp: "+str(timestamp))
        if (len(bucket_list[0])!=0 and timestamp - bucket_list[first_index][0] >= window_size):
                #print("fi "+str(first_index))
                bucket_list[first_index].pop(0)
                count_list[first_index] = count_list[first_index] - 1
                if (len(bucket_list[first_index])==0 and first_index > 0):
                    first_index = first_index - 1 

        if (keyword in teks):
            count_keyword = count_keyword + 1
            bucket_list[0].append(timestamp)
            count_list[0] = count_list[0] + 1

            #print("timestamp: "+str(timestamp))
            #print("first index: "+str(first_index))

            #print("cl "+str(count_list[0]))

            if (count_list[0] > 2):
                #print("cl "+str(count_list[0]))
                first_index = merge_bucket(bucket_list)

        timestamp = timestamp + 1
        #print("bucket sesudah")
        #print(bucket_list)
        
        #print("=======")

file.close()

#print(bucket_list)
sum = 0
for idx in range(0, first_index+1):
    if (idx == first_index):
        temp = len(bucket_list[idx])  
        if (temp == 1):
            sum = sum + 1*(1<<idx)
        else:
            sum = sum + (temp/2)*(1<<idx)
    else:
        sum = sum + len(bucket_list[idx])*(1<<idx)

print("Streaming tweet: ",num_items," buah")
print("Jumlah tweet dengan kata kunci \'Ruby\' dalam ",window_size, "terakhir streaming tweet adalah: ", int(sum))