# ex03.py

# 집합 자료형
# - 배열(Array) : 파이썬에는 없음

# 튜플, Tuple
# - 리스트 계열
tuple1 = (10, 20, 30)
print(tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
# print(tuple1[3]) # tuple index out of range
print(type(tuple1)) # 스크립트 언어들은 반드시 자료형 확인하는 습관

# 루프 탐색
# 파이썬 루프 제어문
# for in 문 = 자바스크립트(foreach문) <> 자바(foreach 문)
# 파이썬의 for문 -> 무조건 배열 탐색
for n in tuple1:
    print(n)

# 튜플의 특징 : 읽기 전용
# tuple1[0] = 100
# print(tuple1)


tuple2 = (10,) # 2.XX 파이썬은 에러발생
print(tuple2)

tuple3 = 10, 20, 30, 40 # 튜플이 가장 기본 집합 자료형
print(tuple3)

atuple = (10, 20, 30)
btuple = (5, 15, 25, 30)

print(atuple + btuple)
print(atuple * 3)

tuple4 = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print(tuple4[3])
print(tuple4[3:]) # 부분 집합 추출
print(tuple4[:3])
print(tuple4[3:6])




# 리스트, List
# - 튜플 : 읽기 전용
# - 리스트 : 읽기/쓰기 가능
list1 = [ 10, 20, 30, 40, 50 ]
print(list1)
print(type(list1))

list2 = [ 'red', 'blue', 'yellow' ]
list3 = [ '홍길동', 20, '서울시', 100 ] # 자료형 혼합 가능 > 비권장
list4 = [ 100, 200, [ 300, 400 ], 500 ] # Jagged Array

print(list2 + list3)
print(list2 * 2)

print(list3[2:])

print(list3[0])
list3[0] = 1000 # 리스트는 요소의 값을 수정이 가능하다.
print(list3[0])

for n in list3:
    print(n)

print(len(tuple1))
print(len(list1))





# 딕셔너리
# - 연관 배열(key, value)
dic1 = { "color": "red", "size": 100 }
print(dic1)
print(type(dic1))

hong = { 'name':'홍길동', 'age': 20, 'address': { '시': '서울시', '구': '강남구', '동': '역삼동' } }
print('이름' , hong['name'])
print('나이', hong['age'])
print('주소', hong['address'])
print('주소(동)', hong['address']['동'])













