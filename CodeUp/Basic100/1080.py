#1, 2, 3 ... 을 계속 더해나갈때, 그 합이 입력한 정수보다 크거나 같을 때까지, (0 ~ 1000) 계속 합하는 프로그램을 작성해보자.

#즉, 1부터 n까지 정수를 계속 합해 간다고 할 때, 어디까지 합해야 같거나 넘어서는지 알아보고자하는 문제이다.

a = int(input())
sum = 0

for i in range(1, 1001):
  if sum < a:
    sum += i
  else:
    print(i-1)
    break
    
 #이미 그 값이 크게 되면, sum 이 이전 i에서 넘은 것이기 때문에 else 안에서 i-1 을 출력해주는 것이다