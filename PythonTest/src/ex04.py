# ex04.py

# 집합, Set
# - 중복값 허용 안함
# - 순서가 없음(인덱스 사용 불가)

set1 = set([10, 20, 30]) # List -> Set 변환
print(set1)

set2 = set([1, 2, 3, 4, 5, 2, 4, 1, 6, 7])
print(set2)

print(type(set2))

# 어디선가 무작위로 데이터 가져와서 중복된 값 제거하고 결과 확인하기
# 파일 읽기 > 라인 1개 > Set 요소 추가(중복값 제거)
f = open('data.txt', 'r')

# print(len(f.readlines()))
# 
# print('file', type(f.readlines()))
# 
# print(f.readlines())

color = set(f.readlines())

print(color)



list = [ 1, 3, 5, 7, 9 ]

for n in list:
    print(n)

num = 2

if num in list:
    print('O')
else:
    print('X')


# 숫자 1 ~ 10까지 출력
print(type(range(10)))

for n in range(10):
    print(n)

for n in range(3, 8):
    print(n)

# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print('%d x %d = %d' % (i, j, i*j))
    print()













