
"""
    Coded by  Abdul Wahab
    PhoneNo   +923174010084
    Email     abdulwahabrana47@gmail.com
    Web       codewithawr.epizy.com
    From      Tando_Jan_Muhmmad Sindh Pakistan
"""

from tkinter import ttk
import pymysql



with open('pass.txt','r') as f:
    pass_word = f.read()

log_host='localhost'
log_port=3306
log_user='root'
log_passwd =  pass_word
log_database='school_manigement'






class SMS_sender:
    def __init__(self,in_frame):

        #---------------MAKING-UI---------------#
        school_signature(frame=in_frame)




        self.add_new_frame=Frame(in_frame,bg='cyan',relief=FLAT)
        self.add_new_frame.place(x=600,y=10,width=900,height=330)
        
        self.Manage_Students_label=Label(self.add_new_frame,text='Seand SMS',font=('Time new roman',20,'bold'),bg='black',fg='white')
        self.Manage_Students_label.place(x=0,y=0,width=900)

        
        self.SMS_seand_label=Label(self.add_new_frame,text='SMS wants to Seand :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.SMS_seand_label.place(x=20,y=40)

        
        self.SMS_seand_entry=Text(self.add_new_frame,font=('time new roman',15,'bold'),relief=RIDGE)
        self.SMS_seand_entry.place(x=20,y=70,width=400,height=150)


        self.SLect_class_lebel=Label(self.add_new_frame,text='Seand SMS :',font=('Time new roman',15,'bold'),bg='cyan')
        self.SLect_class_lebel.place(x=600,y=40)


        classes=['Sleact','1','2','3','4','5','6','7','8','9','10','all Class']
        self.slect_class=ttk.Combobox(self.add_new_frame,values=classes,font=('times nem roman',15,'bold'))
        self.slect_class.place(x=600,y=70,width=150)
        self.slect_class.config(state='readonly')
        self.slect_class.set('Sleact')


        
        self.Enter_number_entry=Label(self.add_new_frame,text='Seand SMS :',font=('Time new roman',15,'bold'),bg='cyan')
        self.Enter_number_entry.place(x=600,y=120)

        self.Enter_number=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.Enter_number.place(x=600,y=150)


        
        self.defoult_devise_label=Label(self.add_new_frame,text='Defoult Devise',font=('Time new roman',15,'bold'),bg='cyan')
        self.defoult_devise_label.place(x=20,y=230)

        self.defoult_devise_entry=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.defoult_devise_entry.place(x=20,y=260)




        self.SLect_class_lebel=Label(self.add_new_frame,text='Seand SMS :',font=('Time new roman',15,'bold'),bg='cyan')
        self.SLect_class_lebel.place(x=240,y=230)


        Sims=['1','2']
        self.slect_defoult_sim=ttk.Combobox(self.add_new_frame,values=Sims,font=('times nem roman',15,'bold'))
        self.slect_defoult_sim.place(x=240,y=260,height=28,width=150)
        self.slect_defoult_sim.config(state='readonly')


        self.Seand_button=Button(self.add_new_frame,text='SEAND',bg='pale green',font=('Time new roman',15,'bold'),command=self.set_send_sms)
        self.Seand_button.place(x=600,y=250)

        









        self.secound_frame=Frame(in_frame,relief=FLAT,bg='gray')
        self.secound_frame.place(x=10,y=350,width=1510,height=410)


        self.searching_frame=Frame(self.secound_frame,relief=FLAT,bg='firebrick2')
        self.searching_frame.place(x=5,y=5,width=1485,height=85)

        self.searching=Label(self.searching_frame,text='Search for Student',font=('times new roman',30,'bold'),fg='black',bg='firebrick2')
        self.searching.place(x=0,y=0)

        Searching_optuns=['Name','Roll No','Contect']
        self.Searching_by=ttk.Combobox(self.searching_frame,values=Searching_optuns,font=('times nem roman',13,'bold'))
        self.Searching_by.place(x=530,y=8,width=85,height=40)
        self.Searching_by.config(state='readonly')
        self.Searching_by.set('Name')

        self.search_entry=Entry(self.searching_frame,relief=RIDGE,font=('times new roman',25,'bold'),bg='gray77',borderwidth=0)
        self.search_entry.place(x=617.5,y=8,width=300,height=40)

    
        
        self.search_button=Button(self.searching_frame,text='Search',font=('times new roman',15,'bold'),bg='gray95',borderwidth=0,command=self.searching_student)
        self.search_button.place(x=918,y=8,height=40)

        

        self.Refrash_button=Button(self.searching_frame,text='Refresh',font=('times new roman',15,'bold'),bg='firebrick3',borderwidth=0,command=self.show_all)
        self.Refrash_button.place(x=1375,y=0,width=110,height=55)


        self.scrol_bar_x=ttk.Scrollbar(self.secound_frame,orient=VERTICAL)
        
        
        self.scrol_bar_y=ttk.Scrollbar(self.secound_frame,orient=HORIZONTAL)

        style = ttk.Style()
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings


        self.tree_vew=ttk.Treeview(self.secound_frame,columns=(1,2,3,4,5,6,7,8),show='headings',height=11,
        xscrollcommand=self.scrol_bar_y.set,yscrollcommand=self.scrol_bar_x.set,style="mystyle.Treeview")


        self.scrol_bar_x.pack(side=RIGHT,fill=Y)
        self.scrol_bar_y.pack(side=BOTTOM,fill=X)

        self.tree_vew.heading(1,text='First Name')
        self.tree_vew.heading(2,text='Last Name')
        self.tree_vew.heading(3,text='Guardian')
        self.tree_vew.heading(4,text='Phone_No')
        self.tree_vew.heading(5,text='Class')
        self.tree_vew.heading(6,text='Roll_No')
        self.tree_vew.heading(7,text='Religion')
        self.tree_vew.heading(8,text='Gender')

        self.tree_vew.column(1,width=100,anchor=CENTER)
        self.tree_vew.column(2,width=120,anchor=CENTER)
        self.tree_vew.column(3,width=120,anchor=CENTER)
        self.tree_vew.column(4,width=100,anchor=CENTER)
        self.tree_vew.column(5,width=120,anchor=CENTER)
        self.tree_vew.column(6,width=120,anchor=CENTER)
        self.tree_vew.column(7,width=140,anchor=CENTER)
        self.tree_vew.column(8,width=100,anchor=CENTER)


        self.tree_vew.place(x=5,y=65,width=1485,height=325)
        self.tree_vew.bind("<ButtonRelease-1>",self.click_inserting)
        self.tree_vew.bind("<Return>",self.click_inserting)
        
        self.tree()


        try:
            self.defoult_devise_entry.insert(0,get_setting(what_to_get='defoult_devise'))
        except:
            pass
        try:
            self.slect_defoult_sim.set(get_setting(what_to_get='defoult_sim'))
        except:
            pass
        
            
                
    def tree(self):
        try:
            con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
            cur=con.cursor()
            cur.execute("Select First_Name, Last_Name, Guardian, Phone_No, Class, Roll_No, Religion, Gender, D_o_B, P_o_B, Lact_School, D_O_A, C_A, Progress, Conduct, D_o_L, C_L_F, R_o_L from students_info")
            self.row=cur.fetchall()
            self.tree_vew.delete(*self.tree_vew.get_children())
            if len(self.row)!=0:
                for i in self.row:
                    if str(i[15])=='' and str(i[16])=='':
                        self.tree_vew.insert('','end',values=i)
            con.commit()
            con.close()
        except:
            pass

                
                

    def searching_student(self):
        if self.Searching_by.get()=='Roll No':
            con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
            cur=con.cursor()
            cur.execute("Select First_Name, Last_Name, Guardian, Phone_No, Class, Roll_No, Religion, Gender from students_info where Roll_No=%s",self.search_entry.get())
            self.row=cur.fetchall()
            if len(self.row)!=0:
                self.tree_vew.delete(*self.tree_vew.get_children())
                for i in self.row:
                    self.tree_vew.insert('','end',values=i)
            con.commit()
            con.close()
        
        elif self.Searching_by.get()=='Name':
            con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
            cur=con.cursor()
            cur.execute("Select First_Name, Last_Name, Guardian, Phone_No, Class, Roll_No, Religion, Gender from students_info where First_Name=%s",self.search_entry.get())
            self.row=cur.fetchall()
            if len(self.row)!=0:
                self.tree_vew.delete(*self.tree_vew.get_children())
                for i in self.row:
                    self.tree_vew.insert('','end',values=i)
            con.commit()
            con.close()

        elif self.Searching_by.get()=='Contect':
            con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
            cur=con.cursor()
            cur.execute("Select First_Name, Last_Name, Guardian, Phone_No, Class, Roll_No, Religion, Gender from students_info where Phone_No=%s",self.search_entry.get())
            self.row=cur.fetchall()
            if len(self.row)!=0:
                self.tree_vew.delete(*self.tree_vew.get_children())
                for i in self.row:
                    self.tree_vew.insert('','end',values=i)
            con.commit()
            con.close()
        
        else:
            messagebox.showerror('Error','Please Chack Your Input or Slact Correct "Search By!" Option')
    



    def show_all(self):
        self.tree()
        self.search_entry.delete(0,END)
        self.Searching_by.set('Name')

    def click_inserting(self,ev):
        self.cur_row=self.tree_vew.focus()
        self.content=self.tree_vew.item(self.cur_row)
        self.info=self.content['values']

        self.Enter_number.delete(0,END)
        self.Enter_number.insert(0,self.info[3])


    def set_send_sms(self):
        api = get_setting(what_to_get='api')
        D_Devise = self.defoult_devise_entry.get()
        D_sim = self.slect_defoult_sim.get()
        msg_is = str(self.SMS_seand_entry.get(1.0,END))

        if self.slect_class.get()!='Sleact' and self.slect_class.get()!='all Class' and self.Enter_number.get()=='':
            con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
            cur=con.cursor()
            cur.execute("Select Phone_No, D_o_L, C_L_F from students_info where Class=%s",self.slect_class.get())
            row=cur.fetchall()
            con.commit()
            con.close()
            for i in row:
                if str(i[1]) == '' and str(i[2]) == '':
                    number = str(i[0])
                    msg_is = str(self.SMS_seand_entry.get(1.0,END))
                    send_sms(API=api,number=number,msg=msg_is,defult_devise=D_Devise,defoult_sim=D_sim)
                elif str(i[1]) != '' and str(i[2]) != '':
                    pass
            
        elif self.slect_class.get()=='all Class' and self.Enter_number.get()=='':
            con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
            cur=con.cursor()
            cur.execute("Select Phone_No, D_o_L, C_L_F from students_info")
            row=cur.fetchall()
            con.commit()
            con.close()
            for i in row:
                if str(i[1]) == '' and str(i[2]) == '':
                    number = str(i[0])
                    msg_is = str(self.SMS_seand_entry.get(1.0,END))
                    send_sms(API=api,number=number,msg=msg_is,defult_devise=D_Devise,defoult_sim=D_sim)
                elif str(i[1]) != '' and str(i[2]) != '':
                    pass


        elif self.slect_class.get()=='Sleact':

            if self.Enter_number.get() != '':
                number = self.Enter_number.get()
                send_sms(API=api,number=number,msg=msg_is,defult_devise=D_Devise,defoult_sim=D_sim)

            elif self.Enter_number.get() != '':
                pass



        # api = self.get_setting(what_to_get='api')
        # D_Devise = self.defoult_devise_entry.get()
        # D_sim = self.slect_defoult_sim.get()
        # number = num
        # msg_is = str(self.SMS_seand_entry.get(1.0,END))
        # self.send_sms(API=api,number=number,msg=msg_is,defult_devise=D_Devise,defoult_sim=D_sim)

        


if __name__!='__main__':
    from module.defs import *
    
if __name__=='__main__':
    from defs import *
    root = Tk()
    root.title('Sc_Ma_Sy Student_Maniger')
    root.geometry('1530x790+0+0')
    
    root.iconbitmap('LOGOS/main_icon.ico')

    student=SMS_sender(in_frame=root)

    
    root.mainloop()