import AdminPanel
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import csv
import openpyxl
from tkinter import messagebox
import customtkinter


class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+150+30")
        self.root.resizable(0, 0)
        self.root.title("Attendance Management System")
        self.load_main_page()

    # Main Page Design #
    def load_main_page(self):
        image = Image.open("images\\MainPage.jpg")
        photo = ImageTk.PhotoImage(image)
        label = Label(self.root, image=photo)
        label.place(x=-2, y=0)
        self.load_auto_attendance_section()
        self.load_manual_attendance_section()

#################################################################-

    def load_auto_attendance_section(self):
        # Automatic Attendance Label #
        auto_attendance_label = tk.Label(
            self.root,
            text="Automatically Fill Attendance",
            font=("Century Gothic", 19, " bold "),
            fg="#FFFFFF",
            bg="#4E87F6",
        )
        auto_attendance_label.place(x=120, y=150)

        # Subject Messsage and Text Box #
        global SUBTXTA
        SUBTXTA = customtkinter.CTkEntry(master=self.root,width=400,bg_color='#4E87F6',border_color="#4E87F6" , placeholder_text_color="#4E87F6" , fg_color="#FFFFFF" ,text_color="#4E87F6",placeholder_text="Enter Subject..",font=('Century Gothic', 18),height=45)
        SUBTXTA.place(x=100, y=300)
        
        # Fill Attendance Button For Automatic#
        fill_attendance_button_auto = tk.Button(
            self.root,
            text="Fill Attendance",
            cursor="hand2",
            relief=FLAT,
            font=("Century Gothic", 15, " bold "),
            fg="#4E87F6",
            bg="#FFFFFF",
            activebackground="green",
        )
        fill_attendance_button_auto.place(x=220, y=450)
        

#################################################################

    def load_manual_attendance_section(self):
        # Manually Attendance Label #
        manual_attendance_label = tk.Label(
            self.root,
            text="Manually Fill Attendance",
            font=("Century Gothic", 19, " bold "),
            fg="#4895EF",
            bg="#FFFFFF",
        )
        manual_attendance_label.place(x=810, y=150)

        # Subject Messsage and Text Box For Manual #
        global SUBTXTM
        SUBTXTM = customtkinter.CTkEntry(master=self.root,width=400,bg_color='#FFFFFF' , text_color="#FFFFFF",fg_color="#4895EF" ,placeholder_text_color="#FFFFFF",border_color= '#FFFFFF',placeholder_text="Enter Subject..",font=('Century Gothic', 18),height=45)
        SUBTXTM.place(x=770, y=300)
        
        # Fill Attendance Button For Manual #
        fill_attendance_man = tk.Button(
            self.root,
            text="Fill Attendance",
            cursor="hand2",
            relief=FLAT,
            font=("Century Gothic", 15, "bold"),
            fg="#FFFFFF",
            command=self.register,
            bg="#4895EF",
            activebackground="green",
        )
        fill_attendance_man.place(x=890, y=450)
        
        self.root.mainloop()

#################################################################

    # Register Page #
    def register(self):
        self.fill_subject()
        register_window = Toplevel(self.root)
        register_window.geometry("800x500")
        register_window.resizable(0, 0)
        register_window.title("Attendance Management System")
        reg_image= Image.open("images\\registerPage.png")
        reg_photo = ImageTk.PhotoImage(reg_image)
        label2 = Label(register_window, image=reg_photo)
        label2.place(x=-2, y=0)

        # ID Messsage and Text Box #
        global IDTXT
        IDTXT = customtkinter.CTkEntry(master=register_window,width=350,placeholder_text="Enter ID..",font=('Century Gothic', 18),height=35)
        IDTXT.place(x=388, y=150)

        # Name Messsage and Text Box #
        global NameTXT
        NameTXT = customtkinter.CTkEntry(master=register_window,width=350,placeholder_text="Enter Name..",font=('Century Gothic', 18),height=35)
        NameTXT.place(x=388, y=250)

        #Name of Registaration Subject
        subject = customtkinter.CTkLabel(master=register_window,text=SUBTXTM.get(),bg_color='#3553F4',width=200,font=('PT Bold Heading', 25),height=30)
        subject.place(x=48,y=300)
        
        # Enter Data Button #
        register_button = customtkinter.CTkButton(master=register_window,command=self.fill_id_name,width=120,text="Register", bg_color='#D9D9D9',font=('PT Bold Heading', 15))
        register_button.place(x=350,y=356)

        # Convert to Excel Button #
        convert_to_excel_button = customtkinter.CTkButton(master=register_window,command=self.convert_to_excel,width=120,bg_color='#D9D9D9',text="Convert To Excel",font=('PT Bold Heading', 15))
        convert_to_excel_button.place(x=485,y=356)

        # check sheets Button #
        check_sheets_button = customtkinter.CTkButton(master=register_window,command= self.check_sheets,width=120,text="Check Sheets", bg_color='#D9D9D9',font=('PT Bold Heading', 15))
        check_sheets_button.place(x=660,y=356)

        register_window.mainloop()

#################################################################

    # Save Name of Subject on txt file #
    @staticmethod
    def fill_subject():
        file = open("DATA.txt", "a")
        sub = SUBTXTM.get()
        file.writelines("-" * 10 + "\n" + sub.center(20, "#") + "\n")
        file.writelines("Name" + "\t" + "ID\n")
        file.close()

    # Save Name of Student and his/her ID on txt file #
    @staticmethod
    def fill_id_name():
        file = open("DATA.txt", "a")
        ID = IDTXT.get()
        name = NameTXT.get()
        file.writelines(name + "\t" + ID + "\n")
        file.close()

    # Convert txt File To Excel File #
    @staticmethod
    def convert_to_excel():
        input_file = "DATA.txt"
        output_file = "data.xlsx"

        wb = openpyxl.Workbook()
        ws = wb.worksheets[0]

        with open(input_file, "r") as data:
            reader = csv.reader(data, delimiter="\t")
            for row in reader:
                ws.append(row)
        wb.save(output_file)


    def check_sheets(self):
        check_window = tk.Toplevel(self.root)
        check_window.geometry("600x400")
        check_window.title("Check Sheets")

        text_widget = tk.Text(check_window,height=20, width=50)
        text_widget.pack(padx=20, pady=20)

        with open("DATA.txt", "r") as file:
            content = file.read()
            text_widget.insert("1.0", content)

# function to the window close event #
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        Admin.destroy()
        raise SystemExit


# Show Admin Panel #
Admin = Tk()
AdminPanel.LoginPage(Admin)
Admin.protocol("WM_DELETE_WINDOW", on_closing)  # Bind the function to the window close event
Admin.mainloop()

# Show MainPage #
Main = Tk()
app = StudentManagementSystem(Main)
Main.mainloop()