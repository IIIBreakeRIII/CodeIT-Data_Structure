class Node:
    """Linked List의 Node Class"""

    def __init__(self, data):
        self.data = data    # Node가 저장하는 Data
        self.next = None    # 다음 Node에 대한 Reference

class DoubleLinkedList:
    """Double Linked List Class"""
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Double Linked List 추가 연산 Method"""
        new_node = Node(data) # 새로운 Data를 저장하는 Node
        
        # Double Linked List가 비어 있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: # Double Linked List에 Data가 이미 있는 경우
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def append(self, data):
        """Double Linked List 추가 연산 Method"""
        new_node = Node(data)   # 새로운 Data를 저장하는 Node
        
        # Double Linked List가 비어 있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:   # Double Linked List 안에 Data가 이미 있는 경우
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

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

# 빈 Double Linked List wjddml
my_list = DoubleLinkedList()

# Double Linked List에 Data 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

# 빈 Double Linked List 정의
my_list = DoubleLinkedList()

# Double Linked List에 Data 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)