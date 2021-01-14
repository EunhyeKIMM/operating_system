#import threading
from threading import Thread

count = 2 # 운영할 스레드의 개수 

def sum(low, high):
    global count 
    total = 0
    for i in range(low, high):
        total += i 
    print("Subthread", total)
    count -= 1

t1 = Thread(target=sum, args=(1, 100000))
t2 = Thread(target=sum, args=(1, 10000000))
t1.start()
t2.start()

while count != 0:
    pass 

print("Main Thread")