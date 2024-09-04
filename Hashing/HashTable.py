class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_Hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        i = self.get_Hash(key)
        self.arr[i] = value

    def __getitem__(self, key):
        i = self.get_Hash(key)
        return self.arr[i]

    def __delitem__(self, key):
        i = self.get_Hash(key)
        self.arr[i] = None


h = HashTable()
print(h.get_Hash("march 6"))

# Adding Element
h['march 6'] = 320
h['march 22'] = 290

# Retriving Element
print(h['march 6'])