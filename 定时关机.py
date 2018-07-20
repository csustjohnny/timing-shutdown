import os
from tkinter import *
from datetime import datetime
from tkinter import Button
from tkinter.simpledialog import askinteger
from tkinter.messagebox import *
def inputinfo():
    h = min(askinteger('输入','请输入时'),23)
    m = min(askinteger('输入','请输入分'),59)
    s = min(askinteger('输入','请输入秒'),59)
    now = datetime.now()
    nh,nm,ns = now.hour, now.minute, now.second
    if(h>=nh):
        counter = (h - nh) * 60 * 60 +(m - nm) * 60 + (s - ns)
    else:
        counter = (h - nh + 24) *60 * 60 + (m -nm) * 60 + (s - ns)
    os.system('shutdown -s -t {}'.format(counter))
    showinfo('','定时成功！')


def shutdown():
    os.system('shutdown -a')
    showinfo('','取消定时成功！')
def askquit():
    if askokcancel('确定','您确定要退出吗？'):
        os._exit(0)
    
window = Tk()
window.title('定时关机')
window.geometry('250x90')
Button(window, text='定时关机',command=inputinfo).pack(fill=X)
Button(window, text='取消定时',command=shutdown).pack(fill=X)
Button(window, text='退出', command=askquit).pack(fill=X)
window.mainloop()



##t = input('请输入关机时间，格式：时:分:秒\n')
##hms = t.split(':') if ':' in t else t.split('：')
##
##h,m,s = hms #目标时间
##h = min(int(h), 24)
##m = min(int(m),59)
##s = min(int(s),59)
##
##
