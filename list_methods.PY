ten_things = "apples oranges crow telephone light sugar"
stuff = ten_things.split(' ')
print("wait there are not ten items in ten_things")

more_stuff = ["table", "spoon", "fan", "glass", "computer", "sofa", "mirror", "door"]
while(len(stuff) != 10):
	storage =  more_stuff.pop()
	stuff.append(storage)
	print(stuff)
	print(len(stuff))

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
