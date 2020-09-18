list = [1,2,3,4,6,7]
class Node:
 def __init__(self,nodeval):
   self.nodeval = nodeval
   self.next = None

#converting list into linked list
 
for i in range(len(list)):
 newnode = Node(list[i])
 if i == 0:
   head = newnode
   prev = head
   continue
 prev.next = newnode
 prev = newnode

temp = head
while temp != None:
   print(temp.nodeval)
   temp = temp.next
print("the_end linked list created")

#adding element in middle

n, k = 4,5
temp = head
while temp != None:
 if temp.nodeval == n:
   addnode = Node(k)
   store = temp.next
   temp.next = addnode
   addnode.next = store
   break
 temp = temp.next

temp = head
while temp != None:
   print(temp.nodeval)
   temp = temp.next
print("the_end element in middle added")

#adding element in first

firstnode = Node(k)
store = head 
firstnode.next = store
head = firstnode
 
temp = head
while temp != None:
   print(temp.nodeval)
   temp = temp.next
print("the_end element at first added")

#adding element at last
temp = head
while temp != None:
   if temp.next == None:
     newnode = Node(k)
     temp.next = newnode
     newnode.next = None
     break
   temp = temp.next
   
temp = head
while temp != None:
   print(temp.nodeval)
   temp = temp.next
print("the_end element at last added")


 