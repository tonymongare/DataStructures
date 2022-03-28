class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
	def AtEnd(self,newdata):
		newnode = Node(newdata)
		if self.head is None:
			self.head = newnode
			return
		last = self.head
		while(last.next):
			last = last.next
		last.next = newnode

	def printlist(self):
		listitems = self.head
		if listitems is not None:
			print(listitems.data)
			listitems = listitems.next
linked_list = LinkedList()

linked_list.head = Node("NIC")
second = Node("StandardChartered")
third = Node("Family Bank")	
fourth = Node("NIC bank")

linked_list.head.next = second
second.next = third
third.next =fourth

linked_list.AtEnd("JPMorgan")

linked_list.printlist()

	

		

		
