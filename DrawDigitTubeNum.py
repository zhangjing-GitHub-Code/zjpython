import turtle as tt
import datetime,time
tt.setup(800,350,300,300)
#tt.Setup(800,350,300,300)
def drawGap():
    tt.pu()
    tt.fd(4)
def drawone(pd=False):
    drawGap()
    tt.pendown() if pd else tt.penup()
    tt.fd(22)
    drawGap()
    tt.right(90)
def drawDigit(num='0'):
    if num=='1': tt.fd(-5)
    #M
    drawone(True) if num in ['a','b','c','d','e','f','2','3','4','5','6','8','9'] else drawone(False)
    #RD
    drawone(True) if num in ['a','b','d','0','1','3','4','5','6','7','8','9'] else drawone(False)
    #D
    drawone(True) if num in ['b','c','d','e','0','2','3','5','6','8','9'] else drawone(False)
    #LD
    drawone(True) if num in ['a','b','c','d','e','f','0','2','6','8'] else drawone(False)
    tt.left(90) # Go up
    #LU
    drawone(True) if num in ['a','b','e','f','0','4','5','6','8','9'] else drawone(False)
    #U
    drawone(True) if num in ['a','e','f','0','2','3','5','6','7','8','9'] else drawone(False)
    #RU
    drawone(True) if num in ['a','d','0','1','2','3','4','7','8','9'] else drawone(False)
    tt.left(180)
    tt.pu()
    tt.fd(10)
def drawstr(fk):
    for i in fk:
        if i==" ":
            tt.pu()
            tt.forward(30)
            continue
        if i==";":
            tt.write('年',font={"Arial",18,"normal"})
            #tt.fd(10)
        elif i=="/":
            tt.write('月',font={"Arial",18,"normal"})
            tt.fd(25)
        elif i=="+":
            tt.write('日',font={"Arial",18,"normal"})
            tt.fd(25)
        elif i=="(":
            tt.write('时',font={"Arial",18,"normal"})
            tt.fd(25)
        elif i=="#":
            tt.write('分',font={"Arial",18,"normal"})
            tt.fd(25)
        elif i=="\\":
            tt.write('秒',font={"Arial",18,"normal"})
            tt.fd(25)
        else:
            drawDigit(i)
tt.pensize(2.5)
tt.speed(370)
tt.pu()
tt.fd(-360)
tt.hideturtle()
#drawstr("188 4 ffcf")
while True:
    tt.tracer(False)
    tt.clear()
    datee=datetime.datetime.now().strftime("%Y;%m/%d+%H(%M#%S\\")
    drawstr(datee)
    tt.pu()
    tt.goto(-360,0)
    time.sleep(0.1)
    tt.tracer(True)
