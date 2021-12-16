
"""
    Coded by  Abdul Wahab
    PhoneNo   +923174010084
    Email     abdulwahabrana47@gmail.com
    Web       codewithawr.epizy.com
    From      Tando_Jan_Muhmmad Sindh Pakistan
"""


from tkinter import ttk
from tkinter.messagebox import askyesno
import pymysql





with open('pass.txt','r') as f:
    pass_word = f.read()

log_host='localhost'
log_port=3306
log_user='root'
log_passwd =  pass_word
log_database='school_manigement'




class Saff_info:
    def __init__(self,in_frame):

        #---------------MAKING-UI---------------#
        
        school_signature(frame=in_frame)



        self.add_new_frame=Frame(in_frame,bg='cyan',relief=FLAT)
        self.add_new_frame.place(x=600,y=10,width=900,height=330)
        
        self.Manage_Saffs_label=Label(self.add_new_frame,text='Manage Saffs Data',font=('Time new roman',20,'bold'),bg='black',fg='white')
        self.Manage_Saffs_label.place(x=0,y=0,width=900)



        self.firstname=Label(self.add_new_frame,text='Fist Name :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.firstname.place(x=20,y=40)

        self.enter_first_name=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_first_name.place(x=20,y=70)

        self.last_name=Label(self.add_new_frame,text='Last Name :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.last_name.place(x=250,y=40)

        self.enter_last_name=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_last_name.place(x=250,y=70)

        
        

        self.father_name=Label(self.add_new_frame,text='Guardian :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.father_name.place(x=480,y=40)

        self.enter_father_name=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_father_name.place(x=480,y=70)


        self.D_O_B=Label(self.add_new_frame,text='D,O,B :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.D_O_B.place(x=20,y=100)

        self.enter_D_O_B=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_D_O_B.place(x=20,y=130)


        self.ID_NO=Label(self.add_new_frame,text='ID No :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.ID_NO.place(x=250,y=100)

        self.enter_ID_NO=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_ID_NO.place(x=250,y=130)




        self.Gender=Label(self.add_new_frame,text='Gender :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.Gender.place(x=480,y=100)

        genders=['Male','Female']
        self.Gender_slaction=ttk.Combobox(self.add_new_frame,values=genders,font=('times nem roman',15,'bold'))
        self.Gender_slaction.place(x=480,y=130,width=205)
        self.Gender_slaction.config(state='readonly')
        self.Gender_slaction.set('Slact Gender')


        self.Subjects=Label(self.add_new_frame,text='Subjects :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.Subjects.place(x=20,y=160)

        
        self.Subjects_slaction=Entry(self.add_new_frame,font=('times nem roman',15,'bold'))
        self.Subjects_slaction.place(x=20,y=190,width=205)
        

        

        self.phone_no=Label(self.add_new_frame,text='Phone No :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.phone_no.place(x=250,y=160)

        self.enter_phone_no=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_phone_no.place(x=250,y=190)

        self.religion=Label(self.add_new_frame,text='Religion :',font=('Times new roman',15,'bold'),bg='cyan',fg='black')
        self.religion.place(x=480,y=160)

        self.enter_religion=Entry(self.add_new_frame,font=('times new roman',15,'bold'))
        self.enter_religion.place(x=480,y=190)


        self.Address=Label(self.add_new_frame,text='Address :',font=('times new roman',15,'bold'),bg='cyan',fg='black')
        self.Address.place(x=20,y=220)

        self.enter_Address=Text(self.add_new_frame,font=('time new roman',15,'bold'),relief=RIDGE)
        self.enter_Address.place(x=20,y=250,width=600,height=60)



        buttoun_X = int(725)



        self.add_button=Button(self.add_new_frame,text='Add',font=('times new roman',17,'bold'),bg='pale green',bd=4,command=self.add_Saff)
        self.add_button.place(x=buttoun_X,y=100,width=110,height=35)

        self.upd_button=Button(self.add_new_frame,text='Update',font=('times new roman',17,'bold'),bg='pale green',bd=4,command=self.update_Saff)
        self.upd_button.place(x=buttoun_X,y=150,width=110,height=35)

        self.delet_button=Button(self.add_new_frame,text='Delete',font=('times new roman',17,'bold'),bg='pale green',bd=4,command=self.delet_Saff)
        self.delet_button.place(x=buttoun_X,y=200,width=110,height=35)

        self.clear_button=Button(self.add_new_frame,text='Clear',font=('times new roman',17,'bold'),bg='pale green',bd=4,command=self.clare_feleds)
        self.clear_button.place(x=buttoun_X,y=250,width=110,height=35)





        self.secound_frame=Frame(in_frame,relief=FLAT,bg='gray')
        self.secound_frame.place(x=10,y=350,width=1510,height=410)


        self.searching_frame=Frame(self.secound_frame,relief=FLAT,bg='firebrick2')
        self.searching_frame.place(x=5,y=5,width=1485,height=85)

        self.searching=Label(self.searching_frame,text='Search for Saff',font=('times new roman',30,'bold'),fg='black',bg='firebrick2')
        self.searching.place(x=0,y=0)

        Searching_optuns=['Name','ID No','Contect']
        self.Searching_by=ttk.Combobox(self.searching_frame,values=Searching_optuns,font=('times nem roman',13,'bold'))
        self.Searching_by.place(x=530,y=8,width=85,height=40)
        self.Searching_by.config(state='readonly')
        self.Searching_by.set('Name')

        self.search_entry=Entry(self.searching_frame,relief=RIDGE,font=('times new roman',25,'bold'),bg='gray77',borderwidth=0)
        self.search_entry.place(x=617.5,y=8,width=300,height=40)

    
        
        self.search_button=Button(self.searching_frame,text='Search',font=('times new roman',15,'bold'),bg='gray95',borderwidth=0,command=self.searching_Saff)
        self.search_button.place(x=918,y=8,height=40)

        

        self.Refrash_button=Button(self.searching_frame,text='Refresh',font=('times new roman',15,'bold'),bg='firebrick3',borderwidth=0,command=self.show_all)
        self.Refrash_button.place(x=1375,y=0,width=110,height=55)


        self.scrol_bar_x=ttk.Scrollbar(self.secound_frame,orient=VERTICAL)
        
        
        self.scrol_bar_y=ttk.Scrollbar(self.secound_frame,orient=HORIZONTAL)

        style = ttk.Style()
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings


        self.tree_vew=ttk.Treeview(self.secound_frame,columns=(1,2,3,4,5,6,7,8,9,10),show='headings',height=11,
        xscrollcommand=self.scrol_bar_y.set,yscrollcommand=self.scrol_bar_x.set,style="mystyle.Treeview")


        self.scrol_bar_x.pack(side=RIGHT,fill=Y)
        self.scrol_bar_y.pack(side=BOTTOM,fill=X)

        self.tree_vew.heading(1,text='First Name')
        self.tree_vew.heading(2,text='Last Name')
        self.tree_vew.heading(3,text='Guardian')
        self.tree_vew.heading(4,text='D_O_B')
        self.tree_vew.heading(5,text='ID No')
        self.tree_vew.heading(6,text='Gender')
        self.tree_vew.heading(7,text='Subjects')
        self.tree_vew.heading(8,text='Contact No')
        self.tree_vew.heading(9,text='Religion')
        self.tree_vew.heading(10,text='Home Adress')

        self.tree_vew.column(1,width=100,anchor=CENTER)
        self.tree_vew.column(2,width=120,anchor=CENTER)
        self.tree_vew.column(3,width=120,anchor=CENTER)
        self.tree_vew.column(4,width=100,anchor=CENTER)
        self.tree_vew.column(5,width=120,anchor=CENTER)
        self.tree_vew.column(6,width=120,anchor=CENTER)
        self.tree_vew.column(7,width=140,anchor=CENTER)
        self.tree_vew.column(8,width=100,anchor=CENTER)
        self.tree_vew.column(9,width=100,anchor=CENTER)
        self.tree_vew.column(10,width=100,anchor=CENTER)

        self.tree_vew.place(x=5,y=65,width=1485,height=325)
        self.tree_vew.bind("<ButtonRelease-1>",self.click_inserting)
        self.tree_vew.bind("<Return>",self.click_inserting)
        self.tree()


    def tree(self):
        try:
            con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
            cur=con.cursor()
            cur.execute("Select * from staff_info")
            self.row=cur.fetchall()
            self.tree_vew.delete(*self.tree_vew.get_children())
            if len(self.row)!=0:
                
                for i in self.row:
                    self.tree_vew.insert('','end',values=i)
            con.commit()
            con.close()
        except:
            pass

                
        
    def  add_Saff(self):
        if  self.enter_first_name.get()=='' or self.enter_last_name.get()=='' or self.enter_father_name.get()=='' or self.enter_D_O_B.get()=='' or self.Gender_slaction.get()=='Slact Gender' or self.Subjects_slaction.get()=='' or self.enter_phone_no.get()=='' or self.enter_religion.get()=='' or self.enter_Address.get(1.0,END)=='':
            messagebox.showerror('Error!','all fields are require')

        else:
            answer = askyesno(title='confirmation',message='Are you Sure to Add new Saff')
            if answer:
                con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
                cur=con.cursor()
                
                data_for_insert = (f"'{self.enter_first_name.get()}','{self.enter_last_name.get()}','{self.enter_father_name.get()}','{self.enter_D_O_B.get()}','{self.enter_ID_NO.get()}','{self.Gender_slaction.get()}','{self.Subjects_slaction.get()}','{self.enter_phone_no.get()}','{self.enter_religion.get()}','{self.enter_Address.get(1.0,END)}'")
                cur.execute(f"Insert into staff_info (First_Name, Last_Name, Guardian, D_O_B, ID_No, Gender, Subjects, Phone_No, religion, Address) values ({data_for_insert})")
                con.commit()
                con.close()
                messagebox.showinfo('Success','Saff added on Server')
                self.tree()
            
    
    def update_Saff(self):
        if  self.enter_first_name.get()=='' or self.enter_last_name.get()=='' or self.enter_father_name.get()=='' or self.enter_D_O_B.get()=='' or self.enter_ID_NO.get()=='' or self.Gender_slaction.get()=='Slact Gender' or self.Subjects_slaction.get()=='Slact Subjects' or self.enter_phone_no.get()=='' or self.enter_religion.get()=='' or self.enter_Address.get(1.0,END)=='':
            messagebox.showerror('Error!','All Fields are Require')

        else:
            answer = askyesno(title='confirmation',
                    message='Are you Sure to Update Saff')
            if answer:
                con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
                cur=con.cursor()
                cur.execute("Update staff_info set First_Name=%s, Last_Name=%s, Guardian=%s, D_O_B=%s, Gender=%s, Subjects=%s, Phone_No=%s, religion=%s, Address=%s where ID_No=%s ",(self.enter_first_name.get(),self.enter_last_name.get(),self.enter_father_name.get(),self.enter_D_O_B.get(),self.Gender_slaction.get(),self.Subjects_slaction.get(),self.enter_phone_no.get(),self.enter_religion.get(),self.enter_Address.get(1.0,END),self.enter_ID_NO.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Saff as updated on Server')
                self.tree()


    
    def delet_Saff(self):
        if  self.enter_ID_NO.get()=='':
            messagebox.showerror('Error!','Roll No is are require ot delete')
        
        else:
            answer = askyesno(title='confirmation',
                    message='Are you Sure to Delete Saff')
            if answer==True:
                con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
                cur=con.cursor()
                cur.execute("Delete from staff_info where (ID_No=%s)",self.enter_ID_NO.get())
                con.commit()
                con.close()
                messagebox.showinfo('Success','Saff as delete from Server')
                self.tree()
        


    def clare_feleds(self):
        self.enter_first_name.delete(0,END)
        self.enter_last_name.delete(0,END)
        self.enter_father_name.delete(0,END)
        self.enter_D_O_B.delete(0,END)
        self.enter_ID_NO.delete(0,END)
        self.Gender_slaction.set('Slact Gender')
        self.Subjects_slaction.delete(0,END)
        self.enter_phone_no.delete(0,END)
        self.enter_religion.delete(0,END)
        self.enter_Address.delete(1.0,END)
    



    def click_inserting(self,ev):
        self.clare_feleds()
        self.cur_row=self.tree_vew.focus()
        self.content=self.tree_vew.item(self.cur_row)
        self.info=self.content['values']
        if len(self.info)>0:
            self.enter_first_name.insert(0,self.info[0])
            self.enter_last_name.insert(0,self.info[1])
            self.enter_father_name.insert(0,self.info[2])
            self.enter_D_O_B.insert(0,self.info[3])
            self.enter_ID_NO.insert(0,self.info[4])
            self.Gender_slaction.set(self.info[5])
            self.Subjects_slaction.insert(0,self.info[6])
            self.enter_phone_no.insert(0,self.info[7])
            self.enter_religion.insert(0,self.info[8])
            self.enter_Address.insert(1.0,self.info[9])
        elif len(self.info)<=0:
            pass



    def searching_Saff(self):
        if self.Searching_by.get()=='ID No':
            con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
            cur=con.cursor()
            cur.execute("Select First_Name, Last_Name, Guardian, D_O_B, ID_No, Gender, Subjects, Phone_No, religion, Address from staff_info where ID_No=%s",self.search_entry.get())
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
            cur.execute("Select First_Name, Last_Name, Guardian, D_O_B, ID_No, Gender, Subjects, Phone_No, religion, Address from staff_info where First_Name=%s",self.search_entry.get())
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
            cur.execute("Select First_Name, Last_Name, Guardian, D_O_B, ID_No, Gender, Subjects, Phone_No, religion, Address from staff_info where Phone_No=%s",self.search_entry.get())
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
        self.Searching_by.set('Name')
        self.search_entry.delete(0,END)

if __name__!='__main__':
    from module.defs import *
    
if __name__=='__main__':
    from defs import *
    root = Tk()
    root.title('Sc_Ma_Sy Saff')
    root.geometry('1530x790+0+0')
    
    root.iconbitmap('LOGOS/main_icon.ico')

    Saff=Saff_info(in_frame=root)
    root.mainloop()