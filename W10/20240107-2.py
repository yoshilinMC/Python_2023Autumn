# class car:
#     def __init__(self,color):
#         self.color = color
#         self.next = None
# head = car("black")
# red = car("red")
# pink = car("pink")
# new = car("blue")
# head.next = red
# red.next = pink
# pink.next = new
# new.next = red
# red.next = new
# new.next = red

# def traverse(head):
#     ptr = head
#     while True:
#         # ptr = ptr.next
#         print("The color of the car is {}".format(ptr.color))
#         if ptr.next == head:
#             break
#         ptr = ptr.next
#     print("Finish traverse")

# traverse(red)

class car:
    def __init__(self,color):
        self.color = color
        self.previous = None
        self.next = None