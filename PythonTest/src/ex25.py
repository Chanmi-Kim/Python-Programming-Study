# ex25.py
'''

윈도우 기반
- 작업 스케쥴러 기능 : 지정된 시간마다 특정 작업을 실행
- + 특정 조건 > 파이썬 프로그램 실행

python.exe : 실행 결과 출력
pythonw.exe : 실행 결과 미출력(화면에 아무것도 안나타남)

'''
print('안녕하세요.')
#input('')

f = open('log.txt', 'a')

for i in range(10000):
    print(i)
    f.write(str(i))

f.close()
















