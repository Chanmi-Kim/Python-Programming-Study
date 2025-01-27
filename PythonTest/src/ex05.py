# ex05.py
from chardet.latin1prober import OTH

# 파이썬 클래스
class Item:
    # 멤버(변수, 메소드(함수))
    pass # 아무것도 아님

# if num > 0:
#     print("액션")
# else
#     pass

# Item item1 = new Item();
item1 = Item()

print(type(item1))
print(item1)


# 좌표 클래스
class Point:
    x = 100
    y = 200

    def check(self): # self 매개변수는 멤버 메소드의 첫번째 매개변수
        print('x = %d, y = %d' % (self.x, self.y)) # self = this
        
p1 = Point()
p1.check()



class Size:
    # width
    # height
    # self.width = width
    
    def setSize(self, width, height):
        self.width = width
        self.height = height

size1 = Size()
# print(size1.width)
# print(size1.height)

size1.setSize(300, 400)
print(size1.width)
print(size1.height)


class Computer:
    cpu = 'i5' # public
    __memory = '16gb' # private
    
com = Computer()
# print(com.cpu, com.__memory)
# AttributeError: 'Computer' object has no attribute 'memory'

# 생성자
class Cup:
    # 멤버 변수
    # size = 0
    # color = 'white'
    
    # 생성자(__init__)
#     def __init__(self):
#         self.size = 0
#         self.color = 'white'
    
    def __init__(self, size, color):
        self.size = size
        self.color = color

cup1 = Cup(100, 'blue')
print(cup1.size)
print(cup1.color)



# 클래스 상속
class Parent:
    name = '부모'
    def hello(self):
        print('안녕하세요.')

class Child(Parent):
    nick = '자식'
    name = '자식이 또 추가'
    def hi(self):
        print('방가~')
    def hello(self):
        print("Hi~")

child = Child()
print(child.name)
print(child.nick)
child.hello()
child.hi()




# 연산자 오버로딩(***)
# - 연산자도 메소드처럼 취급해서 오버로딩을 가능하게 만드는 기술
# result = sum(10, 20) # sum(int, int)
# result = sum(3.5, 2.5) # sum(float, float)
# 
# result = 10 + 20
# result = 2.5 + 2.5

class Note:
    page = 0
    color = ''
    def __init__(self, page, color):
        self.page = page
        self.color = color
    def __add__(self, other):
        # print(self.page + other.page)
        return Note(self.page + other.page, self.color)

n1 = Note(100, 'white')
n2 = Note(150, 'black')

# Note + Note = Note
# print(n1 + n2)
n3 = n1 + n2 # + n4 + n5
print(n3.page)
print(n3.color)

#n3 = bindNote(bindNote(bindNote(n1, n2), n4), n5)













    
    