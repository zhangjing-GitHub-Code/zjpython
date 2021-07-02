import socket
print('你好，我是小i，有什么可以帮您?')
local_addr=('localhost',10000)
remote_addr=('192.168.1.245',20000)#ip地址请根据实际设定
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(local_addr)
ss.connect(remote_addr)
while 1:
    sendData=input('发送:')
    if sendData=='quit':
        ss.sendto('quit'.encode("utf-8"),remote_addr)
        break
    ss.send(sendData.encode("utf-8"),remote_addr)
    reciveData,rec_addr=ss.recvfrom(1024)
    if reciveData:
        print("小i @",rec_addr[0])
        print("发来消息:",reciveData.decode())
ss.close()
