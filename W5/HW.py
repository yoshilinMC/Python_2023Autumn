class car:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.next = name
        self.next = age
        self.next = name
        self.next = age
        self.next = None
head = car("Amy",25)
head.next = car("Eddy",43)
head.next.next = car("Esme",32)

def traverse(head):
    ptr = head
    while ptr != None:
        print("The employee name is is {} and the age is {}".format(ptr.name,ptr.age))
        ptr = ptr.next
    print("Finish traverse")

traverse(head)