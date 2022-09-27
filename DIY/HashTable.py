from operator import mod


class HashTable:
    def __init__(self, MAX):
        self.MAX = MAX
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key):
        tot = 0
        for ch in key:
            tot += ord(ch)
        return tot%50

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if not self.arr[h]:
            self.arr[h].append((key,val))
        else:
            found = False
            for index, element in enumerate(self.arr[h]):
                if element[0] == key:
                    self.arr[h][index] = (key, val)
                    found = True
                    break
            if not found:
                self.arr[h].append((key,val))


    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        found = False
        for index,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
                found = True
                break

        if not found:
            print(f"Key '{key}' not found to delete.")
            return


ht = HashTable(50)
ht['march 6'] = 234
ht['march 17'] =  456345
ht['march 17'] =  'NEW'
ht['dec 15'] = 'Raj'
print(ht.arr)
print(ht['march 6'])
del ht['march 6']
print(ht['march 6'])
del ht['march 5']
print(ht.arr)