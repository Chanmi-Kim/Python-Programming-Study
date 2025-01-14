# ex08.py

# 모듈(Module) : 재사용 목적 > 기능 단위
# 패키지(Package) : 모듈 관리 목적 > 컨테이너(폴더)

# com.test.python 패키지 생성 > MyUtil.py
# 파이썬은 일반 폴더와 다르게 패키지 역할을 하는 폴더는 반드시 __init__.py을 소유해야 한다.


# 같은 패키지내의 모듈
import mod1 as m # Alias
import com.test.python.MyUtil as my

# 다른 패키지내의 모듈
import com.test.python.MyUtil # A
from com.test.python.MyUtil import hi
from com.test.python.MyUtil import Student # B

print(com.test.python.MyUtil.hello())
print(hi())


s1 = com.test.python.MyUtil.Student('홍길동', 20) # A
s1.info()

s2 = Student('아무개', 22) # B
s2.info()

















