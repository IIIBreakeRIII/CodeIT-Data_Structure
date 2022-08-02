# 정수 값
print("hash(12345)")
print(hash(12345))  # 12345
print(hash(12345))  # 12345

# 다른 정수 값
print("hash(12346)")
print(hash(12346))  # 12346

# 소수 값
print("hash(15.1234)")
print(hash(15.1234))  # 284541027336970255
print(hash(15.1234))  # 284541027336970255

# 다른 소수 값
print("hash(81.1234)")
print(hash(81.1234))  # 284541027336978513

# 문자열
print("hash(파이썬)")
print(hash("파이썬"))  # -8002119629611903017
print(hash("파이썬"))  # -8002119629611903017

# 다른 문자열
print("hash(자바)")
print(hash("자바"))  # -8553573703343279427

# Hash 함수에 서로 다른 두 값을 Parameter로 넣었을 때 같은 정수가 Return 될 수 없음
# 데이터를 자신만의 고유한 정수 값으로 바꿔줌

# Hash 함수의 한계
# Python Hash 함수의 경우 언어 자체적으로는 불변 타입(Boolean, 정수형, 소수형, Tuple, 문자열) 자료형에만 사용 가능