class Node:
    """Linked List의 Node Class"""

    def __init__(self, data):
        self.data = data    # Node가 저장하는 Data
        self.next = None    # 다음 Node에 대한 Reference

    
# Data 2, 3, 5, 7, 11을 담는 Node들 생성
head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)

# Node들을 연결
head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node

# Node 순서대로 출력
iterator = head_node

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next

