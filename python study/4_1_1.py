# 함수 [문제1] 홀수 짝수 판별
# 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성하시오.

def is_odd(x):
    if x%2 == 0:
        print("%d은 짝수입니다" %x)
    else:
        print("%d은 홀수입니다" %x)

a = int(input("숫자를 입력하세요 : "))
is_odd(a)
