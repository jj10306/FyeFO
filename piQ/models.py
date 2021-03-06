from datetime import datetime

class Queue:
    def __init__(self):
        self.CAPACITY = 100
        self.arr = [None] * self.CAPACITY
        self.front = 0 ## don't really need 'front' variable. can use back - size
        self.back = 0
        self.size = 0
        self.tas = []
        self.totalWait = 0
        self.totalHelped = 0
    def enqueue(self,student): #back to right
        if student[0] == None:
            return "Student cannot be None!"
        if self.size == len(self.arr):
            return "Queue is full :("
        else:
            self.arr[self.back] = student
            self.back = (self.back + 1) % len(self.arr)
            self.size += 1
    def dequeue(self): #front to the right
        if self.size == 0:
            return "Queue is empty!"
        returned = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % len(self.arr)
        self.size -= 1
        self.totalHelped += 1
        self.totalWait += round((datetime.now() - returned[1]).seconds/60,2)
    def addTa(self,ta):
        if ta not in self.tas:
            self.tas.append(ta)
    def removeTa(self,ta):
        if ta in self.tas:
            self.tas.remove(ta)
    def peek(self):
        if self.size == 0:
            return "Queue is empty!"
        return self.arr[self.front]
    def size(self):
        return self.size
    def clear(self):
        self.arr = [None] * self.CAPACITY
        self.front = 0 ## don't really need 'front' variable. can use back - size
        self.back = 0
        self.size = 0
        self.tas = []
        self.totalWait = 0
        self.totalHelped = 0
    def isEmpty(self):
        return self.size == 0
    def contains(self, name):
        for i in range(self.front, self.back):
            if name == self.arr[i][0]:
                return True
        return False
    def __repr__(self):
        temp = []
        index = self.front
        for i in range(self.size):
            temp.append(self.arr[index][0])
            index  = (index + 1) % len(self.arr)
        return temp
