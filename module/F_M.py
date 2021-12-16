
"""
    Coded by  Abdul Wahab
    PhoneNo   +923174010084
    Email     abdulwahabrana47@gmail.com
    Web       codewithawr.epizy.com
    From      Tando_Jan_Muhmmad Sindh Pakistan
"""

from tkinter import Button, Entry, Frame, Label, Text, Tk, ttk , PhotoImage
from tkinter.constants import BOTTOM, CENTER, END, FLAT, HORIZONTAL, RIDGE, RIGHT, VERTICAL, X, Y
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askyesno

import pymysql
import datetime as dt


with open('pass.txt','r') as f:
    pass_word = f.read()

log_host='localhost'
log_port=3306
log_user='root'
log_passwd =  pass_word
log_database='school_manigement'





class Fee_manigment:
    def __init__(self,in_frame):
        mounts = str(get_setting(what_to_get='mounth'))
        self.mounth_heding = mounts.split(',')




        self.add_fee_frame=Frame(in_frame,bg='cyan',relief=FLAT)
        self.add_fee_frame.place(x=990,y=10,width=530,height=300)
        
        self.Manage_Fee_label=Label(self.add_fee_frame,text='Manige Fee of Student',font=('Time new roman',20,'bold'),bg='black',fg='white')
        self.Manage_Fee_label.place(x=0,y=0,width=580)

        self.firstname=Label(self.add_fee_frame,text='Fist Name :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.firstname.place(x=10,y=40)

        self.enter_first_name=Entry(self.add_fee_frame,font=('times new roman',15,'bold'))
        self.enter_first_name.place(x=10,y=70,width=150)
        

        self.ID_NO=Label(self.add_fee_frame,text='Roll No :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.ID_NO.place(x=190,y=40)

        self.enter_ID_NO=Entry(self.add_fee_frame,font=('times new roman',15,'bold'))
        self.enter_ID_NO.place(x=190,y=70,width=150)

        self.Class_Label=Label(self.add_fee_frame,text='Class :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.Class_Label.place(x=370,y=40)

        self.Class_entry=Entry(self.add_fee_frame,font=('times new roman',15,'bold'))
        self.Class_entry.place(x=370,y=70,width=150)


        self.mounth_Label=Label(self.add_fee_frame,text='Slect Mounth :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.mounth_Label.place(x=10,y=110)

        self.Slct_Mouth_eidit=ttk.Combobox(self.add_fee_frame,values=self.mounth_heding,font=('times nem roman',13,'bold'),)
        self.Slct_Mouth_eidit.place(x=10,y=140,width=150)
        self.Slct_Mouth_eidit.config(state='readonly')
        self.Slct_Mouth_eidit.set('Sleact')
        
        self.Slct_Mouth_eidit.bind('<<ComboboxSelected>>', self.show_mounth)


        self.eidit_Label=Label(self.add_fee_frame,text='Slect Mounth :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.eidit_Label.place(x=190,y=110)

        self.eidit_entry=Entry(self.add_fee_frame,font=('times new roman',15,'bold'))
        self.eidit_entry.place(x=190,y=140,width=150)

        self.note_Label=Label(self.add_fee_frame,text='Note for Student :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.note_Label.place(x=10,y=170)

        self.Note_text=Text(self.add_fee_frame,font=('times new roman',15,'bold'))
        self.Note_text.place(x=10,y=200,height=80,width=200)


        self.refrash_entry=Button(self.add_fee_frame,text='Refrash',font=('arial',15,'bold'),bg='pale green',command=self.clear_entrys)
        self.refrash_entry.place(x=420,y=200,width=100)


        self.Save_eidit_entry=Button(self.add_fee_frame,text='Save',font=('arial',15,'bold'),bg='pale green',command=self.Save_month_fee)
        self.Save_eidit_entry.place(x=420,y=250,width=100)





        # self.enter_first_name.config(state=DISABLED)




        Cal_fram = Frame(in_frame,bg='red3')
        Cal_fram.place(x=990,y=325,width=536,height=436)
        

        frame = Frame(Cal_fram,bg='red3')
        frame.place(x=3,y=3,width=535,height=430)


        self.textdis = Entry(frame,borderwidth=5,font=('arial',15,'bold'))
        self.textdis.place(x=0,y=5,width=300,height=50)


        self.textdis.insert(0, '0')





        One_button = Button(frame,text='1',font=('arial',30,'bold'), command = lambda: self.numberEntry(1))
        One_button.place(x=0,y=59,height=92.5,width=100)

        two_button = Button(frame,text='2',font=('arial',30,'bold'), command = lambda: self.numberEntry(2))
        two_button.place(x=100,y=59,height=92.5,width=100)


        three_button = Button(frame,text='3',font=('arial',30,'bold'), command = lambda: self.numberEntry(3))
        three_button.place(x=200,y=59,height=92.5,width=100)


        four_button = Button(frame,text='4',font=('arial',30,'bold'), command = lambda: self.numberEntry(4))
        four_button.place(x=0,y=152,height=92.5,width=100)

        five_button = Button(frame,text='5',font=('arial',30,'bold'), command = lambda: self.numberEntry(5))
        five_button.place(x=100,y=152,height=92.5,width=100)


        six_button = Button(frame,text='6',font=('arial',30,'bold'), command = lambda: self.numberEntry(6))
        six_button.place(x=200,y=152,height=92.5,width=100)


        four_button = Button(frame,text='7',font=('arial',30,'bold'), command = lambda: self.numberEntry(7))
        four_button.place(x=0,y=245,height=92.5,width=100)

        five_button = Button(frame,text='8',font=('arial',30,'bold'), command = lambda: self.numberEntry(8))
        five_button.place(x=100,y=245,height=92.5,width=100)


        six_button = Button(frame,text='9',font=('arial',30,'bold'), command = lambda: self.numberEntry(9))
        six_button.place(x=200,y=245,height=92.5,width=100)



        coma_button = Button(frame,text='.',font=('arial',30,'bold'), command = lambda: self.numberEntry('.'))
        coma_button.place(x=0,y=337.5,height=92.5,width=100)

        zero_button = Button(frame,text='0',font=('arial',30,'bold'), command = lambda: self.numberEntry(0))
        zero_button.place(x=100,y=337.5,height=92.5,width=100)


        dubel_zero_button = Button(frame,text='00',font=('arial',30,'bold'), command = lambda: self.numberEntry('00'))
        dubel_zero_button.place(x=200,y=337.5,height=92.5,width=100)




        AC_button = Button(frame,text='AC',font=('arial',30,'bold'),command=self.AC)
        AC_button.place(x=305,y=7,height=110,width=110)

        C_button = Button(frame,text='C',font=('arial',30,'bold'),command=self.clare)
        C_button.place(x=420,y=7,height=110,width=110)


        Add_button = Button(frame,text='+',font=('arial',30,'bold'), command = lambda: self.operation("add"))
        Add_button.place(x=305,y=122,height=110,width=110)

        subtract_button = Button(frame,text='−',font=('arial',30,'bold'), command = lambda: self.operation("sub"))
        subtract_button.place(x=420,y=122,height=110,width=110)



        Multi_button = Button(frame,text='×',font=('arial',30,'bold'), command = lambda: self.operation("melt"))
        Multi_button.place(x=305,y=237,height=110,width=110)

        Devid_button = Button(frame,text='÷',font=('arial',30,'bold'), command = lambda: self.operation("devid"))
        Devid_button.place(x=420,y=237,height=110,width=110)



        Equl_button = Button(frame,text='=',font=('arial',30,'bold'),command = self.sum_of_total)
        Equl_button.place(x=305,y=352,height=75,width=225)










        self.secound_frame=Frame(in_frame,relief=FLAT,bg='gray')
        self.secound_frame.place(x=10,y=10,width=980,height=750)


        self.searching_frame=Frame(self.secound_frame,relief=FLAT,bg='firebrick2')
        self.searching_frame.place(x=6,y=5,width=950,height=85)




        for_class_optuns=['Sleact','1','2','3','4','5','6','7','8','9','10']
        self.for_class=ttk.Combobox(self.searching_frame,values=for_class_optuns,font=('times nem roman',13,'bold'))
        self.for_class.place(x=5,y=8,width=85,height=40)
        self.for_class.config(state='readonly')
        self.for_class.set('Sleact')


        Searching_optuns=['Name','Roll No','Contect']
        self.Searching_by=ttk.Combobox(self.searching_frame,values=Searching_optuns,font=('times nem roman',13,'bold'))
        self.Searching_by.place(x=100,y=8,width=85,height=40)
        self.Searching_by.config(state='readonly')
        self.Searching_by.set('Name')

        self.search_entry=Entry(self.searching_frame,relief=RIDGE,font=('times new roman',25,'bold'),bg='gray77',borderwidth=0)
        self.search_entry.place(x=187.5,y=8,width=300,height=40)

    
        
        self.search_button=Button(self.searching_frame,text='Search',font=('times new roman',15,'bold'),bg='gray95',borderwidth=0,command=self.searching_student)
        self.search_button.place(x=488,y=8,height=40)

        

        self.Refrash_button=Button(self.searching_frame,text='Refresh',font=('times new roman',15,'bold'),bg='firebrick3',borderwidth=0,command=self.show_all)
        self.Refrash_button.place(x=590,y=5,width=110,height=50)



        

        self.print_for_class_button=Button(self.secound_frame,text='Print',font=('times new roman',16,'bold'),bg='pale green',command=self.print_class_for)
        self.print_for_class_button.place(x=800,y=10,height=45,width=90)
        


        
        self.mounth_prograss = ttk.Progressbar(self.secound_frame,orient=HORIZONTAL,length=600,mode='determinate')
        self.mounth_prograss.place(x=304,y=63,height=9,width=604)
        self.prograss()

        self.scrol_bar_x=ttk.Scrollbar(self.secound_frame,orient=VERTICAL)



        self.scrol_bar_y=ttk.Scrollbar(self.secound_frame,orient=HORIZONTAL)

        style = ttk.Style()
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings




        self.tree_vew=ttk.Treeview(self.secound_frame,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16),show='headings',height=11,
        xscrollcommand=self.scrol_bar_y.set,yscrollcommand=self.scrol_bar_x.set,style="mystyle.Treeview")


        self.scrol_bar_x.pack(side=RIGHT,fill=Y)
        self.scrol_bar_y.pack(side=BOTTOM,fill=X)
        try:
            self.tree_vew.heading(1,text='First Name')
            self.tree_vew.heading(2,text='Roll No')
            self.tree_vew.heading(3,text='Class')
            self.tree_vew.heading(4,text=self.mounth_heding[0])
            self.tree_vew.heading(5,text=self.mounth_heding[1])
            self.tree_vew.heading(6,text=self.mounth_heding[2])
            self.tree_vew.heading(7,text=self.mounth_heding[3])
            self.tree_vew.heading(8,text=self.mounth_heding[4])
            self.tree_vew.heading(9,text=self.mounth_heding[5])
            self.tree_vew.heading(10,text=self.mounth_heding[6])
            self.tree_vew.heading(11,text=self.mounth_heding[7])
            self.tree_vew.heading(12,text=self.mounth_heding[8])
            self.tree_vew.heading(13,text=self.mounth_heding[9])
            self.tree_vew.heading(14,text=self.mounth_heding[10])
            self.tree_vew.heading(15,text=self.mounth_heding[11])
            self.tree_vew.heading(16,text="Total")
        except:
            pass
        


        self.tree_vew.column(1,width=100,anchor=CENTER)
        self.tree_vew.column(2,width=100,anchor=CENTER)
        self.tree_vew.column(3,width=100,anchor=CENTER)
        self.tree_vew.column(4,width=50,anchor=CENTER)
        self.tree_vew.column(5,width=50,anchor=CENTER)
        self.tree_vew.column(6,width=50,anchor=CENTER)
        self.tree_vew.column(7,width=50,anchor=CENTER)
        self.tree_vew.column(8,width=50,anchor=CENTER)
        self.tree_vew.column(9,width=50,anchor=CENTER)
        self.tree_vew.column(10,width=50,anchor=CENTER)
        self.tree_vew.column(11,width=50,anchor=CENTER)
        self.tree_vew.column(12,width=50,anchor=CENTER)
        self.tree_vew.column(13,width=50,anchor=CENTER)
        self.tree_vew.column(14,width=50,anchor=CENTER)
        self.tree_vew.column(15,width=50,anchor=CENTER)
        self.tree_vew.column(16,width=50,anchor=CENTER)


        self.tree_vew.place(x=5,y=70,width=952,height=650)
        self.tree_vew.bind("<ButtonRelease-1>",self.click_inserting)
        self.tree_vew.bind("<Return>",self.click_inserting)
        self.for_class.bind("<<ComboboxSelected>>",self.searching_student)
        self.tree()



    def Save_month_fee(self):
        if self.Slct_Mouth_eidit.get()!='Sleact':
            count=0
            for mounth in self.mounth_heding:
                count = count+1
                if mounth ==  self.Slct_Mouth_eidit.get():
                    if count <=9:
                        mounthcount = '0'+str(count)
                    elif count >=10:
                        mounthcount = str(count)
                    
            con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
            cur=con.cursor()
            cur.execute(f"Update students_info set Fee_Mounth{mounthcount}=%s, Fee_Note=%s where First_Name=%s and Roll_No=%s",(self.eidit_entry.get(),self.Note_text.get(1.0,END),self.enter_first_name.get(),self.enter_ID_NO.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Student as updated on Server')
            answer = askyesno(title='confirmation',message='do you want to Print rased for adding')
            if answer:
                name = self.enter_first_name.get()
                roll = self.enter_ID_NO.get()
                from_class = self.Class_entry.get()
                data = [name, roll, from_class]
                print_fee_raside(Stud_data=data)
            self.tree()

        if self.Slct_Mouth_eidit.get()=='Sleact':
                    
            con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
            cur=con.cursor()
            cur.execute(f"Update students_info set Fee_Note=%s where First_Name=%s and Roll_No=%s",(self.Note_text.get(1.0,END),self.enter_first_name.get(),self.enter_ID_NO.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Student as updated on Server')
            self.tree()

    
    def tree(self):
        try:
            con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
            cur=con.cursor()
            cur.execute(f"Select First_Name,Roll_No,Class,Fee_Mounth01,Fee_Mounth02,Fee_Mounth03,Fee_Mounth04,Fee_Mounth05,Fee_Mounth06,Fee_Mounth07,Fee_Mounth08,Fee_Mounth09,Fee_Mounth10,Fee_Mounth11,Fee_Mounth12,D_o_L,C_L_F from students_info")
            row=cur.fetchall()
            if len(row)!=0:
                self.tree_vew.delete(*self.tree_vew.get_children())
                for i in row:
                    if str(i[15])=='' and str(i[16])=='':
                        conv = lambda f : f or '0'
                        fees = [conv(f) for f in i]

                        total = 0
                        for num in fees[3:15]:
                            num = int(str(num).replace('None','0'))
                            total = total + num
        
                        info = (fees[0],fees[1],fees[2],fees[3],fees[4],fees[5],fees[6],fees[7],fees[8],fees[9],fees[10],fees[11],fees[12],fees[13],fees[14],total)
                        
                        self.tree_vew.insert('','end',values=info)
            con.commit()
            con.close()
        except:
            pass



    def prograss(self):
        if self.get_mounth()=='01':
            prograss=8.333-4.166
        elif self.get_mounth()=='02':
            prograss=8.333*2-4.166
        elif self.get_mounth()=='03':
            prograss=8.333*3-4.166
        elif self.get_mounth()=='04':
            prograss=8.333*4-4.166
        elif self.get_mounth()=='05':
            prograss=8.333*5-4.166
        elif self.get_mounth()=='06':
            prograss=8.333*6-4.166
        elif self.get_mounth()=='07':
            prograss=8.333*7-4.166
        elif self.get_mounth()=='08':
            prograss=8.333*8-4.166
        elif self.get_mounth()=='09':
            prograss=8.333*9-4.166
        elif self.get_mounth()=='10':
            prograss=8.333*10-4.166
        elif self.get_mounth()=='11':
            prograss=8.333*11-4.166
        elif self.get_mounth()=='12':
            prograss=8.333*12-4.166
        self.mounth_prograss['value']=prograss


        
    def searching_student(self,ev):
        if self.for_class.get()!='Sleact' and self.search_entry.get()=='':
            con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
            cur=con.cursor()
            cur.execute(f"Select First_Name,Roll_No,Class,Fee_Mounth01,Fee_Mounth02,Fee_Mounth03,Fee_Mounth04,Fee_Mounth05,Fee_Mounth06,Fee_Mounth07,Fee_Mounth08,Fee_Mounth09,Fee_Mounth10,Fee_Mounth11,Fee_Mounth12,D_O_L,C_L_F from students_info where Class={self.for_class.get()}")
            self.row=cur.fetchall()
            if len(self.row)!=0:
                self.tree_vew.delete(*self.tree_vew.get_children())
                for i in self.row:
                    if str(i[15])=='' and str(i[16])=='':
                        conv = lambda f : f or '0'
                        fees = [conv(f) for f in i]
                        total = 0
                        for num in fees[3:15]:
                            num = int(str(num).replace('None','0'))
                            total = total + num
                        info = (fees[0],fees[1],fees[2],fees[3],fees[4],fees[5],fees[6],fees[7],fees[8],fees[9],fees[10],fees[11],fees[12],fees[13],fees[14],total)
                        self.tree_vew.insert('','end',values=info)
                    
            con.commit()
            con.close()
        elif self.Searching_by.get()=='Roll No':
            con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
            cur=con.cursor()
            if self.for_class.get()!='Sleact':
                cur.execute(f"Select First_Name,Roll_No,Class,Fee_Mounth01,Fee_Mounth02,Fee_Mounth03,Fee_Mounth04,Fee_Mounth05,Fee_Mounth06,Fee_Mounth07,Fee_Mounth08,Fee_Mounth09,Fee_Mounth10,Fee_Mounth11,Fee_Mounth12,D_O_L,C_L_F from students_info where Roll_No={self.search_entry.get()} and Class={self.for_class.get()}")
            elif self.for_class.get()=='Sleact':
                cur.execute(f"Select First_Name,Roll_No,Class,Fee_Mounth01,Fee_Mounth02,Fee_Mounth03,Fee_Mounth04,Fee_Mounth05,Fee_Mounth06,Fee_Mounth07,Fee_Mounth08,Fee_Mounth09,Fee_Mounth10,Fee_Mounth11,Fee_Mounth12,D_O_L,C_L_F from students_info where Roll_No={self.search_entry.get()}")
            self.row=cur.fetchall()
            if len(self.row)!=0:
                self.tree_vew.delete(*self.tree_vew.get_children())
                for i in self.row:
                    if str(i[15])=='' and str(i[16])=='':
                        conv = lambda f : f or '0'
                        fees = [conv(f) for f in i]
                        total = 0
                        for num in fees[3:15]:
                            num = int(str(num).replace('None','0'))
                            total = total + num
                        info = (fees[0],fees[1],fees[2],fees[3],fees[4],fees[5],fees[6],fees[7],fees[8],fees[9],fees[10],fees[11],fees[12],fees[13],fees[14],total)
                        self.tree_vew.insert('','end',values=info)
            con.commit()
            con.close()
        
        elif self.Searching_by.get()=='Name':
            con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
            cur=con.cursor()
            if self.for_class.get()!='Sleact':
                cur.execute(f"Select First_Name,Roll_No,Class,Fee_Mounth01,Fee_Mounth02,Fee_Mounth03,Fee_Mounth04,Fee_Mounth05,Fee_Mounth06,Fee_Mounth07,Fee_Mounth08,Fee_Mounth09,Fee_Mounth10,Fee_Mounth11,Fee_Mounth12,D_O_L,C_L_F from students_info where First_Name=%s and Class={self.for_class.get()}",self.search_entry.get())
            elif self.for_class.get()=='Sleact':
                cur.execute("Select First_Name,Roll_No,Class,Fee_Mounth01,Fee_Mounth02,Fee_Mounth03,Fee_Mounth04,Fee_Mounth05,Fee_Mounth06,Fee_Mounth07,Fee_Mounth08,Fee_Mounth09,Fee_Mounth10,Fee_Mounth11,Fee_Mounth12,D_O_L,C_L_F from students_info where First_Name=%s",self.search_entry.get())
            self.row=cur.fetchall()
            if len(self.row)!=0:
                self.tree_vew.delete(*self.tree_vew.get_children())
                for i in self.row:
                    if str(i[15])=='' and str(i[16])=='':
                        conv = lambda f : f or '0'
                        fees = [conv(f) for f in i]
                        total = 0
                        for num in fees[3:15]:
                            num = int(str(num).replace('None','0'))
                            total = total + num
                        info = (fees[0],fees[1],fees[2],fees[3],fees[4],fees[5],fees[6],fees[7],fees[8],fees[9],fees[10],fees[11],fees[12],fees[13],fees[14],total)
                        self.tree_vew.insert('','end',values=info)
            con.commit()
            con.close()

        elif self.Searching_by.get()=='Contect':
            con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
            cur=con.cursor()
            if self.for_class.get()!='Sleact':
                cur.execute(f"Select First_Name,Roll_No,Class,Fee_Mounth01,Fee_Mounth02,Fee_Mounth03,Fee_Mounth04,Fee_Mounth05,Fee_Mounth06,Fee_Mounth07,Fee_Mounth08,Fee_Mounth09,Fee_Mounth10,Fee_Mounth11,Fee_Mounth12,D_O_L,C_L_F from students_info where Phone_No={self.search_entry.get()} and Class={self.for_class.get()}")
            elif self.for_class.get()=='Sleact':
                cur.execute(f"Select First_Name,Roll_No,Class,Fee_Mounth01,Fee_Mounth02,Fee_Mounth03,Fee_Mounth04,Fee_Mounth05,Fee_Mounth06,Fee_Mounth07,Fee_Mounth08,Fee_Mounth09,Fee_Mounth10,Fee_Mounth11,Fee_Mounth12,D_O_L,C_L_F from students_info where Phone_No={self.search_entry.get()}")
            self.row=cur.fetchall()
            if len(self.row)!=0:
                self.tree_vew.delete(*self.tree_vew.get_children())
                for i in self.row:
                    if str(i[15])=='' and str(i[16])=='':
                        conv = lambda f : f or '0'
                        fees = [conv(f) for f in i]
                        total = 0
                        for num in fees[3:15]:
                            num = int(str(num).replace('None','0'))
                            total = total + num
                        info = (fees[0],fees[1],fees[2],fees[3],fees[4],fees[5],fees[6],fees[7],fees[8],fees[9],fees[10],fees[11],fees[12],fees[13],fees[14],total)
                        self.tree_vew.insert('','end',values=info)
            con.commit()
            con.close()
        
        else:
            messagebox.showerror('Error','Please Chack Your Input or Slact Correct "Search By!" Option')
    



    def click_inserting(self,ev):
        self.cur_row=self.tree_vew.focus()
        self.content=self.tree_vew.item(self.cur_row)
        self.info=self.content['values']
        if len(self.info)>0:
            
            con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
            cur=con.cursor()
            cur.execute(f"Select Fee_Note from students_info where First_Name=%s and Roll_No=%s and Class=%s",(self.info[0],self.info[1],self.info[2]))
            row=cur.fetchone()
            row = str(row[0])
            con.commit()
            con.close()

        
            self.enter_first_name.config(state='normal')
            self.enter_ID_NO.config(state='normal')
            self.Class_entry.config(state='normal')

            self.clear_entrys()

            self.enter_first_name.insert(0,self.info[0])
            self.enter_ID_NO.insert(0,self.info[1])
            self.Class_entry.insert(0,self.info[2])
            self.Note_text.insert(1.0,row)

            MAF = self.info[3:15]
            global dic_fee
            dic_fee = (MAF[0],MAF[1],MAF[2],MAF[3],MAF[4],MAF[5],MAF[6],MAF[7],MAF[8],MAF[9],MAF[10],MAF[11])


            self.enter_first_name.config(state='disabled')
            self.enter_ID_NO.config(state='disabled')
            self.Class_entry.config(state='disabled')
        elif len(self.info)<=0:
            pass

    def show_mounth(self,ev):
        count=0
        for mounth in self.mounth_heding:
            count = count+1
            if mounth ==  self.Slct_Mouth_eidit.get():
                m = int(count)
        self.eidit_entry.delete(0,END)
        m = m-1
        self.eidit_entry.insert(0,dic_fee[m])

    
    def clear_entrys(self):
        self.enter_first_name.config(state='normal')
        self.enter_ID_NO.config(state='normal')
        self.Class_entry.config(state='normal')

        self.enter_first_name.delete(0,END)
        self.enter_ID_NO.delete(0,END)
        self.Class_entry.delete(0,END)
        self.Slct_Mouth_eidit.set('Sleact')
        self.eidit_entry.delete(0,END)
        self.Note_text.delete(1.0,END)

    def show_all(self):
        self.Searching_by.set('Name')
        self.search_entry.delete(0,END)
        self.for_class.set('Sleact')
        self.tree()
    

    def print_class_for(self):
        if self.for_class.get() != 'Print of class':
            he = ("First_Name",'Roll_No','Class','Jan','Fab','Mar','Apr','May','Jun','July','Agu','Sep','Oct','Nav','Des')
            print_fee_form(for_class=self.for_class.get())
        else:
            messagebox.showerror('Error','Pleas Slact a Class to Print of!')


    def get_mounth(self):
        date = dt.date.today()
        s=str(date)
        mounth = str(s[5]+s[6])
        return mounth
        



    total = 0
    current = ""
    input_value = True
    check_sum = False
    op = " "
    result = False

    def AC(self):
        self.check_sum = False
        self.textdis.delete(0,END)

    def clare(self):
        self.textdis.delete(self.textdis.index("end") - 1)

    def numberEntry(self, num):
        self.result = False
        firstnum = self.textdis.get()
        secoundnum = str(num)
        if self.input_value:
            self.current = secoundnum
            self.input_value = False
        else:
            if secoundnum == '.':
                if secoundnum in firstnum:
                    return
            self.current = firstnum + secoundnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total =float(self.textdis.get())

    def valid_function(self):
        f_num=self.total
        s_num = self.current

        if self.op == "add":
            simbel ='+'
            self.total += self.current
        if self.op == "sub":
            simbel ='-'
            self.total -= self.current
        if self.op == "melt":
            simbel ='x'
            self.total *= self.current
        if self.op == "devid":
            simbel ='%'
            self.total /= self.current
        self.input_value = True
        self.check_sum = False
        sp = 23-len(f'{f_num}{simbel}{int(s_num)}=')
        space=('_'*(int(sp-len(f'{self.total}')/2)))
        self.display(f'{f_num}{simbel}{s_num}={space}{self.total}')

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def display(self, value):
        self.textdis.delete(0,END)
        self.textdis.insert(0, value)
        self.textdis.xview_moveto(1)





if __name__!='__main__':
    from module.defs import *
    
if __name__=='__main__':
    from defs import *
    root = Tk()
    root.title('Sc_Ma_Sy Fee_manigment')
    root.geometry('1530x790+0+0')
    
    root.iconbitmap('LOGOS/main_icon.ico')

    student=Fee_manigment(in_frame=root)
    root.mainloop()
