import time
#from win10toast import ToastNotifier
'''def showmsg(title,text):
    #title="P^yt&h*on T$$est@"
    toaster = ToastNotifier()
    #text="T$#he tex!t of P^yt&h*o#n T$$esT@"
    # 有icon的版本
    """toaster.show_toast("Hello World!!!",
                   "Python is 10 seconds awsm!",
                   icon_path="custom.ico",
                   duration=10)
    """
    # 无icon，采用python的icon
    toaster.show_toast(title,
                       text,
                       icon_path=None,
                       duration=2.5)
                   
    # 等待提示框关闭
    """#while toaster.notification_active(): time.sleep(0.01)"""'''
def sever_bot(in_msg):
    import random
    item_dict={'自行车':"""自行车，又称脚踏车或单车，通常是二轮的小型陆上车辆。
人骑上车后，以脚踩踏板为动力，是绿色环保的交通工具。
英文bicycle。其中bi意指二，而cycle意指轮，即两轮车。在中国内地、台湾、新加坡，通常称其为"自行车"或"脚踏车";在港澳则通常称其为"单车"(其实粤语通常都这么称呼);而在日本称为"自転(转)车"。
自行车种类很多，有单人自行车，双人自行车还有多人自行车。""",
'灯':'''灯，照明用品，泛指可以照亮的用具。人类远古时代用火把照明，后来有了蜡烛和油灯。
在古时"烛"是一种由易燃材料制成的火把，用于执持的已被点燃的火把，称之为烛;放在地上的用来点燃的成堆细草和树枝叫做燎，燎置于门外的称大烛，门内的则称庭燎。'''}
    if in_msg in item_dict.keys():
        return item_dict[in_msg]
        #showmsg("Python Socket服务器","接收到匹配的字符串：\n已自动回应")
    else:
        reply=['你说什么?',
               '你说得对!',
               '是不是你哪里写错了?',
               '好吧!',
               '我叫小i，你呢?']
        return random.choice(reply)
        #showmsg("Python Socket服务器","接收到匹配的字符串：{}\n已自动回应".format(reciveData.decode()))
import socket
print('此机是服务器，this is sever_bot')
local_addr=('localhost',20000)
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(local_addr)
#showmsg("Python Socket服务器","Python Socket服务器已启动")
while 1:
    ss.listen(4)
    ss.accept()
    #reciveData,rec_addr=ss.recvfrom(1024)
    while true:
        reciveData,rec_addr=ss.recv(1024)
        if reciveData:
            print("from",rec_addr)
            print("got messge:",reciveData.decode())
        
        if reciveData.decode()=='quit':
            ss.quit()
            break
        echo=sever_bot(reciveData.decode())
        ss.send(echo.encode("utf-8"))
    #showmsg("Python Socket服务器","接收到信息：{}\n已自动回应".format(reciveData.decode()))
ss.close()
#exit()
