stack = []
print(type(stack))

print(f" Initial stack: {stack}")

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

print(f"  After pushing : {stack}")

popped = stack.pop()
print(f"  Popped item: {popped}")
print(f"  Stack after pop: {stack}")

if stack:
    print(f" Top of stack: {stack[-1]}")
else:
    print(f" Stack is empty")


