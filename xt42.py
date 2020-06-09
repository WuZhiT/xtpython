##Animal is-a object(yes,sort of confusing) look at the extra credit(附加练习)
class Animal(object):
    pass

## 创建一个Dog类，继承自Animal
class Dog(Animal):

    def __init__(self,name):
        ## 从self获取name属性，并设它为name
        self.name = name

## 创建一个Cat类，继承自Animal
class Cat(Animal):

    def __init__(self,name):
        ## 从self获取name属性，并设它为name
        self.name = name

##创建一个Person类，带有self和name参数的__init__函数
class Person(object):
    
    def __init__(self,name):
        ## 从self获取name属性，并设它为name
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None

##创建一个Employee类。继承自Person
class Employee(Person):

    def __init__(self,name,magic):
        ##调用父类Employee中Init函数  hmm what is this strange magic？
        super(Employee,self).__init__(name)
        #super() 函数是用于调用父类(超类)的一个方法。
        #super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
        #MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
        ##从self获取salary属性，并设它为salary
        self.salary = salary

##创建一个Fish类
class Fish(object):
    pass

##创建一个Salmon类，继承自类Fish
class Salmon(Fish):
    pass

##创建一个类Halibat，继承自Fish类
class Halibut(Fish):
    pass


##rover is-a Dog
rover = Dog("Rover")

##satan为DOg一个实例
satan = Cat("Satan")

##mary为Person一个实例
mary = Person("Mary")

##frank为Employee一个实例
frank = Employee("Frank",120000)

##从frank获取pet属性，并设为rover
frank.pet = rover

##flipper为Fish类一个实例
flipper = Fish()

##设crouse为salmon一个实例
crouse = Salmon()

##设harry为Halibut类一个实例
harry = Halibut()