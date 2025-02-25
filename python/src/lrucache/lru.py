class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.lru = {}

    def refer(self, key):
         # not present in cache
        if key not in self.lru:
            if len(self.cache) == self.capacity:
                last = self.cache.pop(key)
                del self.lru[key]
         # present in cache
        else:
            self.cache.remove(key)

        # update reference
        self.cache.append(key)
        self.lru[key] = True

    def display(self):
        for i in self.cache:
            print(i,end=' ')
        print('')
