#16진수로 입력된 정수 한 개를 8진수로 바꾸어 출력하는 프로그램을 작성해보자.

#따로 생각나는 방법이 없어서 일단 10진수로 변경후, 다시 8진수로 변경하는 방법을 사용하였다.

num = int(input(), 16)
nums = oct(num)[2:]

print(nums)

'''
다른 사람의 풀이

a=input()
n=int(a, 16)
print('%o' % n)

다음엔 꼭 이 방법으로 풀어봐야지.. 
'''
