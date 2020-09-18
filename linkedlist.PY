class Node:
	def __init__(self, val=0, next=None):
        	self.val = val
        	self.next = next

n1 = Node(5)
n2 = Node(66)
n3 = Node(77)
n4 = Node(99)
n5 = Node(44)
n6 = Node(14)
n7 = Node(105)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
temp = head = n1
def max_returner(head):
        temp = head
        if temp.next == None:
                x = temp
                head = None
                return head, x
        if (temp.next.next == None) and (temp.val > temp.next.val):
                x = temp
                head = temp.next
                temp.next = None
                return head, x
        elif temp.next.next == None and temp.val < temp.next.val:
                x = temp.next
                head = temp
                temp.next = None
                return head, x
        max = 0
        prev = p_max = None
        while(temp!= None):
                if temp.val > max:
                        max = temp.val
                        x = temp
                        p_max = prev
                prev = temp
                temp = temp.next
        p_max.next = x.next
        x.next = None
        return head, x
head, x = max_returner(head)
print(x.val)
head, x = max_returner(head)
print(x.val)
head, x = max_returner(head)
print(x.val)
head, x = max_returner(head)
print(x.val)
head, x = max_returner(head)
print(x.val)
head, x = max_returner(head)
print(x.val)
head, x = max_returner(head)
print(x.val)



    
        

 
 
