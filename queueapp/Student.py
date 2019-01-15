from time import localtime
class Student:
    def __init__(self,name,reason):
        self.name = name.strip()
        self.time = localtime()
        self.reason = reason
    def getName(self):
        return self.name
    def getExtendedTime(self):
        return self.time
    def getTime(self):
        return (self.time.tm_hour, self.time.tm_min, self.time.tm_sec, self.time.tm_wday)
    def __repr__(self):
        return "{}:{}({}:{}:{})".format(self.name,self.reason, self.getTime()[0], self.getTime()[1], self.getTime()[2])

