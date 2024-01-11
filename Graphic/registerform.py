from tkinter import*
from tkinter import font
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
screen = Tk()
screen.geometry("800x500")
screen.title("Register Form")
def change_bg_color(color):
    screen.configure(bg=color)
def save_info():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    age_info = age.get()
    age_info = str(age_info)
    print(firstname_info,lastname_info,age_info)

    file = open("user.txt","a")
    file.write("\n"+firstname_info+" ")
    file.write(lastname_info+" ")
    file.write(age_info+" ")
    file.close()
    print("user",firstname_info,"has been registered successfully")

    firstname_entry.delete(0,END)
    lastname_entry.delete(0,END)
    age_entry.delete(0,END)


label_font = font.Font(weight = "bold",family = "Times New Roman",size=15)
heading = Label(text="Welcome to Online Registration!",font=label_font)
heading.place(relx=0.3,rely=0.05)
screen.configure(bg="lightblue")
frame = Frame(screen,width=5,height=5)
frame.pack()
frame.place(anchor=CENTER,relx=0.3,rely = 0.45)
img = ImageTk.PhotoImage(Image.open("1.jpg"))
label = Label(frame,image=img)
label.pack()


label_font = font.Font(weight = "bold",family = "Times New Roman",size=15)
firstname_text = Label(text="Firstname * ",font=label_font)
firstname_text.place(relx=0.6,rely= 0.2)
label_font = font.Font(weight = "bold",family = "Times New Roman",size=15)
lastname_text = Label(text="Lastname * ",font=label_font)
lastname_text.place(relx=0.6,rely=0.4)
label_font = font.Font(weight = "bold",family = "Times New Roman",size=15)
age_text = Label(text="age * ",font=label_font)
age_text.place(relx=0.6,rely=0.6)

firstname = StringVar()
lastname = StringVar()
age = IntVar()

firstname_entry = Entry(textvariable=firstname,width="40")
firstname_entry.place(relx=0.6,rely=0.3)
firstname_entry.config(highlightbackground="blue",highlightthickness="1")
lastname_entry = Entry(textvariable=lastname,width="40")
lastname_entry.place(relx=0.6,rely=0.5)
lastname_entry.config(highlightbackground="blue",highlightthickness="1")
age_entry = Entry(textvariable=age,width="40")
age_entry.place(relx=0.6,rely=0.7)
age_entry.config(highlightbackground="blue",highlightthickness="1")
label_font = font.Font(weight = "bold",family = "Times New Roman",size=10)
register = Button(text="Register",width="10",height="1",font=label_font,command=save_info)
register.place(relx=0.7,rely=0.8)
screen.mainloop()