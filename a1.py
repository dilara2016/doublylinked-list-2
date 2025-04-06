class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def searching(self,data):
        t = 0
        temp = self.head

        while temp:
            if temp.data == data:
                t = 1;
                break;
            temp = temp.next
        if t==1:
            print("! Element has been found !")
        else:
            print("! Element has NOT been found !")


    def insertion(self, data):
        Nnode = Node(data)
        if self.head is None:
            self.head = Nnode
            print(f"! Successfully inserted {data} as head !")
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Nnode
            Nnode.prev = temp
            print(f"! Successfully inserted {data} at end  !")



    def display(self):
        if self.head == None:
            print("! List Is Empty !")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end = " ")
                temp = temp.next



l = DoublyLL()
l.insertion(10)
l.insertion(20)
l.insertion(30)
l.searching(20)
l.searching(50)
l.display()
print(end='\n')
