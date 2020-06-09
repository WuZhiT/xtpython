#class Other(object):

#    def override(self):
#        print("Other override()")
    
#    def implicit(self):
#        print("Other implicit()")

 #   def altered(self):
 #       print("Othert altered()")

#组合中，可将其它类写入另一个.py文件中
from xt44c1 import Other

class Child(object):

    def __init__(self):
        self.other = Other()
    
    def implicit(self):
        self.other.implicit()

    def override(self):
        print("Child overrife()")
    
    def altered(self):
        print("Child before  Other altered()")
        self.other.altered()
        print("Child after  Other altered()")

son = Child()

son.implicit()
son.override()
son.altered()