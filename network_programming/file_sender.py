import os
import socket 

HOST = "127.0.0.1"
PORT = 6000
FILE_PATH = "c:/Temp/example.txt"

def file_read(file_path):
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            yield data   

with socket.socket() as s:
    try:
        s.connect((HOST, PORT))
        fileSize = os.path.getsize(FILE_PATH)

        # 파일 크기 전송
        print("전송 파일 크기", fileSize)
        s.sendall(str(fileSize).encode())

        # 준비 상태 수신
        isready = s.recv(1024).decode()           
        if isready == "ready":
            # 파일 전송
            for data in file_read(FILE_PATH):
                s.sendall(data) 
            print("전송완료")

    except Exception as e:
        print(e)

