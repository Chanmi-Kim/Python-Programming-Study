# ex05.py

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














    
    