from Queue import Queue
from Student import Student
class Driver:
    def __init__(self):
        self.q = Queue()
    def add(self,student):
        value = self.q.enqueue(student)
        if value == None:
            handle = open("studentLog.csv", "a")
            handle.write("{},{},{},{},{}\n".format(student.getName(), student.getTime()[0],
                                                   student.getTime()[1]
                                                   , student.getTime()[2]
                                                   , student.getTime()[3]))
            handle.close()
        else:
            return value
    def remove(self): ##add boolean to see if they were present when called?
        value = self.q.dequeue()
        return value
    def queue(self):
        return self.q
