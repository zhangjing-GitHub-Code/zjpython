from PIL import Image
import PIL,os
## Log Decoration start
reset="\033[0m"
step_log="\033[33m[\033[34m*\033[33m]\033[0m "
ok_log="\033[33m[\033[33m"+chr(10004)+"\033[33m]\033[0m "
err_log="\033[33m[\033[31m!\033[33m]\033[0m "
## Log Decoration end
if os.name=="nt":
    os.system("")
ascii_char=list('"$%_WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-/+@<>i!;:,^`. ')
def get_ascii(r,b,g,a=256):
    if a<=5: return " "
    gray = int(0.2126*r+g*0.7152+b*0.0722)
    unit=256/len(ascii_char)
    return ascii_char[int(gray//unit)]
fi=input(step_log+"要转换哪个图片? (./pre.png): ")
try:
    im=Image.open('pre.png') if len(fi)<=2 else Image.open(fi)
    W,H=90,50
    im=im.resize((W,H))
    txt=""
    for i in range(H):
        for j in range(W):
            txt+= get_ascii(*im.getpixel((j,i)))
        txt+="\n"
    fo = open("ascii_after.txt","w")
    fo.write(txt)
    if len(fi)<=1: fi='pre.png'
    print(ok_log+"已将`{}`转换为ascii art位于`ascii_after.txt`".format(fi))
    fo.close()
except FileNotFoundError:
    if len(fi)<=1: fi='./pre.png'
    print(err_log+"鬼! `{}`不存在！".format(fi))
except PIL.UnidentifiedImageError:
    if len(fi)<=1: fi='./pre.png'
    print(err_log+"你™告诉我 `{}` 是图片??".format(fi))
