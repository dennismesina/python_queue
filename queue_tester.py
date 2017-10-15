'''Tester for dm_queue class Queue'''

import dm_queue

#Test case 1, new empty queue
my_queue = dm_queue.Queue()

my_queue.append("Hello")

my_queue.append("World")

print(my_queue.elements)

first_word = my_queue.pop()

print(my_queue.elements)

second_word = my_queue.pop()

print(my_queue.elements)

print(first_word, second_word)

#Test case 2, already defined list of items.
pre_defined_list = ["This", "is", "my", "predefined", "list"]

my_other_queue = dm_queue.Queue(pre_defined_list)

print(my_other_queue.elements)

my_other_queue.pop()

print(my_other_queue.elements)

my_other_queue.pop()

print(my_other_queue.elements)

my_other_queue.pop()

print(my_other_queue.elements)

my_other_queue.pop()

print(my_other_queue.elements)

my_other_queue.pop()

print(my_other_queue.elements)

my_other_queue.pop()