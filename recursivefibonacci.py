def fibonnaci(n):
 if n <= 1:
  return n
 else:
  return(fibonnaci(n-1)+ fibonnaci(n-2))
term = int(input("enter terms"))
for i in range(term):
 print(fibonnaci(i))
