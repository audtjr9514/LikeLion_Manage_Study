# 함수 [문제2] 평균값 계산
# 입력으로 들어오는 모든 수의 평균값을 계산해 주는 함수를 작성해 보자. 
# (단, 입력으로 들어오는 수의 갯수는 정해져 있지 않다.)


def sum_avg(x=[]):
    sum = 0
    for i in x:
        sum += int(i)
    avg = sum / len(x)
    print("입력받은 평균의 값은 %1.1f" %avg)

a = input("숫자를 입력하세요 : ").split(" ")
sum_avg(a)