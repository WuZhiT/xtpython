class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):

    def implicit(self):
        print("Child  Before implicit()")
        super(Child,self).implicit()
        print("Child After implicit()")
    

dad = Parent()
son = Child()

dad.implicit()
son.implicit()