from os import link
from linked_list import Node

class LinkedList:
    """Linked List Class"""
    def __init__(self):
        self.head = None    # Linked List의 가장 앞 Node
        self.tail = None    # Linked List의 가장 뒤 Node

    def insert_after(self, previous_node, data):
        """Linked List 주어진 Node 뒤 삽입 연산 Method"""
        new_node = Node(data)

        # 가장 마지막 순서 삽입
        if previous_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        # 두 Node 사이에 삽입
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node

    def find_node_at(self, index):  # Linked List의 원하는 Index 찾기
        """Linked List 접근 연산 Method, Prameter Index는 항상 있다고 가정"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def append(self, data):
        """Linked List 추가 연산 Method"""
        new_node = Node(data)

        # Linked List가 비어있으면 새로운 Node가 Linked List의 처음이자 마지막 Node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # Linked List가 비어있지 않을 경우
        else:
            self.tail.next = new_node   # 가장 마지막 Node 뒤에 새로운 Node 추가
            self.tail = new_node        # 마지막 Node를 추가한 Node로 바꿔줌

    def __str__(self):
        """Linked List를 문자열로 표현해서 Return하는 Method"""
        res_str = "|"

        # Linked List 안에 모든 Node를 돌기 위한 변수, 일단 가장 앞 Node로 정의
        iterator = self.head

        # Linked List 끝까지 반복
        while iterator is not None:
            # 각 Node의 Data를 Return하는 문자열에 더해줌
            res_str += f" {iterator.data} |"
            iterator = iterator.next    # 다음 Node로 넘어감

        return res_str

# 새로운 Linked List 생성
linked_list = LinkedList()

# Linked List에 Data 추가
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(11)

# Linked List Node에 접근 (Data 가지고 오기)
print(linked_list.find_node_at(3).data)

# Linked List Node에 접근 (Data 변경)
linked_list.find_node_at(2).data = 13

print(linked_list)

node_2 = linked_list.find_node_at(2)    # Index 2에 있는 Node 접근
linked_list.insert_after(node_2, 6)     # Index 2 뒤에 6 삽입

print("Insert After Index 2")
print(linked_list)