from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import customtkinter
# # class LoginPage:
# #     def __init__(self, window):
# #         self.window = window
# #         self.window.geometry("1920*1080+150+30")
# #         self.window.resizable(0, 0)
# #         self.window.title("Admin Panel (Attendance Management System)")

# #         # ========================================================================
# #         # ============================background image============================
# #         # ========================================================================
# #         self.bg_frame = Image.open("images\\loginback.jpg")
# #         photo = ImageTk.PhotoImage(self.bg_frame)
# #         self.bg_panel = Label(self.window, image=photo)
# #         self.bg_panel.image = photo
# #         self.bg_panel.pack(fill="both", expand="yes")

def register():
        register_window = Tk()
        register_window.geometry("800x500")
        register_window.resizable(0, 0)
        register_window.title("Attendance Management System")
        # register_window["bg"] = ("#ff9800")
        # register_window.attributes('-alpha',0.9)
        image2 = Image.open("images\\reg.png")
        photo2 = ImageTk.PhotoImage(image2)
        label2 = Label(register_window, image=photo2)
        label2.place(x=-2, y=0)

        # ID Messsage and Text Box #
        id_label = tk.Label(
            register_window,
            text="Enter ID",
            width=15,
            fg="black",
            bg="#00539C",
            height=2,
            font=("light", 15, " bold "),
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
            # command=fill_id_name,
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
            # command=convert_to_excel,
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
            # command= check_sheets,
            font=("times", 15, " bold "),
        )
        check_sheets_button.place(x=660, y=456)

        register_window.mainloop()

# register()



def register():
        
        win = Tk()
        win.geometry("800x500")
        image2 = Image.open("images\\regg.png")
        photo2 = ImageTk.PhotoImage(image2)
        label2 = Label(win, image=photo2)
        label2.place(x=-2, y=0)



        ID = customtkinter.CTkEntry(master=win,width=350,placeholder_text="Enter ID..",font=('PT BOLD HEADING', 18),height=35)
        ID.place(x=388, y=150)

        name = customtkinter.CTkEntry(master=win,width=350,placeholder_text="Enter Name..",font=('PT BOLD HEADING', 18),height=35)
        name.place(x=388, y=250)
        
        # label = Label(win,text="OOP",font="light",bg='#00C2FF')
        # label.place()

        subject = customtkinter.CTkLabel(master=win,text="OOP",bg_color='#3553F4',width=200,font=('PT BOLD HEADING', 18),height=30)
        subject.place(x=48,y=300)

        register_button = customtkinter.CTkButton(master=win,width=120,text="Register", bg_color='#D9D9D9',corner_radius=6,font=('PT BOLD HEADING', 18))
        register_button.place(x=350,y=356)

        convert_to_excel_button = customtkinter.CTkButton(master=win,width=120,bg_color='#D9D9D9',text="Convert To Excel",corner_radius=6,font=('PT BOLD HEADING', 18))
        convert_to_excel_button.place(x=490,y=356)

        check_sheets_button = customtkinter.CTkButton(master=win,width=120,text="Check Sheets", bg_color='#D9D9D9', corner_radius=6,font=('PT BOLD HEADING', 18))
        check_sheets_button.place(x=660,y=356)
        

        win.mainloop()

register()