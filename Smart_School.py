
"""
    Coded by:  Abdul Wahab Rana
    PhoneNo :  +923174010084
    Email   :  abdulwahabrana47@gmail.com
    Web     :  codewithawr.epizy.com
    From    :  Tando_Jan_Muhmmad Sindh Pakistan
"""

from module.F_M import Fee_manigment
from module.S_M import Student_info
from module.Staff_M import Saff_info
from module.SMS_sander import SMS_sender


from module.defs import *



import webbrowser
import time
from tkinter import filedialog, ttk



with open('pass.txt','r') as f:
    pass_word = f.read()

log_host='localhost'
log_port=3306
log_user='root'
log_passwd =  pass_word
log_database='school_manigement'



def center(win,ISloding):

    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    if ISloding == True:
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
    elif ISloding == False:
        x = win.winfo_screenwidth() // 2 - win_width // 2 
        y = win.winfo_screenheight() // 2 - win_height // 2 -32
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()



def basic():

    
    def hover1(ev):
        entre_format1.config(text='for new line add /n')
    def hover2(ev):
        entre_format2.config(text="add ',' for next mounth")
    def hover_leve1(ev):
        entre_format1.config(text='')
    def hover_leve2(ev):
        entre_format2.config(text='')
    
    def refrash():
        school_name = get_setting('school_name')
        mounth = get_setting('mounth')

        sch_etry.delete(0,END)
        mounth_entry.delete(0,END)

        sch_etry.insert(0,school_name)
        mounth_entry.insert(0,mounth)
            
    def save_basic():
        school_name = sch_etry.get()
        mounth = mounth_entry.get()

        save_setting(what_to_save=school_name,save_to='school_name')
        save_setting(what_to_save=mounth,save_to='mounth')


    setting_windo = Toplevel()
    setting_windo.title('Basic Setting')
    setting_windo.geometry('500x200+0+0')
    setting_windo.iconbitmap('LOGOS/main_icon.ico')
    setting_windo.resizable(False, False)
    setting_windo.attributes('-topmost',True)
    center(setting_windo,True)

    sch_label = Label(setting_windo,text='School Name :',fg='black',font=('',15,'bold'))
    sch_label.place(x=20,y=10)

    sch_etry = Entry(setting_windo,font=('',15,''))
    sch_etry.place(x=20,y=40,width=450)

    entre_format1 = Label(setting_windo,text='',font=('times new roman',10,'bold'))
    entre_format1.place(x=20,y=65,height=20)


    sch_etry.bind("<Enter>",hover1)
    sch_etry.bind("<Leave>",hover_leve1)

    

    mounth_label = Label(setting_windo,text='Mounth List :',fg='black',font=('',15,'bold'))
    mounth_label.place(x=20,y=90)

    mounth_entry = Entry(setting_windo,font=('',15,''))
    mounth_entry.place(x=20,y=120,width=450)

    entre_format2 = Label(setting_windo,text='',font=('times new roman',10,'bold'))
    entre_format2.place(x=20,y=145,height=20)

    mounth_entry.bind("<Enter>",hover2)
    mounth_entry.bind("<Leave>",hover_leve2)

    refrash_button = Button(setting_windo, text='Refrash',font=('times roman',15,''), bg='white', command=refrash)
    refrash_button.place(x=315,y=160)

    save_button = Button(setting_windo, text='Save',font=('times roman',15,''), bg='white', command=save_basic)
    save_button.place(x=420,y=160)


    refrash()

    



def api_setting():
    def open_url(url):
        webbrowser.open_new_tab(url)
    
    def insertng():
        api_entry.delete(0,END)
        defoult_devise.delete(0,END)

        api_entry.insert(0,get_setting(what_to_get='api'))
        Defoult_sim.set(get_setting(what_to_get='defoult_sim'))
        defoult_devise.insert(0,get_setting(what_to_get='defoult_devise'))

    def seving():
        save_setting(what_to_save=api_entry.get(),save_to=('api'))

        save_setting(what_to_save=Defoult_sim.get(),save_to=('defoult_sim'))

        save_setting(what_to_save=defoult_devise.get(),save_to=('defoult_devise'))
    


    
    setting_windo = Toplevel()
    setting_windo.title('API Setting')
    setting_windo.geometry('500x200+0+0')
    setting_windo.iconbitmap('LOGOS/main_icon.ico')
    setting_windo.resizable(False, False)
    setting_windo.attributes('-topmost',True)
    center(setting_windo,True)


    label1 = Label(setting_windo,text='API form zitasms.com :',fg='black',font=('',15,'bold'))
    label1.place(x=20,y=10)

    label2 = Label(setting_windo,text='zitasms.com',fg='blue',font=('',15,'bold'))
    label2.place(x=105,y=10)
    label2.bind('<Button-1>',lambda e:open_url('https://www.zitasms.com'))


    api_entry = Entry(setting_windo,font=('',15,''))
    api_entry.place(x=20,y=40,width=450)



    label2 = Label(setting_windo,text='Defoult SIM :',font=('',15,'bold'))
    label2.place(x=20,y=95)

    classes=['1','2']
    Defoult_sim=ttk.Combobox(setting_windo,values=classes,font=('times nem roman',15,''))
    Defoult_sim.place(x=150,y=97,width=60)
    Defoult_sim.config(state='readonly')
    Defoult_sim.set(get_setting(what_to_get='defoult_sim'))


    label2 = Label(setting_windo,text='Defoult Devise :',font=('',15,'bold'))
    label2.place(x=222,y=95)

    defoult_devise = Entry(setting_windo,font=('',15,''))
    defoult_devise.place(x=380,y=97,width=90)


    refrash_button = Button(setting_windo,text='Refrash',bg='white',font=('',13,'bold'),command=insertng)
    refrash_button.place(x=200,y=160,width=70)

    cancil_button = Button(setting_windo,text='Cancel',bg='white',font=('',13,'bold'),command=setting_windo.destroy)
    cancil_button.place(x=290,y=160,width=70)

    save_button = Button(setting_windo,text='Ok',bg='white',font=('',13,'bold'),command=seving)
    save_button.place(x=380,y=160,width=70)
    insertng()


def backup_setting():
    def takinpath(fileorfolder):
        if fileorfolder == 'file':
            path = filedialog.askopenfilename(title="Slact file to downlode on")
            Path_up_entry.delete(0,END)
            Path_up_entry.insert(0,path)

        elif fileorfolder == 'folder':
            path = filedialog.askdirectory(title='Slact path to downlode on')
            Path_down_entry.delete(0,END)
            Path_down_entry.insert(0,path)
        return path
    

    setting_windo = Toplevel()
    setting_windo.title('Backup Setting')
    setting_windo.geometry('500x200+0+0')
    setting_windo.iconbitmap('LOGOS/main_icon.ico')
    setting_windo.resizable(False,False)
    setting_windo.attributes('-topmost',True)
    center(setting_windo,True)

    
    label1 = Label(setting_windo,text='Sleact Path to Downlode files :',font=('',15,'bold'))
    label1.place(x=20,y=10)

    Path_down_entry = Entry(setting_windo,font=('',15,''))
    Path_down_entry.place(x=20,y=40,width=300)

    Path_down_button = Button(setting_windo,bg='cyan',text='...',font=('',15,''),borderwidth=1,command=lambda : takinpath(fileorfolder='folder'))
    Path_down_button.place(x=320,y=40,height=27)

    Up_backup_setting
    chois=['All Class','1','2','3','4','5','6','7','8','9','10']
    sleact_to_down=ttk.Combobox(setting_windo,values=chois)
    sleact_to_down.place(x=375,y=35,width=100,height=27)
    sleact_to_down.config(state='readonly')
    sleact_to_down.set('All Class')


    Path_down_button = Button(setting_windo,bg='light green',text='DOWNLODE',font=('',15,''),borderwidth=1,command=lambda : downlode(path=Path_down_entry.get(),class_dwon=sleact_to_down.get()))
    Path_down_button.place(x=360,y=72)



    label2 = Label(setting_windo,text='Sleact File Path to Uplode :',font=('',15,'bold'))
    label2.place(x=20,y=100)

    Path_up_entry = Entry(setting_windo,font=('',15,''))
    Path_up_entry.place(x=20,y=130,width=300)

    
    Path_up_button = Button(setting_windo,bg='cyan',text='...',font=('',15,''),borderwidth=1,command=lambda : takinpath(fileorfolder='file'))
    Path_up_button.place(x=320,y=130,height=27)

    
    chois=['Student File','Staff File','Settings']
    sleact_to_uplode=ttk.Combobox(setting_windo,values=chois)
    sleact_to_uplode.place(x=375,y=120,width=100,height=27)
    sleact_to_uplode.config(state='readonly')
    sleact_to_uplode.set('Student File')


    Path_down_button = Button(setting_windo,bg='light green',text='UPLODE',font=('',15,''),borderwidth=1,command=lambda : Up_backup_setting(sleact_to_uplode.get(),Path_up_entry))
    Path_down_button.place(x=360,y=160,width=131)



def Roll_setting():
    

    setting_roll_windo = Toplevel()
    setting_roll_windo.title('Eidit Roll Stated From')
    setting_roll_windo.geometry('500x300+0+0')
    setting_roll_windo.iconbitmap('LOGOS/main_icon.ico')
    setting_roll_windo.resizable(False,False)
    setting_roll_windo.attributes('-topmost',True)
    
    center(setting_roll_windo,True)
    

    

    def inserting(ev):
        roll_entry_eidit.delete(0,END)
        roll_entry_eidit.insert(0,get_setting(sleact_to_show.get()))


    def seving():
        if sleact_to_show.get()!='Sleact Class' and roll_entry_eidit.get()!='':
            save_setting(roll_entry_eidit.get(),sleact_to_show.get())

        elif sleact_to_show.get()=='Sleact Class' and roll_entry_eidit.get()=='':
            messagebox.showerror('Error','You Moust Sleact Class and make Some change and then Save')



    label2 = Label(setting_roll_windo,text='Eidit Where next Roll Gnerated \nfor each Class',font=('',17,'bold'))
    label2.place(x=10,y=10)

    label1 = Label(setting_roll_windo,text='Select Class :',font=('times new roman',15,'bold'))
    label1.place(x=10,y=70)


    chois=['1','2','3','4','5','6','7','8','9','10']
    sleact_to_show=ttk.Combobox(setting_roll_windo,values=chois,font=('',12,''))
    sleact_to_show.place(x=10,y=105,width=100,height=27)
    sleact_to_show.config(state='readonly')
    sleact_to_show.set('Sleact Class')

    label2 = Label(setting_roll_windo,text='Eidit :',font=('times new roman',15,'bold'))
    label2.place(x=150,y=70)

    roll_entry_eidit = Entry(setting_roll_windo,font=('',12,''))
    roll_entry_eidit.place(x=150,y=105,width=100,height=27)

    sleact_to_show.bind('<<ComboboxSelected>>',inserting)

    

    updrate_class = Button(setting_roll_windo,text='Upgrate Class',font=('times new roman',13,'bold'),bg='pale green',command=upgrade_class)
    updrate_class.place(x=350,y=80,height=40)


    make_zero_button = Button(setting_roll_windo,text='Make All Zero',font=('times new roman',13,'bold'),bg='pale green',command=make_all_zero)
    make_zero_button.place(x=350,y=130,height=40)



    seve_button = Button(setting_roll_windo,text='Save',font=('times new roman',15,'bold'),bg='white',command=seving)
    seve_button.place(x=400,y=250,height=40)

    make_zero_button = Button(setting_roll_windo,text='Cancel',font=('times new roman',15,'bold'),bg='white',command=lambda :setting_roll_windo.destroy())
    make_zero_button.place(x=265,y=250,height=40)


root = Tk()
root.title('Smart School')
root.geometry('1530x790+0+0')
root.resizable(False, False)
root.overrideredirect(True)


root.iconbitmap('LOGOS/main_icon.ico')

center(root,False)



def main():
    
    center(lodint_frame,False)
    def on_closing():
        for widget in root.winfo_children():
            if isinstance(widget, Toplevel):
                widget.destroy()
        root.destroy()



    menubar = Menu(root)
    root.config(menu=menubar)

    menu = Menu(menubar, tearoff="off")

    menubar.add_cascade(label="File",menu=menu)

    menu.add_command(label='Exit',command=root.destroy)


    

    setting_menu = Menu(menubar, tearoff="off")

    menubar.add_cascade(label="Setting",menu=setting_menu)


    setting_menu.add_cascade(label='Basics Setting',command=basic)

    setting_menu.add_cascade(label='Gnarat Roll-No',command=Roll_setting)



    API_seb_menu = Menu(menubar, tearoff="off")

    setting_menu.add_command(label='SMS-Setting',command=api_setting)


    backup_seb_menu = Menu(menubar, tearoff="off")

    setting_menu.add_command(label='Backup',command=backup_setting)
        
    tabs = ttk.Notebook(root)
    tabs.place(x=0,y=0)

    tabe1 = Frame(tabs,width=1530,height=790)
    tabe2 = Frame(tabs,width=1530,height=790)
    tabe3 = Frame(tabs,width=1530,height=790)
    tabe4 = Frame(tabs,width=1530,height=790)

    tabe1.place()
    tabe2.place()
    tabe3.place()
    tabe4.place()

    tabs.add(tabe1,text='Student Manigment')
    tabs.add(tabe2,text='Fee Manigment')
    tabs.add(tabe3,text='Staff Manigment')
    tabs.add(tabe4,text='Seand SMS')



    s_m = Student_info(in_frame=tabe1)
    f_M = Fee_manigment(in_frame=tabe2)
    staff_m = Saff_info(in_frame=tabe3)
    sms = SMS_sender(in_frame=tabe4)
    lodint_frame.attributes('-topmost',False)
    



    root.protocol("WM_DELETE_WINDOW", on_closing)
def temp1():
    main()
    center(root,False)
    lodint_frame.attributes('-topmost',True)
    
    lodint_frame.attributes('-topmost',False)
    
    
    

lodint_frame = Toplevel()
lodint_frame.geometry('1530x825+0+0')
lodint_frame.resizable(False, False)
lodint_frame.overrideredirect(True)
lodint_frame.configure(background='black')

center(lodint_frame,False)


cn = Canvas(lodint_frame,width=1530,height=825)
cn.pack(expand=True)



bg_logo = PhotoImage(file='LOGOS/bg.png')

cn.create_image(0,0,image=bg_logo,anchor='nw')


sof_logo = PhotoImage(file='LOGOS/Logo_ading.png')

cn.create_image(765,370,image=sof_logo)






progress = ttk.Progressbar(lodint_frame, orient = HORIZONTAL,length = 805, mode = 'determinate')


devi = 4
def bar():
    de = 0
    for i in range(devi):
        progress['value'] = de+100//devi
        root.update_idletasks()
        de = de + 100//devi
        if de != 100:
            time.sleep(1)
  
progress.place(x=361,y=640)
lodint_frame.after(500,bar)

def temp():
    lodint_frame.destroy()
    root.overrideredirect(False)
    
    try:
        con = pymysql.connect(host=log_host,port=log_port,user=log_user,passwd=log_passwd, database=log_database)
        con.close()
    except:
        messagebox.showerror('Error','Cant find MYsql DataBase')

    
    
lodint_frame.after(devi*1000,temp)
root.after(devi//2,temp1)
lodint_frame.mainloop()




