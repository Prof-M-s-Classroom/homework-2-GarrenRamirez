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

    def print_list(self):   #Modified for Testing; Will Remove Upon Submission
       temp=self.head
       while temp is not None:
           print(temp.value)
           temp=temp.next

    def insert_at_index(self, index, value):
        new_node = Node(value)
        if index == 0:
            self.prepend(new_node)
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
        if index < 0 or index > self.length:
            print("Invalid: Index Out of Bounds")
            return False
        elif self.length == 0:
            print("Invalid: List is Emtpy")
            return False
        elif index == 0:
            self.delfirst()
        elif index == self.length:
            self.dellast()
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

# Methods Implemented; Testing Tomorrow