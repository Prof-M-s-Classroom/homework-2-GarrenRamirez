from Spaceship import Spaceship

class Node:
    def __init__(self, value):
        self.value = value
        self.next=None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self,value):
       new_node = Node(value)
       self.head = new_node
       self.tail = new_node
       self.length = 1

    def __str__(self):
        return str(self.head)

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def delfirst(self):
       if self.length == 0:
           return None
       temp=self.head
       self.head=self.head.next
       temp.next=None
       self.length -= 1
       if self.length == 0:
           self.tail=None
       return temp

    def dellast(self):
        if self.length == 0:
            return None
        temp=self.head
        pre=self.head
        while temp.next:
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length -= 1
        if self.length == 0:
            self.head=None
            self.tail=None
        return temp

    def print_list(self):
       temp=self.head
       while temp is not None:
           print(temp.value)
           temp=temp.next

    def insert_at_index(self, index, value):
        new_node = Node(value)
        if index == 0:
            return self.prepend(new_node)
        elif index == self.length:
            return self.append(new_node)
        elif index > self.length or index < 0:
            print("Invalid: Index Out of Bounds!")
            return False
        else:
            temp = self.head
            temp_index = 0
            while temp_index != index - 1:
                temp = temp.next
                temp_index += 1
            if temp_index + 1 == self.length:
                self.append(new_node)
            else:
                temp_following_node = temp.next
                temp.next = new_node
                new_node.next = temp_following_node
            self.length += 1
        return True

    def delete_at_index(self, index):
        if index == 0:
            return self.delfirst()
        elif index == self.length - 1:
            return self.dellast()
        elif self.length == 0:
            print("Invalid: List is Emtpy")
            return False
        elif index < 0 or index >= self.length:
            print("Invalid: Index Out of Bounds")
            return False
        else:
            temp = self.head
            temp_index = 0
            while temp_index != index - 1:
                temp = temp.next
                temp_index += 1
            temp.next = temp.next.next
            self.length -= 1
        return True

#TODO : Write function insertatindex to insert a newnode at any given index. Consider all edge cases, including missing nodes.
#TODO : Write fucntion deleteatindex to delete a newnode at any given index. COnsider all edge cases, including missing nodes.
# Make sure to reuse existing function for the correct edge cases for both TODOs
# Write appropriate test function below to test for the new functions.

s1 = Spaceship("Voyager",100)
s2 = Spaceship("Enterprise",200)
s3 = Spaceship("Atlantis",300)
s4 = Spaceship("Challenger",400)
s5 = Spaceship("Artemis",500)
s6 = Spaceship("Pathfinder", 600)

def test_linked_list():
    ll = LinkedList(10)
    ll.append(20)
    ll.append(30)

    print("Initial list:")
    ll.print_list() #expecting 10, 20, 30

    # Testing insert_at_index
    print("\nInserting 15 at index 1:")
    ll.insert_at_index(1, 15)
    ll.print_list() #expecting 10, 15, 20, 30

    print("\nInserting 5 at index 0:")
    ll.insert_at_index(0, 5)
    ll.print_list() #expecting 5, 10, 15, 20, 30

    print("\nInserting 35 at index 5 (end of list):")
    ll.insert_at_index(5, 35)
    ll.print_list() #expecting 5, 10, 15, 20, 30, 35

    print("\nTrying to insert at out-of-bounds index 10:")
    ll.insert_at_index(10, 50)  #expecting Invalid

    # Testing delete_at_index
    print("\nDeleting element at index 2:")
    ll.delete_at_index(2)
    ll.print_list() #expecting 5, 10, 20, 30, 35

    print("\nDeleting first element (index 0):")
    ll.delete_at_index(0)
    ll.print_list() #expecting 10, 20, 30, 35

    print("\nDeleting last element (index 3):")
    ll.delete_at_index(3)
    ll.print_list() #expecting 10, 20, 30

    print("\nTrying to delete at out-of-bounds index 10:")
    ll.delete_at_index(10)  #expecting Invalid

    print("\nTesting Node Linked List! ")
    print("\n")
    test = LinkedList(s2)
    test.append(s3)
    test.prepend(s1)
    test.print_list()   #expecting s1, s2, s3
    print("\n")
    test.insert_at_index(0, s4)
    test.print_list()   #expecting s4, s1, s2, s3
    print("\n")
    test.insert_at_index(5, s6) #expecting Invalid
    test.insert_at_index(4, s6)
    print("\n")
    test.print_list()   #expecting s4, s1, s2, s3, s6
    print("\n")
    test.dellast()
    test.delfirst()
    test.print_list()   #expecting s1, s2, s3
    print("\n")
    test.delete_at_index(6) #expecting Invalid
    test.delete_at_index(2)
    print("\n")
    test.print_list()   #expecting s1, s2

    print("\nTesting Node Linked List Done!")
test_linked_list()