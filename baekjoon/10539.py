# 백준 10539번 - 수빈이와 수열
# https://www.acmicpc.net/problem/10539

'''
수빈이는 심심해서 수열을 가지고 놀고 있다. 먼저, 정수 수열 A를 쓴다. 그리고 그 아래에 정수 수열 A의 해당 항까지의 평균값을 그 항으로 하는 정수 수열 B를 쓴다. 

예를 들어, 수열 A가 1, 3, 2, 6, 8이라면, 수열 B는 1/1, (1+3)/2, (1+3+2)/3, (1+3+2+6)/4, (1+3+2+6+8)/5, 즉, 1, 2, 2, 3, 4가 된다. 

수열 B가 주어질 때, 수빈이의 규칙에 따른 수열 A는 뭘까?
'''
# map()을 이용해서 input()을 받아준 후 다시 list함수로 리스트로 만들어줘야 한다.
N = int(input())
B = list(map(int, input().split()))
A = []

# 방정식 풀듯이.. 계산해서 역으로 구해주는 방법을 계산했다.
for i in range(N):
    A.append(B[i] * (i + 1) - sum(A))

# join을 이용해서 출력하려면 str로 바꾼후 출력해야 한다. 이런 경우엔 그냥 for문 사용해서 end = " "를 붙여 출력하는 것이 빠르다. 
print(" ".join(map(str, A)))
