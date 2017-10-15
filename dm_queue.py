'''This is a basic queue using a list to store elements'''

class Queue(object):
    elements = []

    #initialize with an option to import an existing list into the elements field.
    def __init__(self, elements=None):
        self.elements = elements if elements is not None else []

    #append an element to the end of the list of elements (back of the queue)
    def append(self, element):
        self.elements.append(element)

    #pop and return the top element off of the list of elements (off top of queue)
    def pop(self):
        try:
            element = self.elements.pop(0)
            return element
        except:
            print("There are zero elements.")
            return None

    #return true if the queue is empty, false if not.
    def is_empty():
        if len(elements) > 0:
            return False
        else:
            return True