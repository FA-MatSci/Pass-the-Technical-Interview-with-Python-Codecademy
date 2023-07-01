from linked_list import Node, LinkedList    #instead of writing the linked_list class, you import it
from blossom_lib import flower_definitions


class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for item in range(size)]

    def hash(self, key):   #this method returns a number that is unique to the given key
        #to get a number out of a string use the following:
        enc = key.encode()   #byte representation of a string (it goes by each letter)
        su = sum(enc)   #to get one number that is a sum of all the bytes
        return su

    def compress(self, hash_code):    #returns an array index based on the hash code above
        cal = hash_code % self.array_size
        return cal

    def assign(self, key, value):
        code = self.hash(key)
        array_index = self.compress(code)
#        self.array[array_index] = [key, value]
        payload = Node([key, value])   #key is at 0, value is at 1
        list_at_array = self.array[array_index]
        for i in list_at_array:
            if i[0] == key:   #i[0] is going to be the key
                i[1] = value
                return    #it stops, so it doesn't even reach the line below
        list_at_array.insert(payload)

    def retrieve(self, key):   #this method returns a value so we only need one parameter, which is the key
        cod = self.hash(key)
        array_index = self.compress(cod)
        list_at_index = self.array[array_index]
        for i in list_at_index:
            if i[0] == key:
                return i[1]
        return None

#        payload = self.array[array_index]
#        return payload[1]

#        if payload:     #if payload != None:
#            self.array[key, value]      #return payload[1]

#        if payload[0] == key:
#            return payload[1]

#        if payload is None or payload[0] != key:
#            return None


blossom = HashMap(len(flower_definitions))
for i in flower_definitions:
    blossom.assign(i[0], i[1])

print(blossom.retrieve('daisy'))