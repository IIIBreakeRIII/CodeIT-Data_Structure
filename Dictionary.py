grades = {}   # 중괄호를 사용

# Key - Value Data 삽입
grades["A"] = 80
grades["B"] = 70
grades["C"] = 90
grades["D"] = 60
grades["E"] = 66

print(grades) # Dictionary 출력

# 한 Key에 여러 Value 저장 시도
grades["B"] = 100

print(grades) # Dictionary 출력

# Key를 이용해서 Value 탐색
print(grades["A"])
print(grades["C"])

# Key를 이용한 삭제
grades.pop("A")
grades.pop("B")

print(grades) # Dictionary 출력