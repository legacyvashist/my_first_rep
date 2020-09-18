class Node :
 def __init__(self, nodeval):
   self.nodeval = nodeval
   self.next = None
linkedlist = Node(5)
newnode = Node(6)
linkedlist.next = newnode
newnode2 = Node(7)
newnode.next = newnode2
print(newnode.next.nodeval)
print(newnode2.nodeval)
print(linkedlist.next.nodeval)
 
 