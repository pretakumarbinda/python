class Data:
    def __init__(self, limit):
        self.limit = limit
        
    def __iter__(self):
        self.value = 10
        return self
    
    def __next__(self):
        x = self.value
        if x>self.limit:
            raise StopIteration
        else:
            self.value = x+1
            return x

for i in Data(15):
    print(i)