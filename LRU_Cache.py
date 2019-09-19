
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        """ Initialize class variables """
        self.capacity = capacity
        self.hashtable = {}   # Hashtable is a dictionary with the pair key, node(key, value)
        self.head = None
        self.tail = None

    def get(self, key):
        """" Retrieve item from provided key. Return -1 if nonexistent """
        if key in self.hashtable:
            node = self.hashtable[key]
            self.remove(key)
            self.add(key, node.value)
            return node.value
        else:
            return -1

    def set(self, key, value):
        """ Set the value if the key is not present in the cache.
        If the cache is at capacity remove the oldest item."""
        if self.capacity == 0:
            print("Can't perform operations on 0 capacity cache")
        else:
            if key not in self.hashtable:
                if len(self.hashtable) == self.capacity:
                    self.remove(self.tail.key)
                self.add(key, value)
            else:
                self.hashtable[key].value = value

    def add(self, key, value):
        node = Node(key, value)
        if self.head is None:
            self.head = node
            self.tail = self.head
            self.tail.prev = self.head
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.hashtable[key] = node

    def remove(self, key):
        node = self.hashtable[key]
        if key == self.tail.key:
            self.tail = self.tail.prev
        node.prev.next = node.next
        node.next.pre = node.prev
        del self.hashtable[key]


# =========== Test case #1 ===============
print("\n===========Test case #1=============")
our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))     # returns 1
print(our_cache.get(2))     # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))     # returns - 1 because the cache reached it capacity


# ============ Test case #2 ==================
# Try to update a value for existing key and check whether it's reflecting properly or not.
print("\n=========Test case #2==========")
our_cache = LRUCache(2)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
print(our_cache.get(1))     # should return 10
print(our_cache.get(2))     # should return 2


# ============ Test case #2 ==================
# Try to create a cache with zero/null/empty capacity and perform set() and get() operation.
print("\n===========Test case #3=============")
our_cache = LRUCache(0)
our_cache.set(1, 1)         # should print some warning message like "Can't perform operations on 0 capacity cache"
print(our_cache.get(1))     # should return -1
