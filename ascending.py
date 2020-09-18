sample = [9,5,7,4,3,2,1]
for i in range(0,len(sample)):
 for j in range(i+1, len(sample)):
   if sample[i]>sample[j]:
    catcher = 0
    catcher = sample[i]
    sample[i]= sample[j]
    sample[j] = catcher
print(sample)

   