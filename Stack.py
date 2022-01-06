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




#Clearing Stack Value.
print(My_stack.clear())
print(My_stack)


My_stack.append("2")
My_stack.append("1")
My_stack.append("3")
print(My_stack)


#Removing Stack value.....
My_stack.remove('3')
print(My_stack)

#lenght Checking
print(len(My_stack))