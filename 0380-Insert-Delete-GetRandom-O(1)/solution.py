import random

class RandomizedSet(object):

    def __init__(self):
        self.lst = []
        self.index_map = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if(val not in self.index_map):
            self.index_map[val] = len(self.lst) 
            self.lst.append(val)
            return True
        
        return False
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if(val in self.index_map):
            index = self.index_map[val]
            temp_val = self.lst[-1]
            self.lst[index] = temp_val
            self.index_map[temp_val] = index

            self.lst.pop()
            self.index_map.pop(val)

            return True
        
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.lst)
      
      