#Single Inheritance


class Parent: 
  def func1(self): 
   print("this is function one")  
   
class Child(Parent): 
  def func2(self): 
    print("this is function two") 
y = Child() 
y.func1() 
y.func2() 