程序运行说明
概述
这是一个基于TCP协议的client-server程序。
client端发送ASCII文件块给server端，发送的块长度随机，范围在[lmin, lmax]之间。
server端进行reverse处理，并返回给client端，client端会在命令行下打印出来。
过程中进行四种报文类型Initialization、agree、reverseRequest和reverseAnswer的交互。
server端能够同时处理2个及以上client端的同时请求。


运行环境
Python 3.8.10

配置选项
IP地址：ip
端口号：port
文件位置：path
最短切片长度：lmin
最长切片长度：lmax

运行方式
guest os上，
python3 reversetcpserver.py
host os的命令行方式下，
python udpclient.py <server_ip> <server_port>
python3 reversetcpclient.py <ip> <port> <path> <lmin> <lmax>

注意事项
请确保reversetcpserver.py在reversetcpclient.py运行之前已经启动，并且reversetcpserver.py的ip地址和端口与reversetcpclient.p设置一致。
文件位置应为客户端本地存在的文件路径。
