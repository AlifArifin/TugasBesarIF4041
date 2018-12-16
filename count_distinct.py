import json

def hash(key):
    result = key % 513
    return result

def trailing(binkey):
    
    idx = len(binkey) - 1
    count = 0

    while (idx > 0):
        
        if (binkey[idx]=='0'):
            count = count + 1
        
        idx = idx - 1

    return count

file = open("streaming", "r")

maks = -1
num_items = 200
counter = 0

for line in file:
    #print(line)
    if (line != '\n'):

        counter = counter + 1
        if (counter > num_items):
            break
        obj = json.loads(line)
        id_stream = obj["id"]
        hashed_value = hash(id_stream)
        trailing_zeroes = trailing("{0:b}".format(hashed_value))
        #print("id: "+str(obj["id"]))
        #print("hash: "+str(hash(obj["id"])))
        #print("biner: "+"{0:b}".format(hashed_value))
        #print("jumlah trailing zeroes: "+str(trailing_zeroes))
        maks = max(maks, 1 << trailing_zeroes)

file.close()

print("Streaming 200 twitter")
print("Jumlah elemen yang berbeda: ", maks)