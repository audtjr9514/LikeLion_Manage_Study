# [문제2] MaxLimitCalculator

# 이번에 여러분이 작성해야 하는 클래스는 MaxLimitCalculator 클래스이다. 
# MaxLimitCalculator 클래스는 객체변수 value가 100이상의 값은 가질 수 없도록 제한하는 클래스이다. 
# 즉, 다음과 같이 동작해야 한다.

# cal = MaxLimitCalculator()
# cal.add(50)  # 50 더하기
# cal.add(60)  # 60 더하기

# print(cal.value)  # 100 출력 
# 단, 한가지 전제 조건이 있다. 그 조건은 반드시 다음과 같은 Calculator 클래스를 상속해서 만들어야 한다는 것이다.

# class Calculator:
#     def __init__(self):
#         self.value = 0

#     def add(self, val):
#         self.value += val
# 위와 같은 조건을 만족하는 MaxLimitCalculator 클래스를 작성하시오.

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
            
cal = MaxLimitCalculator()
cal.add(50)  # 50 더하기
cal.add(60)  # 60 더하기

print(cal.value)