#여기까지! 이제그만~
#https://codeup.kr/problem.php?id=1087

#1, 2, 3 ... 을 계속 더해나갈때, 그 합이 입력한 정수보다 같거나 작을 때까지, (0 ~ 1000) 계속 합하는 프로그램을 작성해보자.
#예를 들어 57을 입력하면 1+2+3+...+8+9+10=55 에 다시 11을 더해 66일 때 66이 출력되어야 한다.
#어느 정도까지 합을 계산할 지, 정수 한개를 입력받는다.
#1, 2, 3, 4, 5 ... 계속 더해가다가, 입력된 정수보다 커지거나 같아지는 경우, 그 때 까지의 합을 출력한다.

num = int(input())
sum = 0

for i in range(1, num+1):
  if sum >= num:
    print(sum) 
    break
  else:
    sum += i
