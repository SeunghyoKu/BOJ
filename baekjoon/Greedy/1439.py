# 뒤집기
# 그리디 알고리즘
# https://www.acmicpc.net/problem/1439

'''
다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있다. 다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다. 다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

예를 들어 S=0001100 일 때,

전체를 뒤집으면 1110011이 된다.
4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.

문자열 S가 주어졌을 때, 다솜이가 해야하는 행동의 최소 횟수를 출력하시오.
'''

s = input()
num1, num2 = 0, 0
answer = 0

for i in range(len(s)-1):
    num1, num2 = s[i], s[i+1]

    if num1 != num2:
        answer += 1

print((answer//2) if (answer%2) == 0 else (answer//2+1))

# 앞, 뒤의 숫자가 바뀔때마다 1을 증가시켜 몇 번 바뀌었는지 확인하였다.
# 짝수번 바뀔 경우, 숫자 한 묶음 당 한 번씩 바꿀 수 있기 때문에 /2한 값을 return하였다.
# 홀수번 바뀔 경우, 소숫점을 올림하여 몫에 +1한 값을 return하면 된다.


# 다른 사람의 풀이

data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

if data[0] == '1':
  count0 += 1
else:
  count1 += 1
  
for i in range(len(data) - 1):
  if data[i] != data[i + 1]:
    # 다음 수에서 1로 바뀌는 경우
    if data[i + 1] == '1':
      count0 += 1
    # 다음 수에서 0으로 바뀌는 경우
    else:
      count1 += 1
      
print(min(count0, count1))

# 0 -> 1 경우와 1 -> 0 경우를 모두 고려한 후, 더 작은 숫자를 리턴하는 방법이다.
# 숫자가 1일 경우에는 0 카운터를 +1 하고,
# 숫자가 0일 경우에는 1 카운터를 +1 하는 식의 방식이다.
# 조금 더 직관적인 방법이라 좋은 풀이 같다.
