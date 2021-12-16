import os
from tkinter import messagebox
from webbrowser import get
import pymysql
import pymysql

import datetime as dt
import requests
import time
import tempfile



with open('pass.txt','r') as f:
    pass_word = f.read()

log_host='localhost'
log_port=3306
log_user='root'
log_passwd =  pass_word
log_database='school_manigement'



#   -------------------ABOUT SETTING --------------------------

def get_setting(what_to_get):
    try:
        con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd,database=log_database)
        cur=con.cursor()
        cur.execute("Select answer from settings where object=%s",what_to_get)
        row=cur.fetchone()
        con.commit()
        con.close()
        return row[0]
    except:
        pass
    

def save_setting(what_to_save,save_to):
    con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
    cur=con.cursor()
    cur.execute("Update settings set answer=%s where object=%s",(what_to_save,save_to))
    con.commit()
    con.close()
    
# ----------------------------------- ABOUT BACKUP------------------------------------


def downlode(path,class_dwon):   
    con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
    cur=con.cursor()

    if len(path)!=0 or len(path)!='0':

        if class_dwon == 'All Class': 
            cur.execute("Select * from students_info")
            row=cur.fetchall()
            for students in row:
                roll = students[5]
                year = roll[:2]
                students = list(students)
                student = list()
                for i in students:
                    i = str(i)
                    student.append(i.replace(' ','_'))
                student = str(student).replace('\n','\\n')
                student = student.replace("'",'')
                student = student.replace("None",'0')
                student = student.replace("[",'')
                student = student.replace("]",'')
                f = open(f'{path}\studs_{year}.txt', 'a')
                f.write((f"\n{student}\n"))
                f.close()

        if class_dwon != 'All Class':
            cur.execute(f"Select * from students_info where Class={class_dwon}")
            row=cur.fetchall() 
            for students in row:
                roll = students[5]
                year = roll[:2]
                students = list(students)
                student = list()
                for i in students:
                    i = str(i)
                    student.append(i.replace(' ','_'))
                student = str(student).replace('\n','\\n')
                student = student.replace("'",'')
                student = student.replace("None",'0')
                student = student.replace("[",'')
                student = student.replace("]",'')
                f = open(f'{path}\studs__{class_dwon}_{year}.txt', 'a')
                f.write((f"\n{student}\n"))
                f.close()

        cur.execute("Select * from staff_info")
        row=cur.fetchall()

        for staffs in row:
            staff = list(staffs)
            staff = list()
            for i in staffs:
                i = str(i)
                staff.append(i.replace(' ','_'))
            staff = str(staff).replace('\n','\\n')
            staff = staff.replace("'",'')
            staff = staff.replace("None",'0')
            staff = staff.replace("[",'')
            staff = staff.replace("]",'')
            f=open(f'{path}\Staff_info.txt', 'a')
            f.write((f"\n{staff}\n"))
            f.close()

        cur.execute("Select * from settings")
        row=cur.fetchall()

        for Settings in row:
            
            Settings = (f"\n{str(Settings[0]).replace(' ','_')},{str(Settings[1]).replace(' ','_')}\n")
            Settings = str(Settings).replace('\n','')
            Settings = Settings.replace("'",'')
            Settings = Settings.replace("(",'')
            Settings = Settings.replace(")",'')

            f= open(f'{path}\Settings.txt', 'a')
            f.write(f"\n{Settings}\n")
            f.close()
    
    elif len(path)==0 or len(path)=='0':
        con.close()
        messagebox.showerror('Error','Please Chack your Sleacted Path To downlode on!')

    con.close()

def Up_backup_setting(file_name,Path_up):
    con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
    cur=con.cursor()
    try:
        if file_name=='Student File':
            with open(Path_up.get(),'r') as f:
                lines = f.readlines()
            if len(lines)!=0:
                for line in lines:
                    line = str(line).replace("'",'')
                    line = str(line).replace("\n",'')
                    line = str(line).replace("\\n",'\n')
                    line = str(line).replace("(",'')
                    line = str(line).replace(")",'')
                    line = line.split(',')
                    try:
                        if len(line)!= 1 and len(line)==23:
                            line1 = (f"'{line[0].replace('_',' ')}','{line[1].replace('_',' ')}','{line[2].replace('_',' ')}','{line[3].replace('_',' ')}','{line[4].replace('_',' ')}','{line[5].replace('_',' ')}','{line[6].replace('_',' ')}','{line[7].replace('_',' ')}','{line[8].replace('_',' ')}','{line[9].replace('_',' ')}','{line[10].replace('_',' ')}','{line[11].replace('_',' ')}','{line[12].replace('_',' ')}','{line[13].replace('_',' ')}','{line[14].replace('_',' ')}','{line[15].replace('_',' ')}','{line[16].replace('_',' ')}','{line[17].replace('_',' ')}','{line[18].replace('_',' ')}','{line[19].replace('_',' ')}','{line[20].replace('_',' ')}','{line[21].replace('_',' ')}','{line[22].replace('_',' ')}'")
                            cur.execute(f"Insert into students_info (First_Name, Last_Name, Guardian, D_O_B, Roll_No, Gender, Class, Phone_No, religion, Address, Fee_Mounth01, Fee_Mounth02, Fee_Mounth03, Fee_Mounth04, Fee_Mounth05, Fee_Mounth06, Fee_Mounth07, Fee_Mounth08, Fee_Mounth09, Fee_Mounth10, Fee_Mounth11, Fee_Mounth12, Fee_Note) values ({line1})")
                            con.commit()
                    except pymysql.err.IntegrityError:
                        messagebox.showerror('Error',f'Name :({line[0]} {line[1]}) Roll No :({line[4]}) Student is allready in Database')
            else:
                messagebox.showerror('Error','This File is Might Empty or you Sleacted worng File')
            

        elif file_name=='Staff File':
            with open(Path_up.get(),'r') as f:
                lines = f.readlines()
            if len(lines)!=0:
                for line in lines:
                    line = str(line).replace("'",'')
                    line = str(line).replace("\n",'')
                    line = str(line).replace("\\n",'\n')
                    line = str(line).replace("(",'')
                    line = str(line).replace(")",'')
                    line = line.split(',')
                    try:
                        if len(line)!= 1 and len(line)== 10:
                            line2 = (f"'{line[0].replace('_',' ')}','{line[1].replace('_',' ')}','{line[2].replace('_',' ')}','{line[3].replace('_',' ')}','{line[4].replace('_',' ')}','{line[5].replace('_',' ')}','{line[6].replace('_',' ')}','{line[7].replace('_',' ')}','{line[8].replace('_',' ')}','{line[9].replace('_',' ')}'")
                            cur.execute(f"Insert into staff_info (First_Name, Last_Name, Guardian, D_O_B, ID_No, Gender, Subjects, Phone_No, religion, Address) values ({line2})")
                            con.commit()
                    except pymysql.err.IntegrityError:
                            messagebox.showerror('Error',f'Name :({line[0]} {line[1]}) ID No :({line[4]}) Staff is allready in Database')
            else:
                messagebox.showerror('Error','This File is Might Empty or you Sleacted worng File')


        elif file_name=='Settings':
            with open(Path_up.get(),'r') as f:
                lines = f.readlines()
            if len(lines)!=0:
                for line in lines:
                    line = str(line).replace("'",'')
                    line = str(line).replace("\\n",'\n')
                    line = str(line).replace("\n",'')
                    line = str(line).replace("(",'')
                    line = str(line).replace(")",'')
                    line = line.split(',')
                    try:
                        if len(line)!= 1 and len(line)== 2:
                            line3 = (f"'{line[0].replace('_',' ')}','{line[1].replace('_',' ')}'")
                            cur.execute(f"Insert into settings (object, answer) values ({line3})")
                            con.commit()
                    except pymysql.err.IntegrityError:
                            messagebox.showerror('Error',f'({line[0]}/{line[1]}) is allready in Database')

            else:
                messagebox.showerror('Error','This File is Might Empty or you Sleacted worng File')
    except IndexError:
        messagebox.showerror('Error','You Might have Sleacted Wrong File Name \nplease Cheack Which File')
    except FileNotFoundError:
        messagebox.showerror('Error','There is not any File Path to Uplode')



#------------------------------ ABIUT ROLL AND CLASS's------------------------
chois=['All Class','1','2','3','4','5','6','7','8','9','10']
def make_all_zero():
    answer = messagebox.askyesno(title='confirmation',message='Are you Sure to Make ALL \nRoll No Generting Stated From Zero')
    if answer:
        for i in chois:
            save_setting('0',i)


def upgrade_class():
    answer = messagebox.askyesno(title='confirmation',message='Are you Sure Upgrade ALL class To Next Class it is not \ngonna work for Class 10 and Student leven School')
    if answer:
        con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
        cur=con.cursor()
        cur.execute("Select * from students_info")
        row = cur.fetchall()
        for student in row:
            print(str(student[15]))
            B_F_class = str(student[4])

            if int(B_F_class) <= 9 and str(student[15])=='':
                A_F_class = str(int(B_F_class)+1)

            elif int(B_F_class):
                A_F_class = B_F_class

            elif str(student[15])!='':
                A_F_class = B_F_class

            cur.execute("Update students_info set Class=%s where Roll_No=%s",(A_F_class,student[5]))
            con.commit()
            
        con.commit()
        con.close()

def roll_generat(for_class):
    
    con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
    cur=con.cursor()
    cur.execute(f"Select answer from settings where object='{str(for_class)}'")
    row=cur.fetchone()
    con.commit()
    row = str(int(row[0])+1)
    con.close()
    year = dt.date.today()
    year =list(str(year.year))
    year = year[-2]+year[-1]
    if int(for_class) <= 9:
        if int(row) <= 9:
            y = year+'0'+str(for_class)+'0'+row
        elif int(row) >= 10:
            y = year+'0'+str(for_class)+row
    
    elif int(for_class) >= 10:
        if int(row) <= 9:
            y = year+str(for_class)+'0'+row
        elif int(row) >= 10:
            y = year+str(for_class)+row
    return y

# ---------------------------------- ABOUT SMS SENDING ---------------------


def send_sms(API,number,msg,defult_devise,defoult_sim):
    try:
        D_S = str(int(defoult_sim)-1)
        # https://my.zitasms.com/services/send.php?key=b29a9c29335890eecfc2816c1094e2f5145da52c&number=%2B923174010084&message=%28messige%29&devices=85|1
        re = requests.get(f'https://my.zitasms.com/services/send.php?key={API}&number=%2B92{number}&message={msg}&devices={defult_devise}|{D_S}')
        return 'sended'
    except ValueError:
        messagebox.showerror('Error','Please cheack your SMS Settings')
    except requests.exceptions.ConnectionError:
        messagebox.showerror('Error','Please cheack your Internet Conection')

# ------------------------------ ABOUT FEE MANIGMENT -----------------------


mounts = str(get_setting(what_to_get='mounth'))
mounts = mounts.split(',')

school = get_setting('school_name')
school = str(school).split('/n')

def print_fee_form(for_class):
    from fpdf import FPDF
    from datetime import date
    

    class PDF(FPDF):
        def header(self):
            for line in school:
                self.image('LOGOS/school_logo.png', 20, 7, 30)
                self.set_font('helvetica', 'B', 16)
                self.cell(0,6, line,align='C', ln=1)
                pdf.ln(1)
            self.set_font('helvetica', '', 12)
            self.cell(0,6, f'{today}',align='C', ln=1)


        def footer(self):
            self.set_y(-10)

            self.set_font('helvetica', 'BU', 10)
            self.cell(0, 10, f'Page no {self.page_no()}', align='C')            
    con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
    cur=con.cursor()
    cur.execute(f"Select First_Name,Roll_No,Class,Fee_Mounth01,Fee_Mounth02,Fee_Mounth03,Fee_Mounth04,Fee_Mounth05,Fee_Mounth06,Fee_Mounth07,Fee_Mounth08,Fee_Mounth09,Fee_Mounth10,Fee_Mounth11,Fee_Mounth12,D_O_L,C_L_F from students_info where Class={for_class}")
    row=cur.fetchall()
    con.commit()
    con.close()

    def add_line_c():
        pdf.set_font('helvetica', '', 16)
        pdf.cell(0,0, ' ', align='C', border=1, ln=1)



    temp_file = os.path.join(tempfile.gettempdir(), "fee_form_class.pdf")
    today = date.today().strftime("%d/%m/%Y")

    pdf = PDF('P', 'mm', 'Letter')
    pdf.set_auto_page_break(auto=1,margin=-20)

    # adding page
    pdf.add_page()


    pdf.set_font('helvetica', '', 10)
    pdf.cell(0,20, ' ', align='C',ln=1)
    
    # adding lint from add_line_c function 
    add_line_c()

    # defining wirth of coloumns
    w_l = [25,16,12,12,12,12,12,12,12,12,12,12,12,12,12]
    
    pdf.set_font('helvetica', '', 10)

    # ading hader 
    Chart_heder = ['First_Name', 'Roll_No', 'Class']
    for i in mounts:
        Chart_heder.append(i)

    
    for i in range(len(Chart_heder)):
        pdf.cell(w_l[i],10, f'{Chart_heder[i]} |', align='C')
    pdf.ln()

    add_line_c()
    # ading dada to tabel
    for student in row:
        count = 0
        if str(student[15])=='' and str(student[16])=='':
            pdf.set_font('helvetica', '', 10)
            for data in student:
                if count<=len(student)-1:
                    data = str(data).replace('None','0')
                    pdf.cell(w_l[count],6, f'{data}', align='C')
                    if count < len(w_l)-1:
                        count=count+1
    
        pdf.ln()

    pdf.output(temp_file)
    os.system(temp_file)



def print_fee_raside(Stud_data):
    from fpdf import FPDF
    from datetime import date

    class PDF(FPDF):
        def header(self):
            for line in school:
                self.set_font('helvetica', 'B', 16)
                self.cell(89,6, line,align='C')
                center_devider()
                self.set_font('helvetica', 'B', 16)
                self.cell(89,6, line,align='C', ln=1)
                pdf.ln(1)
            
            self.set_font('helvetica', '', 14)
            self.cell(89,6, 'School Copy',align='C')
            center_devider()
            self.set_font('helvetica', '', 14)
            self.cell(89,6, 'Student Copy',align='C', ln=1)
                

            self.cell(89,6, f'{today}',align='C')
            center_devider()
            self.set_font('helvetica', '', 14)
            self.cell(89,6, f'{today}',align='C',ln=1)

            
            

    def add_line_c(wir):
        pdf.set_font('helvetica', '', 16)
        pdf.cell(wir,0, ' ', align='C', border=1, ln=1)

    def center_devider():
        pdf.set_font('helvetica', '', 10)
        pdf.cell(15,7, '|',align='C')


    temp_file = os.path.join(tempfile.gettempdir(), "fee_rased.pdf")
    today = date.today().strftime("%d/%m/%Y")

    pdf = PDF('P', 'mm', 'Letter')
    pdf.set_auto_page_break(auto=1,margin=-20)

    # adding page
    pdf.add_page()
    


    pdf.set_font('helvetica', '', 10)
    add_line_c(0)

    # defining wirth of coloumns
    w_l = [25,16,16,16,16]
    
    pdf.set_font('helvetica', '', 10)

    # ading hader 
    Chart_heder = ('First_Name', 'Roll_No', 'Class', 'Mounth', 'Fee')
    for i in range(len(Chart_heder)):
        pdf.cell(w_l[i],10, f'{Chart_heder[i]} |', align='C')
    center_devider()
    for i in range(len(Chart_heder)):
        pdf.cell(w_l[i],10, f'{Chart_heder[i]} |', align='C')
    

    pdf.ln()
    
    add_line_c(0)
    con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd,database=log_database)
    cur=con.cursor()
    cur.execute(f"Select Fee_Mounth01,Fee_Mounth02,Fee_Mounth03,Fee_Mounth04,Fee_Mounth05,Fee_Mounth06,Fee_Mounth07,Fee_Mounth08,Fee_Mounth09,Fee_Mounth10,Fee_Mounth11,Fee_Mounth12 from students_info where First_Name=%s and Roll_No=%s",(Stud_data[0],Stud_data[1]))
    row=cur.fetchone()
    row = list(row)
    con.commit()
    con.close()
    pdf.set_font('helvetica', '', 10)
    count = 0

    for fee in row:
        if fee != None and fee != '0' and fee != 0:
            if count == 0:
                pdf.cell(w_l[0],8, Stud_data[0], align='C')
                pdf.cell(w_l[1],8, Stud_data[1], align='C')
                pdf.cell(w_l[2],8, Stud_data[2], align='C')
            else:
                pdf.cell(w_l[0],8, ' ', align='C')
                pdf.cell(w_l[1],8, ' ', align='C')
                pdf.cell(w_l[2],8, ' ', align='C')

            fee = str(fee).replace('None','0')
            pdf.cell(w_l[3],8, f'{mounts[count]}', align='C')
            pdf.cell(w_l[4],8, f'{fee}', align='C')

            center_devider()

            if count == 0:
                pdf.cell(w_l[0],8, Stud_data[0], align='C')
                pdf.cell(w_l[1],8, Stud_data[1], align='C')
                pdf.cell(w_l[2],8, Stud_data[2], align='C')
            else:
                pdf.cell(w_l[0],8, ' ', align='C')
                pdf.cell(w_l[1],8, ' ', align='C')
                pdf.cell(w_l[2],8, ' ', align='C')
            pdf.cell(w_l[3],8, f'{mounts[count]}', align='C')
            pdf.cell(w_l[4],8, f'{fee}', align='C')

            pdf.ln()
            
        count=count+1


    total = 0
    for num in row:
        num = int(str(num).replace('None','0'))
        total = total + num
    
    add_line_c(0)
    pdf.ln()
    pdf.set_font('helvetica', '', 10)
    pdf.cell(w_l[0],6, 'Totel :', align='C')
    pdf.cell(w_l[1],6, ' ', align='C')
    pdf.cell(w_l[2],6, ' ', align='C')
    pdf.cell(w_l[3],6, ' ', align='C')
    pdf.cell(w_l[4],6, f'{total}', align='C')

    center_devider()

    pdf.cell(w_l[0],6, 'Totel :', align='C')
    pdf.cell(w_l[1],6, ' ', align='C')
    pdf.cell(w_l[2],6, ' ', align='C')
    pdf.cell(w_l[3],6, ' ', align='C')
    pdf.cell(w_l[4],6, f'{total}', align='C')

    pdf.ln()

    add_line_c(0)

    pdf.output(temp_file)
    os.system(temp_file)


# -----------Calculotor------------------


# ----------------------- school signature ---------------------- 
from tkinter import *
class school_signature:
    
    def __init__(self,frame):

        def time():
            now = dt.datetime.now()
            date_str = now.strftime("%d-%m-%Y")
            time_str = now.strftime("%H:%M:%S %p")

            self.Label_date.config(text=date_str)
                

            self.Label_Time.config(text=time_str)

            self.Label_Time.after(1000, time)


        background_school_logo = 'mediumorchid1'
        self.frame_school_logo=Frame(frame,bg=background_school_logo,relief=FLAT)
        self.frame_school_logo.place(x=10,y=10,width=575,height=330)


        self.logo = PhotoImage(file='LOGOS/school_logo.png')

        self.school_logo = Label(self.frame_school_logo, image = self.logo,bg=background_school_logo)
        self.school_logo.place(x=0,y=0)




        self.hading_label=Label(self.frame_school_logo,text=str(get_setting('school_name')).replace('/n','\n'),fg='white',bg=background_school_logo,font=('Time new roman',20,'bold'))
        self.hading_label.place(x=282,y=25,width=295)




        self.time_frame = Frame(self.frame_school_logo,bg='black')
        self.time_frame.place(x=5,y=260,height=65,width=165)

        self.Label_date=Label(self.time_frame,font=('ds-digital',25,'bold'),bg='black',fg='blue')
        self.Label_date.place(x=82.5,y=15,height=30,anchor='center')

        self.Label_Time=Label(self.time_frame,font=('ds-digital',25,'bold'),bg='black',fg='blue')
        self.Label_Time.place(x=82.5,y=45,height=30,anchor='center')
        time()

if __name__ == '__main__':
    data=['Abdul Wahab', '210901', '9']
    print_fee_raside(Stud_data=data)
    # print_fee_form('9')