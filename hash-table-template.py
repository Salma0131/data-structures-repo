class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]

    def hash_function(self, key):
        return key % self.size
    
    def get(self, key):
        index = self.hash_function(key)
        if len(self.table[index]) != 0:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        else:
            return None

    def set(self, key, value):
        index = self.hash_function(key)
        self.table[index].append([key,value])


# Example usage
table = HashTable(5)
table.set(238, "hello")  # 238 % 5 = 3
table.set(5251, "world")  # 5251 % 5 = 1
table.set(123, "good")  # 123 % 5 = 3 (collision with 238)

# Retrieving values
print(table.get(238))   # Output: good (because 123 overwrote the value at index 3)
print(table.get(5251))  # Output: world
print(table.get(22))    # Output: None (no value at 22 % 5 = 2)

