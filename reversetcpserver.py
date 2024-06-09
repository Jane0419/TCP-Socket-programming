# reversetcpserver.py
import socket
import struct
import threading


# python3 reversetcpserver.py


def f(client_socket):
    # 接收initialization报文
    init = client_socket.recv(6)
    types, n = struct.unpack("!HI", init)  # 解打包成字符串
    n = int(n)

    # agree报文
    client_socket.send(b"02")

    for i in range(n):
        # 接收reverseRequest
        reverse_request = client_socket.recv(1024)
        _, data_length = struct.unpack("!HI", reverse_request[:6])
        data = reverse_request[6:].decode('utf-8')

        # reverse
        reverse_data = data[::-1]
        reverse_length = len(reverse_data)

        # 发送reverseAnswer
        answer_msg = struct.pack("!HI", 4, reverse_length)  # 打包为2Bytes+4Bytes的二进制数据
        reverse_answer = answer_msg + reverse_data.encode('utf-8')
        client_socket.send(reverse_answer)

    client_socket.close()


def main():
    server_ip = "0.0.0.0"
    server_port = 4567

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)  # 最大连接数
    print(f"接收 {server_ip}:{server_port}")
    # 同时请求-多线程
    while True:
        client_socket, addr = server.accept()
        print(f"新的客户端 {addr[0]}:{addr[1]}")
        client = threading.Thread(target=f, args=(client_socket,))
        client.start()


if __name__ == "__main__":
    main()
