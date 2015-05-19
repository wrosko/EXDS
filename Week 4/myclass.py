class MyClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mult(self):
        return self.x*self.y
    
class MyClass2(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def mult(self):
        return self.x*self.y*self.z
