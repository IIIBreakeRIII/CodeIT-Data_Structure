# 나누기 방법
def hash_function_remainder(key, array_size):
    """Hash Table의 Key를 나누기 방법으로 0 ~ array_size - 1 범위의 자연수로 바꿔주는 함수"""
    return key % array_size

print(hash_function_remainder(40, 200))
print(hash_function_remainder(120, 200))
print(hash_function_remainder(788, 200))
print(hash_function_remainder(2307, 200))
print("")

# 곱하기 방법
def hash_function_multiplication(key_2, array_size_2, a):
    """Hash Table의 Key를 곱셈 방법으로 0 ~ array_size_2 범위의 자연수로 바꿔주는 함수"""
    temp = a * key_2          # a와 key_2를 곱함
    temp = temp - int(temp)     # a와 key_2를 곱한 값의 소숫점 오른쪽 부분만 저장

    return int(array_size_2 * temp)     # temp와 배열 크기를 곱한 수의 자연수 부분만 리턴

print(hash_function_multiplication(40, 200, 0.61426212))
print(hash_function_multiplication(120, 200, 0.61426212))
print(hash_function_multiplication(788, 200, 0.61426212))
print(hash_function_multiplication(2307, 200, 0.61426212))