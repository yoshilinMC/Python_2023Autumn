# class car:
#     def __init__(self,color):
#         self.color = color
#         self.next = None
# head = car("red")
# blue = car("blue")
# head.next = blue
# blue.next = head

# def traverse(head):
#     ptr = head
#     while True:
#         print("The color of the car is {}".format(ptr.color))
#         ptr = ptr.next
#         if ptr == head:
#             break
#     print("Finish traverse")

# traverse(head)

class car:
    def __init__(self,color):
        self.color = color
        self.next = None
head = car("red")
blue = car("blue")
new = car("black")
head.next = blue
blue.next = new
new.next = head

def traverse(head):
    ptr = head
    while True:
        # ptr = ptr.next
        print("The color of the car is {}".format(ptr.color))
        if ptr.next == head:
            break
        ptr = ptr.next
    print("Finish traverse")

traverse(head)