# 사용자로부터 이름, 전화번호부, 성별을 입력받고 저장합니다.
# 성별의 경우 male 또는 female만 입력 받아야 하고
# 그 외의 경우는, unknown으로 저장합니다.
# 이름, 전화번호부, 성별을 포함한 클래스를 이용해야합니다.
# 입력이 완료되면 매번 전체 입력했던 전화번호의 목록을 출력하고,
# 이름에 "그만"이라고 입력했을시 입력을 중단하고 전화번호의 목록을 출력합니다.


class phone:
    Name = ""           # 없어도 됨
    Phonenumber = ""    # 없어도 됨
    Sex = ""            # 없어도 됨

    def __init__(self, Name, Phonenumber, Sex):
        self.Name = Name
        self.Phonenumber = Phonenumber
        if Sex == "male" or sex == "female":
            self.Sex = Sex
        else:
            self.Sex = "unknown"

    def print(self):
        print("이름은 "+self.Name+", 전화번호는 " +
              self.Phonenumber + ", 성별은 " + self.Sex + "입니다.")

phonelist = list()
while true:
    name = input("이름을 입력하세요 : ")
    if(name == "그만"):
        for person in phonelist:
            person.print()
        break
    phonenumber = input("전화번호를 입력하세요 : ")
    sex = input("성별을 입력하세요(male이나 female로 작성해주세요) : ")
    phonelist.append(phone(name, phonenumber, sex))
    for person in phonelist:
        person.print()
    print()  # 한줄 띄어서 출력하기 위해 쓴 print
