arr = [12,24,56,34,64]
minimum = 0

for i in range(len(arr)):
 for j in range(i+1,len(arr)):
   if arr[j] < arr[i]:
       minimum = arr[i]
       arr[i]= arr[j]
       arr[j]= minimum
print(arr)
       
      