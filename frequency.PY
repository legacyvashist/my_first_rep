input_string = input("type something>")
frequency = {} 
  
for i in input_string: 
   if i in frequency: 
      frequency[i] = frequency[i] + 1
   else: 
      frequency[i] = 1
print(frequency)

frequency2 = {}
sample = input_string.split()
for i in sample:
   if i in frequency2:
      frequency2[i]= frequency2[i] + 1 
   else:
      frequency2[i] = 1
print(frequency2) 

