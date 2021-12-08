# coding=gbk
import tkinter 
from tkinter import * 
from tkinter.filedialog import * 
import os 
root = Tk() 
root.title('nginx����GUI') 
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
    w = Label(root,text="�����nginx����ĵ�һ���汾,лл���֧��") 
    w.pack(side=TOP) 
 
 
 
 
 
 
menubar = Menu(root) 
#���������˵�File��Ȼ������뵽�����Ĳ˵����� 
filemenu = Menu(menubar,tearoff=0) 
filemenu.add_command(label="�������ļ�", command=openfile) 
filemenu.add_command(label="���������ļ�", command=savefile) 
filemenu.add_separator() 
filemenu.add_command(label="�˳�", command=root.quit) 
menubar.add_cascade(label="nginx���ù���", menu=filemenu) 
 
#����һ�������˵�Edit 
editmenu = Menu(menubar, tearoff=0) 
editmenu.add_command(label="���߳���", command=threads) 
editmenu.add_command(label="״̬", command=status) 
editmenu.add_command(label="������", command=total) 
menubar.add_cascade(label="nginx������ز鿴",menu=editmenu) 
 
#���������˵�status 
editmenu = Menu(menubar, tearoff=0) 
editmenu.add_command(label="����nginx", command=start) 
editmenu.add_command(label="ֹͣnginx",command=stop) 
editmenu.add_command(label="����nginx", command=restart) 
menubar.add_cascade(label="nginx����",menu=editmenu) 
#���������˵�Help 
helpmenu = Menu(menubar, tearoff=0) 
helpmenu.add_command(label="about", command=about) 
menubar.add_cascade(label="�鿴�汾�Ͱ���", menu=helpmenu) 
#��ʾ�˵� 
root.config(menu=menubar) 
 
#��ʾ�˵� 
t.pack() 
mainloop()
