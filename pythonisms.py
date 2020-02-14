class Pythonisms:
    def __init__(self, max=50):
        self.length = max
        self._hash_table = [None]*self.length


    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.length):
            raise StopIteration
        self.num += 1
        return self.num

    def time_function(fun):
        start = time.time()
        ret = fun()
        elapsed = time.time() - start
        return ret, elapsed

    def add(self, key, value=None):
        hsh = self._hash(key)
        if not self._hash_table[hsh]:
            self._hash_table[hsh] = []
        self._hash_table[hsh].append([key, value])

    
    def get(self, key):
        hashed_key = self._hash(key)
        key_index = self._hash_table[hashed_key]
        if key_index:
            for i in range(len(key_index)):
                if key == key_index[i][0]:
                    return key_index[i][1]
        return None

    def contains(self, key):
        hashed_key = self._hash(key)
        key_index = self._hash_table[hashed_key]       
        if key_index:
            if key == key_index[0][0]:
                return True
        return False
        

    def get_length(self):
        return self.length