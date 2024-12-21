from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1280x720+150+30")
        self.window.resizable(0 , 0)
        self.window.title("Login (Attendance Management System)")

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open("images\\light.png")
        photo = ImageTk.PhotoImage(self.bg_frame)# converts the image into a Tkinter-compatible format
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo # prevent the image from being garbage-collected and disappearing
        self.bg_panel.pack(fill="both", expand="yes")
        
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg="#ffffff", width=700, height=720,)
        self.lgn_frame.place(x=260, y=30)

        # ========================================================================
        # ========================================================================
        self.heading = Label(
            self.lgn_frame,
            text="WELCOME BACK...",
            font=("Montserrat", 20, "bold"),
            bg="#ffffff",
            fg="#1762df",
            relief=FLAT,
        )
        self.heading.place(x=-260, y=80, width=800, height=40)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(
            self.lgn_frame,
            text="Login",
            bg="#ffffff",
            fg="#1e1e1e",
            font=("Nunito", 17, "bold"),
        )
        self.sign_in_label.place(x=300, y=160)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(
            self.lgn_frame,
            text="Username",
            bg="#ffffff",
            fg="#1762df",
            font=("yu gothic ui", 13, "bold"),
        )
        self.username_label.place(x=200, y=250)

        self.username_entry = Entry(
            self.lgn_frame,
            highlightthickness=0,
            relief=FLAT,
            bg="#F3F3F3",
            fg="#1e1e1e",
            font=("yu gothic ui ", 12, "bold"),
        )
        self.username_entry.place(x=230, y=290, width=270,height=40)

        self.username_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#1F537C", highlightthickness=0
        )
        self.username_line.place(x=200, y=330)
        # ===== Username icon =========
        self.username_icon = Image.open("images\\username_icon.png")
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg="#ffffff")
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=200, y=300)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open("images\\btn11.png")
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg="#ffffff")
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=200, y=470)
        self.login = Button(
            self.lgn_frame,
            text="LOGIN",
            font=("Nunito", 11, "bold"),
            width=31,
            bd=0,
            bg="#0a7ef5",
            height=1,
            cursor="hand2",
            activebackground="#0a7ef5",
            fg="white",
            command=self.signin,
        )
        self.login.place(x=210, y=480)
        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        self.forgot_button = Button(
            self.lgn_frame,
            text="Forgot Password ?",
            font=("yu gothic ui", 9, "bold underline"),
            fg="#1F537C",
            relief=FLAT,
            activebackground="#ffffff",
            borderwidth=0,
            background="#ffffff",
            cursor="hand2",
        )
        self.forgot_button.place(x=400, y=440)
        # =========== Sign Up ==================================================
        self.sign_label = Label(
            self.lgn_frame,
            text="Not Admin?",
            font=("yu gothic ui", 11, "bold"),
            relief=FLAT,
            borderwidth=0,
            background="#ffffff",
            fg="#1F537C",
        )
        self.sign_label.place(x=200, y=535)

        self.signup_img = ImageTk.PhotoImage(file="images\\register.png")
        self.signup_button_label = Button(
            self.lgn_frame,
            image=self.signup_img,
            bg="#ffffff",
            cursor="hand2",
            borderwidth=0,
            background="#ffffff",
            activebackground="#ffffff",
        )
        self.signup_button_label.place(x=300, y=530, width=111, height=35)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(
            self.lgn_frame,
            text="Password",
            bg="#ffffff",
            fg="#1762df",
            font=("yu gothic ui", 13, "bold"),
        )
        self.password_label.place(x=200, y=350)

        self.password_entry = Entry(
            self.lgn_frame,
            highlightthickness=0,
            relief=FLAT,
            bg="#F3F3F3",
            fg="#1e1e1e",
            font=("yu gothic ui", 12, "bold"),
            show="*",
            insertbackground="#1F537C",
        )
        self.password_entry.place(x=230, y=390, width=270,height=40)

        self.password_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#1F537C", highlightthickness=0
        )
        self.password_line.place(x=200, y=430)
        # ======== Password icon ================
        self.password_icon = Image.open("images\\password_icon.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg="#ffffff")
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=200, y=400)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage(file="images\\show.png")

        self.hide_image = ImageTk.PhotoImage(file="images\\hide.png")

        self.show_button = Button(
            self.lgn_frame,
            image=self.show_image,
            command=self.show,
            relief=FLAT,
            activebackground="white",
            borderwidth=0,
            background="white",
            cursor="hand2",
        )
        self.show_button.place(x=510, y=400)


        # ========= Dark/light mode =====================
        self.light_mode=ImageTk.PhotoImage(file="images\\lightbtn.png")
        
        self.dark_mode=ImageTk.PhotoImage(file="images\\darkbtn.png")

        self.light_button = Button(
            self.lgn_frame,
            image=self.light_mode,
            command=self.light,
            relief=FLAT,
            activebackground="white",
            borderwidth=0,
            background="white",
            cursor="hand2",
        )
        self.light_button.place(x=310,y=610)


    def signin(self):
        global username
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if(username == "admin" and password != "123"):
            LoginPage.show_Warning("Password is incorrect!\nPlease try again.")
        elif(username != "admin" and password == "123"):
            LoginPage.show_Warning("Username is incorrect!\nPlease try again.")
        elif(username == "" and password == ""):
            LoginPage.show_Warning("Please Fill Username and Password field!")
        elif(username != "admin" and password != "123"):
            LoginPage.show_Warning("Username and Password are incorrect!\nPlease try again.")
            
        if username == "admin" and password == "123":
            self.window.destroy()

    def show(self):
        self.hide_button = Button(
            self.lgn_frame,
            image=self.hide_image,
            command=self.hide,
            relief=FLAT,
            activebackground="white",
            borderwidth=0,
            background="white",
            cursor="hand2",
        )
        self.hide_button.place(x=510, y=400)
        self.password_entry.config(show="")


    def hide(self):
        self.show_button = Button(
            self.lgn_frame,
            image=self.show_image,
            command=self.show,
            relief=FLAT,
            activebackground="white",
            borderwidth=0,
            background="white",
            cursor="hand2",
        )
        self.show_button.place(x=510, y=400)
        self.password_entry.config(show="*")


    
    def dark(self):
        self.light_button=Button(
            self.lgn_frame,
            image=self.light_mode,
            command=self.light,
            relief=FLAT,
            activebackground="white",
            borderwidth=0,
            background="white",
            cursor="hand2",
        )
        self.light_button.place(x=310,y=610)
        self.dark_bg_frame= Image.open("images\\light.png")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel.configure(image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill="both", expand="yes")
        self.lgn_frame.configure(bg='white')
        self.heading.configure(bg='white',fg='#0abcec')
        self.sign_in_label.configure(bg='white',fg='black')
        self.username_label.configure(bg="white",fg='#0abcec')
        self.username_entry.configure(bg="#F3F3F3",fg='black')
        self.username_icon_label.configure(bg='white')
        self.lgn_button_label.configure(bg='white',fg='white')
        self.forgot_button.configure(bg="white",fg='#0abcec',activebackground="white")
        self.sign_label.configure(bg="white",fg='#000640')
        self.signup_button_label.configure(bg='white',activebackground="white")
        self.password_label.configure(bg="white",fg='#0abcec')
        self.password_entry.configure(bg="#F3F3F3",fg='black')
        self.password_icon_label.configure(bg='white')
        self.show_button.configure(bg='white')

    def light(self):
        self.dark_button = Button(
            self.lgn_frame,
            image=self.dark_mode,
            command=self.dark ,
            relief=FLAT,
            activebackground="#000640",
            borderwidth=0,
            background="#000640",
            cursor="hand2",
        )
        self.dark_button.place(x=310, y=610) 
        self.dark_bg_frame= Image.open("images\\dark.png")
        dark_photo = ImageTk.PhotoImage(self.dark_bg_frame)
        self.bg_panel.configure(image=dark_photo)
        self.bg_panel.image = dark_photo
        self.bg_panel.pack(fill="both", expand="yes")
        self.lgn_frame.configure(bg='#000640')
        self.heading.configure(bg='#000640',fg='#0abcec')
        self.sign_in_label.configure(bg='#000640',fg='white')
        self.username_label.configure(bg="#000640",fg='#0abcec')
        self.username_entry.configure(bg="#000330",fg='white')
        self.username_icon_label.configure(bg='#000640')
        self.lgn_button_label.configure(bg='#000640',fg='white')
        self.forgot_button.configure(bg="#000640",fg='#0abcec',activebackground="#000640")
        self.sign_label.configure(bg="#000640",fg='white')
        self.signup_button_label.configure(bg='#000640',activebackground="#000640")
        self.password_label.configure(bg="#000640",fg='#0abcec')
        self.password_entry.configure(bg="#000330",fg='white')
        self.password_icon_label.configure(bg='#000640')
        self.show_button.configure(bg='#000640')
        # self.hide_button.configure(bg='#000640')

    @staticmethod
    def show_Warning(msg):
        messagebox.showwarning("warning", msg)

# w=Tk()
# LoginPage(w)
# w.mainloop()