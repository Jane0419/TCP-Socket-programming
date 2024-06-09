# reversetcpclient.py
import socket
import struct
import sys
import random


# python reversetcpclient.py 192.168.128.128 4567 test.txt 10 20


def read_files(path):
    with open(path, 'r') as file:
        return file.read()


def main():
    if len(sys.argv) < 4:
        print("缺少必要的参数")
        sys.exit(1)
    # ip地址
    ip = sys.argv[1]
    # 端口
    port = int(sys.argv[2])
    # 文件位置
    path = sys.argv[3]
    # 切片长度
    lmin = int(sys.argv[4]) if len(sys.argv) > 4 else 10
    lmax = int(sys.argv[5]) if len(sys.argv) > 5 else 20

    data = read_files(path)
    length = len(data)
    # 切片
    bytes_block = []
    while length > 0:
        byte = random.randint(lmin, lmax)
        if byte > length:
            byte = length
        bytes_block.append(byte)
        length -= byte
    n = len(bytes_block)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

    # 发送initialization报文
    init_msg = struct.pack("!HI", 1, n)  # 打包为2Bytes+4Bytes的首部
    client.send(init_msg)

    # 接收agreement
    agree_msg = client.recv(1024).decode('utf-8')
    if agree_msg != "02":
        print("服务器拒绝了您的请求\n")
        client.close()
        sys.exit(1)
    new_test = ""
    loc = 0

    for i, byte in enumerate(bytes_block):
        # 发送reverseRequest
        num_block = data[loc:loc + byte]
        num_length = len(num_block)
        loc += byte
        request_msg = struct.pack("!HI", 3, num_length)  # 打包为2Bytes+4Bytes的首部
        reverse_request = request_msg + num_block.encode('utf-8')
        client.send(reverse_request)

        # 接收reverseAnswer
        reverse_answer = client.recv(1024)
        _, reverse_length = struct.unpack("!HI", reverse_answer[:6])
        reverse_num = reverse_answer[6:].decode('utf-8')

        # 第x块:反转的文本
        print(f"{i + 1}: {reverse_num}")
        new_test += reverse_num

    with open('reverse_test.txt', 'w') as o:
        o.write(new_test)

    client.close()


if __name__ == "__main__":
    main()
