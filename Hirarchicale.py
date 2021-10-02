#Hierarchical inheritance

class Parent:
      def function1(self):
      	 print("this is first function 1")
 
class Child1(Parent):
      def function2(self):
      	print("this is second function 2") 
class Child2(Parent):
      def function3(self):
      	print("this is third function 3")
 
x = Child1()
x1 = Child2() 
x.function1()
x.function2()