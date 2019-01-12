class Queue:
    def __init__(self):
        self.CAPACITY = 3
        self.arr = [None] * self.CAPACITY
        self.front = 0 ## don't really need 'front' variable. can use back - size
        self.back = 0
        self.size = 0
    def enqueue(self,student): #back to right
        if student == None:
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
        return returned
    def peek(self):
        if self.size == 0:
            return "Queue is empty!"
        return self.arr[self.front]
    def size(self):
        return self.size
    def clear(self):
        self.arr = [None] * self.CAPACITY
        self.front = 0
        self.back = 0
        self.size = 0
    def isEmpty(self):
        return size == 0
    def __repr__(self):
        return str(self.arr)
