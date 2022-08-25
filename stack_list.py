from collections import deque

stack = deque()

# Stack 맨 끝에 Data 추가
stack.append("1")
stack.append("2")
stack.append("3")
stack.append("4")
stack.append("5")

print(stack)  # Stack 출력

# 맨 끝 Data 접근
print(stack[-1])

# 맨 끝 Data 삭제
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)  # Stack 출력
