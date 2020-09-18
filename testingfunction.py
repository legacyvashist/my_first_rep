def testing(x):
 print(f"testing is {x}")

testing("successfull")
testing("failed")



def loop_test(y):
 i = 0
 while i != y+1:
   print(f"the loop will run {y} times")
   print(f"the loop count is {i}")
   i = i + 1

loop_test(9)
loop_test(5)