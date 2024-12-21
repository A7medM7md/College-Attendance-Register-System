import AdminPanel
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import csv
import openpyxl
from tkinter import messagebox


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

        say_welcome = tk.Label(
            self.root,
            text=f"Welcome {AdminPanel.username.capitalize()} :)",
            font=("Times New Romans", 19, " bold "),
            fg="#3A6B35",
            bg="#4E87F6",
        )
        say_welcome.place(x=25, y=20)

        self.load_auto_attendance_section()
        self.load_manual_attendance_section()

    def load_auto_attendance_section(self):
        # Automatic Attendance Label #
        auto_attendance_label = tk.Label(
            self.root,
            text="Automatically Fill Attendance",
            font=("times", 19, " bold "),
            fg="#FFFFFF",
            bg="#4E87F6",
        )
        auto_attendance_label.place(x=120, y=150)
        # Subject Messsage and Text Box #
        subject_label = tk.Label(
            self.root,
            text="Enter Subject",
            font=("times", 19, " bold "),
            fg="#4895EF",
            bg="#FFFFFF",
        )
        subject_label.place(x=690, y=300)

        global SUBTXT
        SUBTXT = tk.Entry(
            self.root, bg="#FFFFFF", fg="#4895EF", relief=FLAT,  highlightthickness=1 , font=("times", 25, " bold ")
        )
        SUBTXT.place(x=900, y=300)

        # Fill Attendance Button #
        fill_attendance_button = tk.Button(
            self.root,
            text="Fill Attendance",
            cursor="hand2",
            relief=FLAT,
            font=("times", 15, " bold "),
            fg="#FFFFFF",
            command=self.register,
            bg="#4895EF",
            activebackground="green",
        )
        fill_attendance_button.place(x=910, y=450)

    def load_manual_attendance_section(self):
        # Manually Attendance Label #
        manual_attendance_label = tk.Label(
            self.root,
            text="Manually Fill Attendance",
            font=("times", 19, " bold "),
            fg="#4895EF",
            bg="#FFFFFF",
        )
        manual_attendance_label.place(x=810, y=150)
        # Subject Messsage and Text Box For Automatic #
        subject_label_auto = tk.Label(
            self.root,
            text="Enter Subject",
            font=("times", 19, " bold "),
            fg="#FFFFFF",
            bg="#4E87F6",
        )
        subject_label_auto.place(x=30, y=300)

        SUBTXTA = tk.Entry(
            self.root, bg="#4E87F6", fg="#FFFFFF", relief=FLAT, highlightthickness=1 , font=("times", 25, " bold ")
        )
        SUBTXTA.place(x=240, y=297)
        # Fill Attendance Button For Automatic #
        fill_attendance_button_auto = tk.Button(
            self.root,
            text="Fill Attendance",
            cursor="hand2",
            relief=FLAT,
            font=("times", 15, " bold "),
            fg="#4E87F6",
            bg="#FFFFFF",
            activebackground="green",
        )
        fill_attendance_button_auto.place(x=240, y=450)

        self.root.mainloop()

    # Register Page #
    def register(self):
        self.fill_subject()
        # register_window = tk.Tk()
        register_window = Toplevel(self.root)
        register_window.geometry("800x500")
        register_window.resizable(0, 0)
        register_window.title("Attendance Management System")
        register_window["bg"] = "#00539C"
        # image2 = Image.open("images\\registerPage.png")
        # photo2 = ImageTk.PhotoImage(image2)
        # label2 = Label(register_window, image=photo2)
        # label2.place(x=-2, y=0)

        # ID Messsage and Text Box #
        id_label = tk.Label(
            register_window,
            text="Enter ID",
            width=15,
            fg="black",
            bg="#00539C",
            height=2,
            font=("times", 15, " bold "),
        )
        id_label.place(x=20, y=100)

        global IDTXT
        IDTXT = tk.Entry(
            register_window,
            relief=FLAT,
            highlightthickness =1,
            width=20,
            bg="#00539C",
            fg="white",
            font=("times", 25, " bold "),
        )
        IDTXT.place(x=270, y=105)
        # Name Messsage and Text Box #
        name_label = tk.Label(
            register_window,
            text="Enter Name",
            width=15,
            fg="black",
            bg="#00539C",
            height=2,
            font=("times", 15, " bold "),
        )
        name_label.place(x=20, y=200)

        global NameTXT
        NameTXT = tk.Entry(
            register_window,
            relief=FLAT,
            highlightthickness =1,
            width=20,
            bg="#00539C",
            fg="white",
            font=("times", 25, " bold "),
        )
        NameTXT.place(x=270, y=205)
        # Enter Data Button #
        data_save_button = tk.Button(
            register_window,
            text="Enter Data",
            cursor="hand2",
            command=self.fill_id_name,
            relief=FLAT,
            fg="black",
            bg="white",
            width=19,
            height=1,
            activebackground="green",
            font=("times", 15, " bold "),
        )
        data_save_button.place(x=50, y=360)
        # Convert to Excel Button #
        data_convert_button = tk.Button(
            register_window,
            text="Convert to Excel",
            cursor="hand2",
            command=self.convert_to_excel,
            relief=FLAT,
            fg="black",
            bg="white",
            width=19,
            height=1,
            activebackground="green",
            font=("times", 15, " bold "),
        )
        data_convert_button.place(x=500, y=360)
        # check sheets Button #
        check_sheets_button = tk.Button(
            register_window,
            text="Check Sheets",
            cursor="hand2",
            relief=FLAT,
            fg="black",
            bg="white",
            width=10,
            height=1,
            activebackground="green",
            command= self.check_sheets,
            font=("times", 15, " bold "),
        )
        check_sheets_button.place(x=660, y=456)

        register_window.mainloop()

    # Save Name of Subject on txt file #
    @staticmethod
    def fill_subject():
        file = open("DATA.txt", "a")
        sub = SUBTXT.get()
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

    # Convert txt File To Excel File 3
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

        # window.mainloop()

    def check_sheets(self):
        check_window = tk.Toplevel(self.root)
        check_window.geometry("600x400")
        check_window.title("Check Sheets")

        text_widget = tk.Text(check_window, height=20, width=50) #wrap='word'
        text_widget.pack(padx=20, pady=20)

        with open("DATA.txt", "r") as file:
            content = file.read()
            text_widget.insert("1.0", content)

# function to the window close event #
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        raise SystemExit


# Show Admin Panel #
window = Tk()
AdminPanel.LoginPage(window)
window.protocol("WM_DELETE_WINDOW", on_closing)  # Bind the function to the window close event
window.mainloop()

# Show MainPage #
root = Tk()
app = StudentManagementSystem(root)
root.mainloop()