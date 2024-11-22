from collections import deque
stack = deque([])

stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
stack.append('e')

print('Initial stack:')
print(stack)
print('\nElements popped from stack:')
print(stack.popleft())


print('\nStack after elements are popped:')
print(stack)

