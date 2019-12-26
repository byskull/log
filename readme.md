Log 간단 정의
============

python 에서 간단하게 log 보여주기
-------------

1. python 에서 변수 내용 보기
# python 에서는 print(s) 와 같이 간단하게 변수 내용을 출력할 수 있습니다. 

2. python 에서 class 내 변수 내용 확인
#### 그렇지만 class의 경우 안에 변수가 많을 경우 저렇게 간단하게 보면 더 헛갈릴 수 있어서
#### logexp.py 에 간단하게 예제를 만들어 봤습니다

#### s에 들어오는 class의 class의 명을 먼저 출력 합니다.
#### 그 후 dir(s)와 같이 하면 s 안에 있는 모든 요소의 리스트를 불러오는데요,
#### 그중에는 instancemethod도 있고 (멤버 함수) 변수도 있어서 
#### getattr으로 값을 불러온 후 , 함수의 경우 callable 여부를 살펴보면 함수인지 변수인지 알 수 있습니다
#### 그러면 변수명과 변수 내용을 출력하면 됩니다.

def log(s):    
    print "Class Name : " + s.__class__.__name__
    for i in dir(s) :
        tmp = getattr( s, i )
        if tmp != None and not callable(tmp) and  __name__ != tmp :
            print i, tmp