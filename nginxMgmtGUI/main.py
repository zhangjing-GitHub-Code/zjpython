# coding=gbk
import tkinter 
from tkinter import * 
from tkinter.filedialog import * 
import os 
root = Tk() 
root.title('nginx管理GUI') 
root.geometry('800x400') 
t = tkinter.Text(root,height=20,width=100,bg='grey',wrap = 'word' ) 
 
def openfile(): 
    t.delete(1.0, 'end') 
    fd = LoadFileDialog(root) 
    filename = fd.go() 
    content = open(filename, 'r') 
    lines= content.readlines() 
    for line in lines: 
        t.insert('end',line) 
#    file.close() 
 
def savefile(): 
    fd = SaveFileDialog(root) 
    filename= fd.go() 
    file = open(filename, 'w') 
    content = t.get(1.0, END) 
    file.write(content) 
    file.close() 
 
 
def threads(): 
    t.delete(1.0, 'end') 
    result = os.popen('ps -ef | grep nginx | grep -v grep|wc -l').readlines() 
    t.insert(INSERT, "\n".join(result), "a") 
 
 
def status(): 
    t.delete(1.0, 'end') 
    result = os.popen('sh status.sh').readlines() 
    t.insert(INSERT, "\n".join(result), "a") 
 
def total(): 
    t.delete(1.0, 'end') 
    result = os.popen('sh conn.sh').readlines() 
    t.insert(INSERT, "\n".join(result), "a") 
 
 
 
 
 
def start(): 
    t.delete(1.0, 'end') 
    result = os.popen('nginx').readlines() 
    t.insert(INSERT, "\n".join(result), "a") 
def stop(): 
    t.delete(1.0, 'end') 
    result = os.popen('nginx -s quit').readlines()     
    t.insert(INSERT, "\n".join(result), "a") 
def restart(): 
    t.delete(1.0, 'end') 
    result = os.popen('nginx -s restart').readlines() 
    t.insert(INSERT, "\n".join(result), "a") 
 
 
 
 
def about(): 
    t.delete(1.0, 'end') 
    w = Label(root,text="这个是nginx管理的第一个版本,谢谢大家支持") 
    w.pack(side=TOP) 
 
 
 
 
 
 
menubar = Menu(root) 
#创建下拉菜单File，然后将其加入到顶级的菜单栏中 
filemenu = Menu(menubar,tearoff=0) 
filemenu.add_command(label="打开配置文件", command=openfile) 
filemenu.add_command(label="保存配置文件", command=savefile) 
filemenu.add_separator() 
filemenu.add_command(label="退出", command=root.quit) 
menubar.add_cascade(label="nginx配置管理", menu=filemenu) 
 
#创建一个下拉菜单Edit 
editmenu = Menu(menubar, tearoff=0) 
editmenu.add_command(label="总线程数", command=threads) 
editmenu.add_command(label="状态", command=status) 
editmenu.add_command(label="连接数", command=total) 
menubar.add_cascade(label="nginx基本监控查看",menu=editmenu) 
 
#创建下拉菜单status 
editmenu = Menu(menubar, tearoff=0) 
editmenu.add_command(label="启动nginx", command=start) 
editmenu.add_command(label="停止nginx",command=stop) 
editmenu.add_command(label="重启nginx", command=restart) 
menubar.add_cascade(label="nginx操作",menu=editmenu) 
#创建下拉菜单Help 
helpmenu = Menu(menubar, tearoff=0) 
helpmenu.add_command(label="about", command=about) 
menubar.add_cascade(label="查看版本和帮助", menu=helpmenu) 
#显示菜单 
root.config(menu=menubar) 
 
#显示菜单 
t.pack() 
mainloop()
