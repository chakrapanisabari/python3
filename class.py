class first:
    def __init__(self):
        self.stack=[]
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        value=self.stack[-1]
        del self.stack[-1]
        return value

ob1=first()
ob1.push(1)
ob1.push(2)
print(ob1.pop())

