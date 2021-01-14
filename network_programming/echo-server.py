import socket

HOST = '127.0.0.1'
PORT = 9999

# 주소 체계(address family): IPv4. 소켓 타입: TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_socket = socket.socket() 위의 값은 디폴트라 이렇게 써도 된다.

# 이미 열린 포트 충돌시 재사용 옵션 설정
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen()
# accept 함수에서 대기, 클라이언트 접속 시 새로운 소켓을 리턴
client_socket, addr = server_socket.accept()    # 제일 중요!

# 접속한 클라이언트의 주소 출력
print('Connected by', addr)


while True:
    # 메시지 수신 대기 
    data = client_socket.recv(1024)
    if not data:
        break

    # data(byte array)를 문자열로 변환하여 출력
    print('Received from', addr, data.decode())

    # 받은 문자열을 다시 클라이언트로 전송(에코)
    client_socket.sendall(data)
    
client_socket.close()
server_socket.close()