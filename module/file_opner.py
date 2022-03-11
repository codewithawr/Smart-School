
"""
    Coded by  Abdul Wahab
    PhoneNo   +923174010084
    Email     abdulwahabrana47@gmail.com
    Web       codewithawr.epizy.com
    From      Tando_Jan_Muhmmad Sindh Pakistan
"""


from time import sleep
from tkinter import Button, Entry, Frame, Label, PhotoImage, Tk, filedialog, ttk
from tkinter.constants import BOTTOM, CENTER, END, FLAT, HORIZONTAL, RIDGE, RIGHT, VERTICAL, X, Y
from tkinter import messagebox
from tkinter.messagebox import askyesno
import datetime as dt



with open('pass.txt','r') as f:
    pass_word = f.read()

log_host='localhost'
log_port=3306
log_user='root'
log_passwd =  pass_word
log_database='school_manigement'




class file_opner:
    def __init__(self,in_frame):

        #---------------MAKING-UI---------------#
        school_signature(frame=in_frame)


        
        self.path=''

        self.add_new_frame=Frame(in_frame,bg='cyan',relief=FLAT)
        self.add_new_frame.place(x=600,y=10,width=900,height=330)
        
        self.Manage_Students_label=Label(self.add_new_frame,text='Manage Students Data from file',font=('Time new roman',20,'bold'),bg='black',fg='white')
        self.Manage_Students_label.place(x=0,y=0,width=900)


        
        self.firstname=Label(self.add_new_frame,text='Fist Name :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.firstname.place(x=20,y=48)

        self.enter_first_name=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_first_name.place(x=20,y=78,width=165)


        self.last_name=Label(self.add_new_frame,text='Last Name :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.last_name.place(x=215,y=48)

        self.enter_last_name=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_last_name.place(x=215,y=78,width=100)

                
                

        self.father_name=Label(self.add_new_frame,text='Guardian :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.father_name.place(x=345,y=48)

        self.enter_father_name=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_father_name.place(x=345,y=78,width=165)




        self.Phone_No=Label(self.add_new_frame,text='Phone_No :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.Phone_No.place(x=540,y=48)

        self.enter_Phone_No=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_Phone_No.place(x=540,y=78,width=143)


        self.Class=Label(self.add_new_frame,text='Class :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.Class.place(x=713,y=48)

        classes=['1','2','3','4','5','6','7','8','9','10']
        self.Class_slaction=ttk.Combobox(self.add_new_frame,values=classes,font=('times nem roman',15,'bold'))
        self.Class_slaction.place(x=713,y=78,width=143)
        self.Class_slaction.config(state='readonly')
        self.Class_slaction.set('Class')

        




        self.ID_NO=Label(self.add_new_frame,text='Roll No :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.ID_NO.place(x=20,y=119)

        self.enter_ID_NO=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_ID_NO.place(x=20,y=149,width=100)



        self.religion=Label(self.add_new_frame,text='Religion :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.religion.place(x=150,y=119)

        self.enter_religion=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_religion.place(x=150,y=149,width=100)






        self.Gender=Label(self.add_new_frame,text='Gender :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.Gender.place(x=280,y=119)


        genders=['Male','Female']
        self.Gender_slaction=ttk.Combobox(self.add_new_frame,values=genders,font=('times nem roman',15,'bold'))
        self.Gender_slaction.place(x=280,y=149,width=100)
        self.Gender_slaction.config(state='readonly')
        self.Gender_slaction.set('Gender')


        self.D_O_B=Label(self.add_new_frame,text='D,O,Birth :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.D_O_B.place(x=410,y=119)

        self.enter_D_O_B=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_D_O_B.place(x=410,y=149,width=100)



        self.Address=Label(self.add_new_frame,text='Place of Birth :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.Address.place(x=540,y=119)

        self.enter_Address=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_Address.place(x=540,y=149,width=143)




        self.Last_School=Label(self.add_new_frame,text='Last School :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.Last_School.place(x=20,y=192)

        self.enter_Last_School=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_Last_School.place(x=20,y=222,width=200)


        self.DOA=Label(self.add_new_frame,text='D,O,Admition :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.DOA.place(x=250,y=192)

        self.enter_DOA=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_DOA.place(x=250,y=222,width=130)


        self.Class_Admiteddted=Label(self.add_new_frame,text='Class Admiddted :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.Class_Admiteddted.place(x=410,y=192)

        self.enter_Class_Admiteddted=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_Class_Admiteddted.place(x=410,y=222,width=150)


        self.Prigres=Label(self.add_new_frame,text='Progress :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.Prigres.place(x=590,y=192)

        self.enter_Prigres=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_Prigres.place(x=590,y=222,width=93)






        self.Conduct=Label(self.add_new_frame,text='Conduct :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.Conduct.place(x=20,y=265)

        self.enter_Conduct=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_Conduct.place(x=20,y=295,width=140)



        self.DOl=Label(self.add_new_frame,text='D,O,Living :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.DOl.place(x=190,y=265)

        self.enter_DOl=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_DOl.place(x=190,y=295,width=100)



        self.class_left_from=Label(self.add_new_frame,text='Class Left From :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.class_left_from.place(x=320,y=265)

        self.enter_class_left_from=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_class_left_from.place(x=320,y=295,width=150)



        self.Resion_of_left=Label(self.add_new_frame,text='Resion of Leaving :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.Resion_of_left.place(x=500,y=265)

        self.enter_Resion_of_left=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_Resion_of_left.place(x=500,y=295,width=183)





        buttoun_X = int(780)



        self.add_button=Button(self.add_new_frame,text='Add',font=('times new roman',17,'bold'),bg='pale green',bd=4,command=self.add_student)
        self.add_button.place(x=buttoun_X,y=140,width=110,height=35)

        self.upd_button=Button(self.add_new_frame,text='Update',font=('times new roman',17,'bold'),bg='pale green',bd=4,command=self.update_student)
        self.upd_button.place(x=buttoun_X,y=190,width=110,height=35)

        self.delet_button=Button(self.add_new_frame,text='Delete',font=('times new roman',17,'bold'),bg='pale green',bd=4,command=self.delet_student)
        self.delet_button.place(x=buttoun_X,y=240,width=110,height=35)

        self.clear_button=Button(self.add_new_frame,text='Clear',font=('times new roman',17,'bold'),bg='pale green',bd=4,command=self.clare_feleds)
        self.clear_button.place(x=buttoun_X,y=290,width=110,height=35)












        self.secound_frame=Frame(in_frame,relief=FLAT,bg='gray')
        self.secound_frame.place(x=10,y=350,width=1510,height=410)


        self.searching_frame=Frame(self.secound_frame,relief=FLAT,bg='firebrick2')
        self.searching_frame.place(x=5,y=5,width=1485,height=85)

        self.searching=Label(self.searching_frame,text='Search for Student',font=('times new roman',30,'bold'),fg='black',bg='firebrick2')
        self.searching.place(x=0,y=0)
        

        for_class_optuns=['Sleact','1','2','3','4','5','6','7','8','9','10']
        self.for_class=ttk.Combobox(self.searching_frame,values=for_class_optuns,font=('times nem roman',13,'bold'))
        self.for_class.place(x=435,y=8,width=85,height=40)
        self.for_class.config(state='readonly')
        self.for_class.set('Sleact')



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


        self.tree_vew=ttk.Treeview(self.secound_frame,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18),show='headings',height=11,
        xscrollcommand=self.scrol_bar_y.set,yscrollcommand=self.scrol_bar_x.set,style="mystyle.Treeview")


        self.scrol_bar_x.pack(side=RIGHT,fill=Y)
        self.scrol_bar_y.pack(side=BOTTOM,fill=X)

        self.tree_vew.heading(1,text='First Name')
        self.tree_vew.heading(2,text='Last Name')
        self.tree_vew.heading(3,text='Guardian')
        self.tree_vew.heading(4,text='Phone No')
        self.tree_vew.heading(5,text='Class')
        self.tree_vew.heading(6,text='Roll No')
        self.tree_vew.heading(7,text='Religion')
        self.tree_vew.heading(8,text='Gender')
        self.tree_vew.heading(9,text='D_o_B')
        self.tree_vew.heading(10,text='P_o_B')
        self.tree_vew.heading(11,text='Lact School')
        self.tree_vew.heading(12,text='D_O_A')
        self.tree_vew.heading(13,text='C_A')
        self.tree_vew.heading(14,text='Progress')
        self.tree_vew.heading(15,text='Conduct')
        self.tree_vew.heading(16,text='D_o_L')
        self.tree_vew.heading(17,text='C_L_F')
        self.tree_vew.heading(18,text='R_o_L')

        self.tree_vew.column(1,width=90,anchor=CENTER)
        self.tree_vew.column(2,width=90,anchor=CENTER)
        self.tree_vew.column(3,width=90,anchor=CENTER)
        self.tree_vew.column(4,width=80,anchor=CENTER)
        self.tree_vew.column(5,width=80,anchor=CENTER)
        self.tree_vew.column(6,width=80,anchor=CENTER)
        self.tree_vew.column(7,width=80,anchor=CENTER)
        self.tree_vew.column(8,width=80,anchor=CENTER)
        self.tree_vew.column(9,width=80,anchor=CENTER)
        self.tree_vew.column(10,width=80,anchor=CENTER)
        self.tree_vew.column(11,width=80,anchor=CENTER)
        self.tree_vew.column(12,width=80,anchor=CENTER)
        self.tree_vew.column(13,width=80,anchor=CENTER)
        self.tree_vew.column(14,width=80,anchor=CENTER)
        self.tree_vew.column(15,width=80,anchor=CENTER)
        self.tree_vew.column(16,width=80,anchor=CENTER)
        self.tree_vew.column(17,width=80,anchor=CENTER)
        self.tree_vew.column(18,width=80,anchor=CENTER)


        
        self.tree_vew.place(x=5,y=65,width=1485,height=325)
        self.tree_vew.bind("<ButtonRelease-1>",self.click_inserting)
        self.tree_vew.bind("<Return>",self.click_inserting)
        self.for_class.bind("<<ComboboxSelected>>",self.searching_student)
        self.tree()


    
    
    def tree(self):
        try:
            if self.path == '':
                self.path = filedialog.askopenfilename(title="Slact file to downlode on")
            
            if self.path != '':
                with open(self.path, 'r') as f:
                    lines_ = f.readlines()
                if len(lines_)!=0:
                    lines = []
                    for line in lines_:
                        line = str(line).replace("'",'')
                        line = str(line).replace("\n",'')
                        line = str(line).replace("\\n",'\n')
                        line = str(line).replace("(",'')
                        line = str(line).replace(")",'')
                        line = line.split(',')
                        temp = []
                        if len(line) != 1:
                            for i in line:
                                temp.append(i.replace(' ' , ''))
                            lines.append(temp)
                        
                    self.tree_vew.delete(*self.tree_vew.get_children())
                    for i in lines:
                        self.tree_vew.insert('','end',values=i)
        except:
            messagebox.showerror('Error','Sorry You might have to refrash')
        
    def  add_student(self):
        if  self.enter_first_name.get()=='' or self.enter_last_name.get()=='' or self.enter_father_name.get()=='' or self.enter_Phone_No.get()=='' or self.Class_slaction.get()=='' or self.enter_religion.get()=='' or self.Gender_slaction.get()=='Gender' or self.enter_D_O_B.get()=='' or self.enter_Address.get()==' ' or self.enter_Last_School.get()=='' or self.enter_DOA.get()=='' or self.enter_Class_Admiteddted.get()=='':
            messagebox.showerror('Error!','all fields are require')

        else:
            try:
                if self.path != '':
                    with open(self.path, 'r') as f:
                        lines_ = f.readlines()
                    if len(lines_)!=0:
                        lines = []
                        for line in lines_:
                            line = str(line).replace("'",'')
                            line = str(line).replace("\n",'')
                            line = str(line).replace("\\n",'\n')
                            line = str(line).replace("(",'')
                            line = str(line).replace(")",'')
                            line = line.split(',')
                            temp = []
                            if len(line) != 1:
                                for i in line:
                                    temp.append(i.replace(' ' , ''))
                                lines.append(temp)
                                

                        data_for_insert = [self.enter_first_name.get(),self.enter_last_name.get(),self.enter_father_name.get(),self.enter_Phone_No.get(),self.Class_slaction.get(),self.enter_ID_NO.get(),self.enter_religion.get(),self.Gender_slaction.get(),self.enter_D_O_B.get(),self.enter_Address.get(),self.enter_Last_School.get(),self.enter_DOA.get(),self.enter_Class_Admiteddted.get(),self.enter_Prigres.get(),self.enter_Conduct.get(),self.enter_DOl.get(),self.enter_class_left_from.get(),self.enter_Resion_of_left.get()]
                        lines.append(data_for_insert)

                        with open(self.path, 'w') as r:
                            r.write('\n')
                        
                        for i in lines:
                            with open(self.path, 'a') as t:
                                i = str(i)
                                i = i.replace("'",'')
                                i = i.replace("None",'0')
                                i = i.replace("[",'')
                                i = i.replace("]",'')
                                t.write('\n'+i+'\n')
                                

                        messagebox.showinfo('Success','Student added on Server')
                        self.tree()
            except:
                with open(self.path, 'w')as t:
                    t.write(t)
                messagebox.showerror('Error','there was some issue to save your data please open the file you working with and set it manuly')
            
    
    def update_student(self):
        if  self.enter_first_name.get()=='' or self.enter_last_name.get()=='' or self.enter_father_name.get()=='' or self.enter_Phone_No.get()=='' or self.Class_slaction.get()=='' or self.enter_religion.get()=='' or self.Gender_slaction.get()=='Gender' or self.enter_D_O_B.get()=='' or self.enter_Address.get()==' ' or self.enter_Last_School.get()=='' or self.enter_DOA.get()=='' or self.enter_Class_Admiteddted.get()=='':
            messagebox.showerror('Error!','All Fields are Require')

        else:
            if self.path != '':
                    with open(self.path, 'r') as f:
                        lines_ = f.readlines()
                    if len(lines_)!=0:
                        lines = []
                        for line in lines_:
                            line = str(line).replace("'",'')
                            line = str(line).replace("\n",'')
                            line = str(line).replace("\\n",'\n')
                            line = str(line).replace("(",'')
                            line = str(line).replace(")",'')
                            line = line.split(',')
                            temp = []
                            if len(line) != 1:
                                for i in line:
                                    temp.append(i.replace(' ' , ''))
                                lines.append(temp)
                                

                        data_for_insert = [self.enter_first_name.get(),self.enter_last_name.get(),self.enter_father_name.get(),self.enter_Phone_No.get(),self.Class_slaction.get(),self.enter_ID_NO.get(),self.enter_religion.get(),self.Gender_slaction.get(),self.enter_D_O_B.get(),self.enter_Address.get(),self.enter_Last_School.get(),self.enter_DOA.get(),self.enter_Class_Admiteddted.get(),self.enter_Prigres.get(),self.enter_Conduct.get(),self.enter_DOl.get(),self.enter_class_left_from.get(),self.enter_Resion_of_left.get()]
                        r = []
                        for i in lines:
                            if i[5] == data_for_insert[5]:
                                for c,e in enumerate(data_for_insert):
                                    i[c] = e
                            r.append(i)
                        lines = r


                        with open(self.path, 'w') as r:
                            r.write('\n')
                        
                        for i in lines:
                            with open(self.path, 'a') as t:
                                i = str(i)
                                i = i.replace("'",'')
                                i = i.replace("None",'0')
                                i = i.replace("[",'')
                                i = i.replace("]",'')
                                t.write('\n'+i+'\n')
                                

                        
                        messagebox.showinfo('Success','Student as updated on Server')
                        self.tree()


    
    def delet_student(self):
        if  self.enter_ID_NO.get()=='':
            messagebox.showerror('Error!','Roll No and First Name is are require to delete')
        
        if  self.enter_ID_NO.get()!='':
            if self.path != '':
                    with open(self.path, 'r') as f:
                        lines_ = f.readlines()
                    if len(lines_)!=0:
                        lines = []
                        for line in lines_:
                            line = str(line).replace("'",'')
                            line = str(line).replace("\n",'')
                            line = str(line).replace("\\n",'\n')
                            line = str(line).replace("(",'')
                            line = str(line).replace(")",'')
                            line = line.split(',')
                            temp = []
                            if len(line) != 1:
                                for i in line:
                                    temp.append(i.replace(' ' , ''))
                                lines.append(temp)
                                

                        data_for_insert = [self.enter_first_name.get(),self.enter_last_name.get(),self.enter_father_name.get(),self.enter_Phone_No.get(),self.Class_slaction.get(),self.enter_ID_NO.get(),self.enter_religion.get(),self.Gender_slaction.get(),self.enter_D_O_B.get(),self.enter_Address.get(),self.enter_Last_School.get(),self.enter_DOA.get(),self.enter_Class_Admiteddted.get(),self.enter_Prigres.get(),self.enter_Conduct.get(),self.enter_DOl.get(),self.enter_class_left_from.get(),self.enter_Resion_of_left.get()]
                        r = []
                        for i in lines:
                            if i[5] == data_for_insert[5]:
                                continue
                            r.append(i)
                        lines = r


                        with open(self.path, 'w') as r:
                            r.write('\n')
                        
                        for i in lines:
                            with open(self.path, 'a') as t:
                                i = str(i)
                                i = i.replace("'",'')
                                i = i.replace("None",'0')
                                i = i.replace("[",'')
                                i = i.replace("]",'')
                                t.write('\n'+i+'\n')
                                
                    messagebox.showinfo('Success','Student as delete from Server')
                    self.tree()
        


    def clare_feleds(self):
        self.enter_first_name.delete(0,END)
        self.enter_last_name.delete(0,END)
        self.enter_father_name.delete(0,END)
        self.enter_Phone_No.delete(0,END)
        self.Class_slaction.set('Class')
        self.enter_religion.delete(0,END)
        self.enter_ID_NO.delete(0,END)
        self.Gender_slaction.set('Gender')
        self.enter_D_O_B.delete(0,END)
        self.enter_Address.delete(0,END)
        self.enter_Last_School.delete(0,END)
        self.enter_DOA.delete(0,END)
        self.enter_Class_Admiteddted.delete(0,END)
        self.enter_Prigres.delete(0,END)
        self.enter_Conduct.delete(0,END)
        self.enter_DOl.delete(0,END)
        self.enter_class_left_from.delete(0,END)
        self.enter_Resion_of_left.delete(0,END)
    



    def click_inserting(self,ev):
        self.clare_feleds()
        self.cur_row=self.tree_vew.focus()
        self.content=self.tree_vew.item(self.cur_row)
        self.info=self.content['values']
        if len(self.info)>0:
            self.enter_first_name.insert(0,self.info[0])
            self.enter_last_name.insert(0,self.info[1])
            self.enter_father_name.insert(0,self.info[2])
            self.enter_Phone_No.insert(0,self.info[3])
            self.Class_slaction.set(self.info[4])
            self.enter_ID_NO.insert(0,self.info[5])
            self.enter_religion.insert(0,self.info[6])
            self.Gender_slaction.set(self.info[7])
            self.enter_D_O_B.insert(0,self.info[8])
            self.enter_Address.insert(0,self.info[9])
            self.enter_Last_School.insert(0,self.info[10])
            self.enter_DOA.insert(0,self.info[11])
            self.enter_Class_Admiteddted.insert(0,self.info[12])
            self.enter_Prigres.insert(0,self.info[13])
            self.enter_Conduct.insert(0,self.info[14])
            self.enter_DOl.insert(0,self.info[15])
            self.enter_class_left_from.insert(0,self.info[16])
            self.enter_Resion_of_left.insert(0,self.info[17])
        elif len(self.info)<=0:
            pass

    def searching_student(self):
        if self.for_class.get()!='Sleact' and self.search_entry.get()=='':
            with open(self.path, 'r') as f:
                lines_ = f.readlines()
            if len(lines_)!=0:
                lines = []
                for line in lines_:
                    line = str(line).replace("'",'')
                    line = str(line).replace("\n",'')
                    line = str(line).replace("\\n",'\n')
                    line = str(line).replace("(",'')
                    line = str(line).replace(")",'')
                    line = line.split(',')
                    temp = []
                    if len(line) != 1:
                        for i in line:
                            temp.append(i.replace(' ' , ''))
                        lines.append(temp)
                    
                self.tree_vew.delete(*self.tree_vew.get_children())
                for i in lines:
                    if i[4] == self.for_class.get():
                        self.tree_vew.insert('','end',values=i)
                        

        elif self.Searching_by.get()=='Roll No':
            with open(self.path, 'r') as f:
                lines_ = f.readlines()
            if len(lines_)!=0:
                lines = []
                for line in lines_:
                    line = str(line).replace("'",'')
                    line = str(line).replace("\n",'')
                    line = str(line).replace("\\n",'\n')
                    line = str(line).replace("(",'')
                    line = str(line).replace(")",'')
                    line = line.split(',')
                    temp = []
                    if len(line) != 1:
                        for i in line:
                            temp.append(i.replace(' ' , ''))
                        lines.append(temp)
                    
                self.tree_vew.delete(*self.tree_vew.get_children())
                for i in lines:
                    if i[5] == self.search_entry.get():
                        self.tree_vew.insert('','end',values=i)
                        
        
        elif self.Searching_by.get()=='Name':
            with open(self.path, 'r') as f:
                lines_ = f.readlines()
            if len(lines_)!=0:
                lines = []
                for line in lines_:
                    line = str(line).replace("'",'')
                    line = str(line).replace("\n",'')
                    line = str(line).replace("\\n",'\n')
                    line = str(line).replace("(",'')
                    line = str(line).replace(")",'')
                    line = line.split(',')
                    temp = []
                    if len(line) != 1:
                        for i in line:
                            temp.append(i.replace(' ' , ''))
                        lines.append(temp)
                    
                self.tree_vew.delete(*self.tree_vew.get_children())
                for i in lines:
                    if i[0] == self.search_entry.get():
                        self.tree_vew.insert('','end',values=i)
                        

        elif self.Searching_by.get()=='Contect':
            with open(self.path, 'r') as f:
                lines_ = f.readlines()
            if len(lines_)!=0:
                lines = []
                for line in lines_:
                    line = str(line).replace("'",'')
                    line = str(line).replace("\n",'')
                    line = str(line).replace("\\n",'\n')
                    line = str(line).replace("(",'')
                    line = str(line).replace(")",'')
                    line = line.split(',')
                    temp = []
                    if len(line) != 1:
                        for i in line:
                            temp.append(i.replace(' ' , ''))
                        lines.append(temp)
                    
                self.tree_vew.delete(*self.tree_vew.get_children())
                for i in lines:
                    if i[3] == self.search_entry.get():
                        self.tree_vew.insert('','end',values=i)
        
        else:
            messagebox.showerror('Error','Please Chack Your Input or Slact Correct "Search By!" Option')
    

    def show_all(self):
        self.path = ''
        self.tree()
        self.Searching_by.set('Name')
        self.search_entry.delete(0,END)
        self.for_class.set('Sleact')



if __name__!='__main__':
    from module.defs import *
    
if __name__=='__main__':
    from defs import *
    root = Tk()
    root.title('Sc_Ma_Sy Student_Maniger')
    root.geometry('1530x790+0+0')
    
    root.iconbitmap('LOGOS/main_icon.ico')
    fo=file_opner(in_frame=root)
    root.mainloop()
