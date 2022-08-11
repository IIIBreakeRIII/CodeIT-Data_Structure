# Python List 생성
trending = []

# 특정 위치에 Data 삽입
trending.insert(0, "AAA")
trending.insert(1, "BBB")
trending.insert(2, "CCC")
trending.insert(3, "DDD")

print(trending)

# 괄호를 이용한 Index 접근
print(trending[0])
print(trending[1])

trending[2] = 4             # Data 변경

print(trending)

# in 을 이용한 탐색
print("AAA" in trending)    # Return True
print("ZZZ" in trending)    # Return False

# del을 이용한 삭제
del trending[0]

print(trending)