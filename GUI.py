from tkinter import *


class Tk_GUI:
    def __init__(self):
        #初始化Tk()
        self.GUI=Tk()
        self.GUI.title('抖音视频批量下载')

        #设置窗口大小
        self.width = 1024
        self.height = 768

        #获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        self.SCW = self.GUI.winfo_screenwidth()
        self.SCH = self.GUI.winfo_screenheight()
        self.GUI.geometry('%dx%d+%d+%d' % (self.width, self.height, (self.SCW-self.width)/2, (self.SCH-self.height)/2))
        self.v=IntVar()

        #列表中存储的是元素是元组
        self.language=[('python',0),('C++',1),('C',2),('J ava',3)]
        
    #定义单选按钮的响应函数
    def callRB(self):
        for i in range(4):
            if (self.v.get()==i):
                root1 = Tk()
                Label(root1,text='你的选择是'+self.language[i][0]+'!',fg='red',width=20, height=6).pack()
                Button(root1,text='确定',width=3,height=1,command=root1.destroy).pack(side='bottom')

if __name__ == '__main__':
    Tk_GUI = Tk_GUI()
    
    Label(Tk_GUI.GUI,text='选择一门你喜欢的编程语言').pack(anchor=W)
    #for循环创建单选框
    for lan,num in Tk_GUI.language:
        Radiobutton(Tk_GUI.GUI, text=lan, value=num, command=Tk_GUI.callRB, variable=Tk_GUI.v).pack(anchor=W)

    #进入消息循环
    Tk_GUI.GUI.mainloop()