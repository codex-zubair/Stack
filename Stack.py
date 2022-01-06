from collections import deque
from os import X_OK


My_stack = deque()



#Implementing Data Into My Stack


My_stack.append('one')
My_stack.append('Two')
My_stack.append('Three')

#This Code for Right Side adding file from and Removing File.

print(My_stack)

My_stack.pop()
print(My_stack)

#################################################################

My_stack.append('Enter')

print(My_stack)
##########################################################



#This Code for left Side adding File.... and Removing File.

My_stack.popleft()
print(My_stack)


My_stack.appendleft("Left Data Entry")
print(My_stack)

