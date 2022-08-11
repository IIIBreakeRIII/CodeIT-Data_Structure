# deque는 Python Collections Module에서 가지고 온다
from collections import deque

queue = deque()

# Queue의 맨 끝에 Data 삽입
queue.append("AAA")
queue.append("BBB")
queue.append("CCC")
queue.append("DDD")
queue.append("EEE")

print(queue)  # Queue 출력

# Queue의 가장 앞 Data에 접근
print(queue[0])

# Queue 맨 앞 Data 삭제
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print(queue)