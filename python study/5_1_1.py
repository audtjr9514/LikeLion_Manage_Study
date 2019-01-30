# 클래스 [문제1] UpgradeCalculator
# 다음은 Calculator 클래스이다.
# class Calculator:
#     def __init__(self):
#         self.value = 0

#     def add(self, val):
#         self.value += val
# 위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가하시오. 즉, 다음과 같이 동작하는 클래스를 만드시오.
# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
# print(cal.value) // 10에서 7을 뺀 3을 출력
#-------------------------------------------------------------------

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
    def value():
        return self.value

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)
