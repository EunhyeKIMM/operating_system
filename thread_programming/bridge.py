from threading import Lock

class Bridge:
    def __init__(self):
        self.counter = 0
        self.name = "아무개"
        self.address = "모름"
        self.lock = Lock()

    def across(self, name, address):
        self.lock.acquire()
        # == CS(Critical Section) (임계 영역)
        self.counter += 1 
        self.name = name
        self.address = address
        self.check()
        # == CS(Critical Section) (임계 영역)
        self.lock.release()

    def toString(self):
        return "이름: {}, 출신 {}, 도전 횟수: {}".format(self.name, self.address, self.counter)
    # 나머지 두 줄은 강의 자료의 오타 
    # toString 함수는 check 함수에서 사용하는데 check이 쓰여지는 across는 이미 lock이 걸려있는 상태이므로 걸 필요가 없다.
    
    def check(self):
        if self.name[0] != self.address[0]:
            print("문제 발생!!! " + self.toString())