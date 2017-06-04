import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('sayhier.gicp.net', 39654))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))

data_to_send = [ ]
i=500
while i>0:
    data_to_send.append(bytes(str(i), encoding = "utf8"))
    i = i - 1

print (data_to_send)
#for data in [b'Michael', b'Tracy', b'Sarah']:
for data in data_to_send:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
    #print(int.from_bytes(s.recv(1024), byteorder='big'))
    #int.from_bytes(b'\x00\x10', byteorder='big')
s.send(b'exit')
s.close()