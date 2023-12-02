class student:
    def __init__(self,name,age):
      self.name = name
      self.age = age
      self.next = None
name = student("Amy",25)
name.next = None

def traverse(name):
    ptr = name
    while ptr != None:
        print("The employee name is {} and the age is {}".format(ptr.name,ptr.age))
        ptr = ptr.next
    print("Finish traverse")

traverse(name)