
# 패키지(com.test.python) > 모듈(MyUtil.py)

# 모듈의 구성요소
# 1. 전역 변수 : X
# 2. 전역 함수 : O
# 3. 클래스 : O

def hello():
    return '안녕하세요.'

def hi():
    return '반갑습니다.'


class Student:
    # 멤버 변수
    name = ''
    age = 0
    
    # 생성자
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # 멤버 메소드
    def info(self):
        print('안녕하세요. 저는 %s입니다. 나이는 %d세입니다.' % (self.name, self.age))





















