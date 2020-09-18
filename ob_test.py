
class Addition:
 first = 0
 second = 0
 ans = 0
 def __init__(self,f,s):
   self.first = f
   self.second = s
 def display(self):
   print("first number = " + str(self.first))
   print("second number = " + str(self.second))
   print("answer is =" + str(self.ans))
 
 def answer(self):
   self.ans = self.first + self.second
   print(self.ans)

test_ob = Addition(10,20)

test_ob.answer() 
test_ob.display()
