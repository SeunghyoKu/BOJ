#입력 된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.

#xor = ^
#xor 은 뭘까? 둘 다 값이 다를 경우 1을 반환
a, b = input().split(" ")
a = int(a)
b = int(b)
print(a^b)
