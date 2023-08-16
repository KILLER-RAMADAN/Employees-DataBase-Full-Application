from tkinter import messagebox,StringVar,filedialog
from PIL import Image,ImageDraw,ImageFont
import tkinter as tk
from tkinter.ttk import Combobox,Scrollbar
import tkinter.ttk as ttk
from tkinter import Scrollbar
import PIL
from PIL import Image,ImageTk
from db import databsae
import io
import PIL.Image as Image
import sys
import qrcode
import wmi

class employee(tk.Tk):
    
    
    def chack_user(self):
        c=wmi.WMI()
        
        serial=c.Win32_BaseBoard()[0].SerialNumber.strip()
        
        if (serial == "W1KS7BT1020"):
            pass
        else:
            messagebox.showinfo("Denied","Access Denied Thanks For Using Our Program...")
            self.destroy()
    
    def hide_button(self):
        # if  self.hide:
        #     self.hide=False
        #     self.Hide_Table.configure(text="Show")
        #     self.geometry("373x800+600+10")
        #     self.scroll_y.pack(side="bottom",fill="x")
            
        # elif not self.hide:
        #  self.hide=True
        #  self.Hide_Table.configure(text="Hide")
        #  self.geometry("1920x1080+0+0")
        #  self.scroll_y.pack(side="right",fill="y")
        x=messagebox.askyesno("Exit","do you want to exit !?")
        if x:
         sys.exit(0)
    

        
        
    def get_data_from_Table(self,event):
        
        self.focus=self.trev.focus()
        self.contents=self.trev.item(self.focus)
        self.row=self.contents['values']
        self.Id.set(self.row[0])
        self.Name.set(self.row[1])
        self.Jop.set(self.row[2])
        self.Gender.set(self.row[3])
        self.Age.set(self.row[4])
        self.Email.set(self.row[5])
        self.Phone.set(self.row[6])
        self.Address.set(self.row[7])
        self.fetch_data=self.db.add_image(self.Id.get())
        # self.data=self.db.fetche_all()
        # for row in self.data:
        #       self.update()
        #       fp = io.BytesIO(row[8])
              
        #       image = Image.open(fp)
        #       self.image_label=ImageTk.PhotoImage(image)
        #       self.logo.configure(image=self.image_label)
              
   
        
    
    def display_all(self):
        self.trev.delete(*self.trev.get_children())
        self.data=self.db.fetche_all()
        i="images//division.png"
        image = Image.open(i).resize((200,200))
        self.image_label=ImageTk.PhotoImage(image)
        self.logo.configure(image=self.image_label)
        for row in self.data:
            self.trev.insert("","end",values=row)
        
            
    def add_New_employee(self):
      try:
        if self.Id_entry.get()=="" or self.Name_entry.get()=="" or self.Age_entry.get()=="" or self.Phone_entry.get()=="" or self.Email_entry.get()=="" or self.Address_entry.get()=="" or self.Image.get()=="":
            messagebox.showerror("Empty Fields","Enter All Information About Your Employee..")
        else:
            with open(self.Image.get(),"rb") as f:
             self.data=f.read()
            self.db.insert_date(
              self.Id.get(),
              self.Name.get(),
              self.Jop.get(),
              self.Gender.get(),
              self.Age.get(),
              self.Email.get(),
              self.Phone.get(),
              self.Address.get(),
              self.data     
            )        
            self.display_all()
            messagebox.showinfo("Successfully Adding","Successfully Process To Add New Employee...")
            self.clear_details()
      except:
          messagebox.showwarning("Error","This Id Already Used...")
    def clear_details(self):
              self.Id.set(""),
              self.Name.set(""),
              self.Jop.set(""),
              self.Age.set(""),
              self.Email.set(""),
              self.Phone.set(""),
              self.Address.set("")
              self.Image.set("")
              self.Et.set("")
              i="images//division.png"
              image = Image.open(i).resize((200,200))
              self.image_label=ImageTk.PhotoImage(image)
              self.logo.configure(image=self.image_label)
         
    
    def del_em(self):
        if self.Id_entry.get()=="":
              messagebox.showerror("Empty Fields","Enter Id To Remove Your Employee From DataBase..")
              
        else:
            x=messagebox.askyesno("Delete","do you want to delete employee!?")
            if x:
             self.db.remove(self.Id.get())
             self.display_all()
             i="images//division.png"
             image = Image.open(i).resize((200,200))
             self.image_label=ImageTk.PhotoImage(image)
             self.logo.configure(image=self.image_label)
             messagebox.showinfo("Successfully",f"Successfully Process To Remove  Employee...")
           
            
    def edit_employe(self):
        if self.Id_entry.get()=="" or self.Name_entry.get()=="" or self.Age_entry.get()=="" or self.Phone_entry.get()=="" or self.Email_entry.get()=="" or self.Address_entry.get()=="":
            messagebox.showerror("Select Employee","Select Your Employee From The Table To Update His Information....")
        else:
          try:
            with open(self.Image.get(),"rb") as f:
             self.data=f.read()
            self.db.ubdate_data(
              self.Id.get(),
              self.Name.get(),
              self.Jop.get(),
              self.Gender.get(),
              self.Age.get(),
              self.Email.get(),
              self.Phone.get(),
              self.Address.get(),
              self.data
              
            )
         
            self.display_all()
            messagebox.showinfo("Successfully Update","Successfully Update Employee Information ...")
          except:
              messagebox.showerror("Edit Photo","Please Update Employee Photo....")
    def search_about_employee(self):
       if self.Search_entry.get()=="":
           messagebox.showinfo("Empty Field","Enter Information About Your Emplooye in Search Box...")
       else:
            
            self.data=self.db.serche_data(
               self.Ct.get(),
               self.Et.get())
            if self.data:
             messagebox.showinfo("Successfully Update","Successfully Your Employee Found In DataBase...")
             self.trev.delete(*self.trev.get_children())
             self.all_data=self.data
             for row in self.all_data:
              self.trev.insert("","end",values=row)
              img=row[8]
              fp = io.BytesIO(img)
              image = Image.open(fp).resize((180,180))
              self.image_label=ImageTk.PhotoImage(image)
              self.logo.configure(image=self.image_label)
           
            else:
                messagebox.showinfo("Not Found","Employee Not Found In DataBase....")
                self.display_all() 
    def add_image(self):
        self.image_entry.delete(0,1000)
        self.image_file=filedialog.askopenfilename()
        self.image_entry.insert("end",self.image_file)
        self.image_label=ImageTk.PhotoImage(Image.open((self.image_file)).resize((180,180)))
        self.logo.configure(image=self.image_label)
    
    
    
    
    def print_card(self):
       if self.Id_entry.get()=="" or self.Jop_entry.get()=="" or self.Email_entry.get()=="" or self.Name_entry.get()=="":
           messagebox.showerror("Empty Fields","Enter Specific Employee Information..")
      
       else:

        qr=qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
     
         )

        qr.add_data(f"Id: {self.Id_entry.get()}\nName: {self.Name_entry.get()}\nJop: {self.Jop_entry.get()}\nEmail: {self.Email_entry.get()}")
        qr.make(fit=True)
        qr_img=qr.make_image(fill="black",back_color="white")
        qr_img.save(f"qr_images//{self.Id_entry.get()}.png")


        re_qrcode=Image.open(f"qr_images//{self.Id_entry.get()}.png").resize((70,70))
        re_qrcode.save(f"qr_images//{self.Id_entry.get()}.png")
        
        
        self.fetch_data=self.db.add_image(self.Id.get())
        for row in self.fetch_data:
            img=row[8]
            fp = io.BytesIO(img)
            self.image_photo = Image.open(fp).resize((100,100))
            

   

        img=Image.open("cards//card-background.png")
        qrcode_img=Image.open(f"qr_images//{self.Id_entry.get()}.png")
        d=ImageDraw.Draw(img)

        fnt=ImageFont.truetype("micross.ttf",25)

        d.text((50,42),f"{self.Id_entry.get()}",font=fnt ,fill=(0,0,0))

        d.text((82,95),f"{self.Name_entry.get()}",font=fnt ,fill=(0,0,0))
 
        # d.text((0,100),f"Jop: {self.Jop_entry.get()}",font=fnt ,fill=(0,0,0))

        d.text((79,147),f"{self.Email_entry.get()}",font=fnt ,fill=(0,0,0))
        
        img.paste(qrcode_img,(395,115))
        img.paste(self.image_photo,(378,10))
        img.save(f"cards//{self.Id_entry.get()}-Card.png")
        
        messagebox.showinfo("Successfully Process","Employee Card Saved Successfully...")
       
       
       
       
             
    def __init__(self):
        super().__init__()
        
        self.db=databsae("Employee.db")
        
        self.title("Employee-DataBase[Ahmed Ramadan]")
        
        self.geometry("1920x1080")
        
        self.configure(bg="#2c3e50")
        
        
        self.attributes("-topmost",True)
        
        self.attributes("-fullscreen",True)
        
        self.overrideredirect(True)
        
        
        self.hide=True
        
        self.iconbitmap("images//icon.ico")
        
        self.logo_img=ImageTk.PhotoImage(Image.open("images//division.png").resize((200,200)))
        self.back_data_img=ImageTk.PhotoImage(Image.open("images//backup.png").resize((30,30)))
        
        #===============Variables================#
        self.Id=StringVar()
        self.Name=StringVar()
        self.Jop=StringVar()
        self.Email=StringVar()
        self.Phone=StringVar()
        self.Address=StringVar()
        self.Age=StringVar()
        self.Gender=StringVar()
        self.Ct=StringVar()
        self.Et=StringVar()
        self.Image=StringVar()
        #===============Variables================#
        
        #===============Buttons&Entries&Frame================#
        
        
        
        self.bframe=tk.Frame(bg="#1B2631",width=370,height=870)
        
        self.bframe.place(x=0,y=0)
        
        self.logo=tk.Label(self.bframe,image=self.logo_img,bg="#1B2631")
        self.logo.place(x=70,y=690)
        
        self.header_text=tk.Label(self.bframe,fg="white",bg="#1B2631",text="Company Name",font=("calibri",18,"bold"))
        
        self.header_text.place(x=5,y=5)
        
        self.ID_text=tk.Label(self.bframe,fg="white",bg="#1B2631",text="ID",font=("calibri",15,"bold"))
        
        self.ID_text.place(x=5,y=50)
        
        self.Id_entry=tk.Entry(self.bframe,fg="black",textvariable=self.Id,cursor="hand2",justify="center",bg="white",font=("calibri",18))
        
        self.Id_entry.place(x=80,y=50)
        
        self.restore_button=tk.Button(image=self.back_data_img,bg="#1B2631",activebackground="#1B2631",command=self.display_all,bd=0)
        
        self.restore_button.place(x=330,y=50)
        
        
        self.Name_text=tk.Label(self.bframe,fg="white",bg="#1B2631",text="Name",font=("calibri",15,"bold"))
        
        self.Name_text.place(x=5,y=94)
        
        self.Name_entry=tk.Entry(self.bframe,textvariable=self.Name,fg="black",cursor="hand2",justify="center",bg="white",font=("calibri",18))
        
        self.Name_entry.place(x=80,y=95)
        
        
        
        self.Jop_text=tk.Label(self.bframe,fg="white",bg="#1B2631",text="Jop",font=("calibri",15,"bold"))
        
        self.Jop_text.place(x=5,y=144)
        
        self.Jop_entry=tk.Entry(self.bframe,textvariable=self.Jop,fg="black",justify="center",cursor="hand2",bg="white",font=("calibri",18))
        
        self.Jop_entry.place(x=80,y=144)
        
        
        
        self.Gender_text=tk.Label(self.bframe,fg="white",bg="#1B2631",text="Gender",font=("calibri",15,"bold"))
        
        self.Gender_text.place(x=5,y=194)
    
        
        self.gender_combo=ttk.Combobox(values=("Male","Female"),textvariable=self.Gender,state="readonly",justify="left",cursor="hand2",foreground="black",font=("Arial",17),width=10)
        
        self.gender_combo.place(x=80,y=194)
        self.gender_combo.set("Male")
        
        
        self.Age_text=tk.Label(self.bframe,fg="white",bg="#1B2631",text="Age",font=("calibri",15,"bold"))
        
        self.Age_text.place(x=5,y=249)
        
        self.Age_entry=tk.Entry(self.bframe,cursor="hand2",textvariable=self.Age,fg="black",justify="center",bg="white",font=("calibri",18))
        
        self.Age_entry.place(x=80,y=249)
        
        
        self.Email_text=tk.Label(self.bframe,fg="white",bg="#1B2631",text="Email",font=("calibri",15,"bold"))
        
        self.Email_text.place(x=5,y=304)
        
        self.Email_entry=tk.Entry(self.bframe,cursor="hand2",textvariable=self.Email,fg="black",justify="center",bg="white",font=("calibri",18))
        
        self.Email_entry.place(x=80,y=304)
        
        
        self.Phone_text=tk.Label(self.bframe,fg="white",bg="#1B2631",text="Phone",font=("calibri",15,"bold"))
        
        self.Phone_text.place(x=5,y=359)
        
        self.Phone_entry=tk.Entry(self.bframe,cursor="hand2",textvariable=self.Phone,fg="black",justify="center",bg="white",font=("calibri",18))
        
        self.Phone_entry.place(x=80,y=359)
        
        
        
        self.Address_text=tk.Label(self.bframe,fg="white",bg="#1B2631",text="Address",font=("calibri",15,"bold"))
        
        self.Address_text.place(x=5,y=414)
        
        self.Address_entry=tk.Entry(self.bframe,cursor="hand2",textvariable=self.Address,fg="black",justify="center",bg="white",font=("calibri",18))
        
        self.Address_entry.place(x=80,y=414)
        
        self.Search_text=tk.Label(self.bframe,fg="white",bg="#1B2631",text="Search",font=("calibri",15,"bold"))
        
        self.Search_text.place(x=5,y=460)
        
        self.Search_entry=tk.Entry(self.bframe,cursor="hand2",width=10,textvariable=self.Et,fg="black",justify="left",bg="white",font=("calibri",18))
        
        self.Search_entry.place(x=80,y=460)
        
        self.Search_combo=ttk.Combobox(values=("Id","Name","Jop","Gender","Age","Email","Phone","Address"),textvariable=self.Ct,state="readonly",justify="left",cursor="hand2",foreground="black",font=("Arial",17),width=8)
        
        self.Search_combo.place(x=210,y=460)
        self.Search_combo.set("Id")
        
        self.image_text=tk.Label(self.bframe,fg="white",bg="#1B2631",text="Employee Image",font=("calibri",15,"bold"))
        
        self.image_text.place(x=5,y=500)
        
        self.image_entry=tk.Entry(self.bframe,cursor="hand2",width=15,textvariable=self.Image,fg="black",justify="left",bg="white",font=("calibri",18))
        self.image_entry.place(x=5,y=530)
        
        self.Image_file_dialog=tk.Button(self.bframe,text="Add Image",command=self.add_image,width=12,activebackground="#2980b9",activeforeground="white",height=0,font=("celibre",14),bg="#2980b9",fg="white",bd=0)
        
        self.Image_file_dialog.place(x=200,y=530)
        
    
        
        self.searche_info=tk.Button(self.bframe,text="Search",command=self.search_about_employee,width=14,activebackground="#16a085",activeforeground="white",height=1,font=("celibre",16),bg="#16a085",fg="white",bd=0)
        
        self.searche_info.place(x=180,y=5)
        #===============Buttons&Entries&Frame================#
        
        
        
        
        
        #===================Buttons_Frame=====================#
        
        self.button_frame=tk.Frame(self.bframe,bg="white",width=370,relief="solid",height=141,bd=1)
        
        self.button_frame.place(x=0,y=570)
        
        
        self.add_employee=tk.Button(self.button_frame,text="Add Employee",command=self.add_New_employee,width=14,activebackground="#16a085",activeforeground="white",height=1,font=("celibre",16),bg="#16a085",fg="white",bd=0)
        
        self.add_employee.place(x=5,y=5)
        
        
        self.edit_employee=tk.Button(self.button_frame,command=self.edit_employe,text="Edit Employee",width=14,activebackground="#2980b9",activeforeground="white",height=1,font=("celibre",16),bg="#2980b9",fg="white",bd=0)
        
        self.edit_employee.place(x=189,y=5)
        
        
        self.Del_employee=tk.Button(self.button_frame,text="Delete Employee",command=self.del_em,width=14,activebackground="red",activeforeground="white",height=1,font=("celibre",16),bg="red",fg="white",bd=0)
        
        self.Del_employee.place(x=5,y=50)
        
        self.clear_all_details=tk.Button(self.button_frame,text="Clear Details",command=self.clear_details,width=14,activebackground="orange",activeforeground="white",height=1,font=("celibre",16),bg="orange",fg="white",bd=0)
        
        self.clear_all_details.place(x=189,y=50)
        
        
        
        self.print_card_employee=tk.Button(self.button_frame,text="Print Card",command=self.print_card,width=14,activebackground="#11385F",activeforeground="white",height=1,font=("celibre",16),bg="#11385F",fg="white",bd=0)
        
        self.print_card_employee.place(x=5,y=95)
        
        self.Hide_Table=tk.Button(self.button_frame,command=self.hide_button,width=14,activebackground="red",activeforeground="white",height=1,font=("celibre",16),bg="red",fg="white",bd=0)
        
        self.Hide_Table.place(x=189,y=95)
        self.Hide_Table.configure(text="Exit")


        
        
        #===================Buttons_Frame=====================#
        
        
        #======================Table-Frame==================#
        
        self.table_frame=tk.Frame(bg="white",width=1200,height=870)
        self.table_frame.place(x=372,y=0)
        
        
        self.scroll_y=Scrollbar(orient="horizontal",width=0)
        
        style=ttk.Style()
        style.configure("mystile.Treeview",font=("calibri",15),rowhieght=100)
        style.configure("mystile.Treeview.Heading",font=("calibri",15),rowhieght=100)
        self.trev=ttk.Treeview(self.table_frame,columns=(1,2,3,4,5,6,7,8,9),style="mystile.Treeview",yscrollcommand=self.scroll_y)
        self.scroll_y.pack(side="right",fill="y")
        self.trev.bind("<ButtonRelease-1>",self.get_data_from_Table)
        self.trev.heading("1",text="ID")
        self.trev.column("1",width=50)
        self.trev.heading("2",text="Name")
        self.trev.column("2",width=110)
        self.trev.heading("3",text="Jop")
        self.trev.column("3",width=150)
        self.trev.heading("4",text="Gender")
        self.trev.column("4",width=50)
        self.trev.heading("5",text="Age")
        self.trev.column("5",width=50)
        self.trev.heading("6",text="Email")
        self.trev.column("6",width=150)
        self.trev.heading("7",text="Phone")
        self.trev.column("7",width=60)
        self.trev.heading("8",text="Address")
        self.trev.column("8",width=30)
        self.trev.heading("9",text="Image")
        self.trev.column("9",width=30)
        self.trev['show']='headings'
        self.trev.place(x=0,y=0,height=1100,width=1125)
      
        
        
        self.display_all()
        
        self.chack_user()
        


# app=employee()
# app.mainloop()
    
    


