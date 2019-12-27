Log 간단 정의
============

python 에서 간단하게 log 보여주기
-------------

1. python 에서 변수 내용 보기
##### python 에서는 print(s) 와 같이 간단하게 변수 내용을 출력할 수 있습니다. 

2. python 에서 class 내 변수 내용 확인
##### 그렇지만 class의 경우 안에 변수가 많을 경우 저렇게 간단하게 보면 더 헛갈릴 수 있어서
##### logexp.py 에 간단하게 예제를 만들어 봤습니다

##### s에 들어오는 class의 class의 명을 먼저 출력 합니다.
##### 그 후 dir(s)와 같이 하면 s 안에 있는 모든 요소의 리스트를 불러오는데요,
##### 그중에는 instancemethod도 있고 (멤버 함수) 변수도 있어서 
##### getattr으로 값을 불러온 후 , 함수의 경우 callable 여부를 살펴보면 함수인지 변수인지 알 수 있습니다
##### 그러면 변수명과 변수 내용을 출력하면 됩니다.

```python
def log(s):    
    print "Class Name : " + s.__class__.__name__
    for i in dir(s) :
        tmp = getattr( s, i )
        if tmp != None and not callable(tmp) and  __name__ != tmp :
            print i, tmp			
```

3. log file 쌓기
##### log file 이름을 미리 정해놓고 만들어서 쓰면 됩니다.
##### file 이름을 정해놓고 해당 날짜 이름으로 작성하고, 시간을 앞에 출력하면 됩니다.
##### 사용법은 a = logprint("aa") 와 같이 로그파일 이름을 정하고
##### a.prin("anafd") 이렇게 쓰면 됩니다
##### 로그파일 위치를 사전에 정해놓고, 나중에 필요하면 인자로 넘겨줘도 되지만 귀찮지요.


```python
import time

class logprint :

    name = ""

    def __init__(self, name_ ) :
        self.name = name_ 
    
    def prin( self,  s ) :
        f1 = open( "D:\Data\log\log_" + self.name + "." + time.strftime('%Y%m%d'), "at" )        
        f1.write( time.strftime("%H:%M:%S" ) + " " + s )
        
```

