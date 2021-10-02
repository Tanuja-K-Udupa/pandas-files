#Multiple Inheritance
class Parent1:
    def function1(self): 
      print("this is first function 1")
class Parent2: 
     def function2(self): 
       print("this is second function 2") 
class Parent3:
     def function3(self): 
       print("this is third function 3")
class Child(Parent1, Parent2, Parent3):
    def function4(self):
       print("this is fourth function 4")

inherit = Child()
inherit.function1()
inherit.function2()
inherit.function3()
inherit.function4() 