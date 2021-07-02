#本程序是通过无限运行Linux的bash来实现的
#It will make system warning ->out if memory<- before crash (screen-washing) and crash Termux(author's phone RAM is 6GiB)
def crash():
    import os
    fo = open("./.crash.sh",'w')
    fo.write("bash ./.crash.sh\n")
    fo.write("bash -e ./.crash.sh\n")
    fo.close()
    os.popen("bash ./.crash.sh")
i = input("你确定要运行< 崩Termux >吗？(y)")
if i == 'y' or i == 'Y':
    crash()
