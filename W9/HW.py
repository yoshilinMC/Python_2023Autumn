class car:
    def __init__(self,name,time):
        self.name = name
        self.time = time
        self.next = None
head = car("Abby",8)
second = car("John",10)
third = car("Leo",17)
new = car("Brian",1)
head.next = second
second.next = third
third.next = new
new.next = head

def traverse(head):
    ptr = head
    while True:
        # ptr = ptr.next
        print("The name of the member is {}, the purchase time is {}.".format(ptr.name,ptr.time))
        if ptr.next == head:
            break
        ptr = ptr.next
    print("Finish traverse")

traverse(head)