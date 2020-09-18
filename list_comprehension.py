even = [num for num in range(100) if num % 2 == 0 ]
print(even)

odd = [i for i in range(100) if i % 2 != 0]
print(odd)

even_odd = [("even",i) if i%2 == 0 else ("odd",i) for i in range(20)]
print(even_odd)