finished_classes = set()

# Data 저장
finished_classes.add("A")
finished_classes.add("B")
finished_classes.add("C")
finished_classes.add("D")
finished_classes.add("E")

print(finished_classes) # Set 출력

# 중복 Data 저장 시도
finished_classes.add("B")
finished_classes.add("C")

print(finished_classes) # Set 출력

# Data 탐색
print("P" in finished_classes)
print("B" in finished_classes)

# Data 삭제
finished_classes.remove("A")
finished_classes.remove("B")

print(finished_classes) # Set 출력