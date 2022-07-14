from hashlib import new

class Node:
    """Linked List의 Node Class"""

    def __init__(self, data):
        self.data = data    # Node가 저장하는 Data
        self.next = None    # 다음 Node에 대한 Reference

class LinkedList:
    """Linked List Class"""
    
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Linked List 추가 연산 Method"""

        new_node = Node(data)

        if self.head is None:           # Linked List가 비어있을 경우
            self.head = new_node
            self.tail = new_node
        else:                           # Linked List가 비어있지 않을 경우
            self.tail.next = new_node
            self.tail = new_node

# 새로운 Linked List 생성
my_list = LinkedList()

# Linked List에 Data 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

# Linked List 출력
iterator = my_list.head

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next