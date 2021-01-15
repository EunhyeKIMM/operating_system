import json 

dic = {
    "file_name" : "c:/temp/example.txt", 
    "file_size" : 400500
}

l = [dic, dic]
list_msg = json.dumps(1)
print(type(list_msg))
print(list_msg)

l2 = json.loads(list_msg)
print(type(l2))
print(l2)


# 사전(파이썬 자료구조 객체) --> 문자열로 표현 
msg = json.dumps(dic)   # json.dump()
print(type(msg), msg)   # 문자열 msg를 전송

# 문자열 msg를 수신
# 문자열 --> 사전 객체로 복원 
dic2 = json.loads(msg)  # json.load()
print(type(dic2))
print(dic2) 

