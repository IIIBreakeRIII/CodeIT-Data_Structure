class Node:
    """Linked List의 Node Class"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None    # 다음 Node에 대한 Reference
        self.prev = None    # 전 Node에 대한 Reference

class LinkedList:
    """Linked List Class"""
    def __init__(self):
        self.head = None    # Linked List의 가장 앞 Node
        self.tail = None    # Linked List의 가장 뒤 Node

    def find_node_with_key(self, key):
        """Linked List에서 주어진 Data를 갖고있는 Node를 Return 단, 해당 Node 가 없으면 None을 Return"""
        iterator = self.head    # Linked List를 돌기 위해 필요한 Node 변수

        while iterator is not None:
            if iterator.key == key:
                return iterator

            iterator = iterator.next

        return None
        
    def append(self, key, value):
        """Linked List 추가 연산 Method"""
        new_node = Node(key, value)

        # 빈 Linked List라면 Head와 Tail을 새로 만든 Node로 지정
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:       # 이미 Node가 있으면
            self.tail.next = new_node       # Tail의 다음 Node로 추가
            new_node.prev = self.tail
            self.tail = new_node            # Tail Update

    def delete(self, node_to_delete):
        """Double Linked List 삭제 연산 Method"""

        # Linked List에서 마지막 남은 Data를 삭제할 때
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.tail = None
            self.head = None
        # Linked List 가장 앞 Data 삭제할 때
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None
        # Linked List 가장 뒤 Data 삭제할 때
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:       # 두 Node 사이에 있는 Data 삭제할 때
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

    def __str__(self):
        """Linked List를 문자열로 표현해서 Return하는 Method"""
        res_str = ""

        # Linked List 안에 있는 모든 Node를 돌기 위한 변수, 일단 가장 앞 Node로 정의
        iterator = self.head

        # Linked List 끝까지 돎
        while iterator is not None:
            # 각 Node의 Data를 Return하는 문자열에 더해짐
            res_str += "{}: {}\n".format(iterator.key, iterator.value)
            iterator = iterator.next    # 다음 Node로 넘어감
        
        return res_str

# 새로운 Linked List 생성
my_list = LinkedList()

# 새로운 Node 3개 추가
my_list.append(key=101, value="A")
my_list.append(key=201, value="B")
my_list.append(key=301, value="C")

# Linked List 출력
iterator = my_list.head

while iterator is not None:
    print(iterator.key, ":" ,iterator.value)
    iterator = iterator.next