# ex02.py

# 사용자 입출력(콘솔 입출력)
# BIF(Built in Function) - 내장 함수

# 사용자 입력
# 콘솔 입력이기 때문에 모든 입력값은 str이다.

# result = input('안내 메시지') # Blocking Input
# print(result)

# num1 = input('숫자 1 : ')
# num2 = input('숫자 2 : ')
# print(num1 + num2)
# print(int(num1) + int(num2))


# 출력 print()
print(10)
print('문자열')

print(10 + 20) # 산술 연산
print('홍' + '길동') # 문자열 더하기

print('하나' '둘' '셋')
#print(10 20)
print('하나', '둘', '셋') #console.log()

# print('하나', end='\n')
print('하나', end=' ')
print('둘')

a = 1
b = 2
print('%d + %d = %d' % (a, b, a + b))



# 파일 입출력

# 파일 생성하기
# f = open('file.txt', 'a') # f : 파일 참조 객체
# f.write('Hello\n')
# f.close()
# 
# print('쓰기 완료')



# 파일 읽기
f = open('file.txt', 'r')

# txt = f.readline() # readline()이 읽어온 엔터를 안버린다.
# print(txt, end='')
# txt = f.readline()
# print(txt, end='')
# txt = f.readline()
# print(txt, end='')
# txt = f.readline()
# print(txt, end='')


# while True:
#     txt = f.readline()
#     if not txt:
#         break
#     print(txt, end='')


# lines = f.readlines()
# 
# print(type(lines)) # <class 'list'>
# 
# for line in lines:
#     print(line, end='')

for line in f.readlines():
    print(line, end='')










