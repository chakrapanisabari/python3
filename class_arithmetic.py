class calculator:
    def __init__(self):
      self.n = 0

    def add(self, val):
        result = 0
        self.n = val
        print(self.n)
        result += self.n
        return result
    
    def sub(self, val):
        result = 0
        self.n = val
        print(self.n)
        result -= self.n
        return result
c1=calculator()
print(c1.add(10))
print(c1.sub(3))

