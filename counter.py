from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')
upload=Image.open(r"C:\\Users\\rajav\\OneDrive\Desktop\\Rakshitha\\app_img.jpg")
image = ImageTk.PhotoImage(upload)
img_label=Label(root,text="Hey user! Welcome to Denomination Counter Application.",
                bg='light blue')
label1= Label(root,
    text="hey User! welcome to Denomination Counter Application.",
    bg='light blue')
label1.place(relx=0.5,y=340,anchor=CENTER)
def msg():
    Msgbox = messagebox.showinfo(
        "Alert","Do you want to calculate the denomination count?")
    if Msgbox == 'ok':
        topwin()
button1 = Button(root,
    text="Let's get started!",
    command=msg,
    bg='brown',
    fg='white')
button1.place(x=260,y=360)
def topwin():
    top = Toplevel(root)
    top.title("Currency Denominatin Counter")
    top.configure(bg='grey')
    top.geometry('600x400')
    label = Label(top,text="Enter amount",bg='grey')
    label.place(x=230,y=50)
    entry = Entry(top)
    entry.place(x=200,y=80)
    lbl = Label(top,
        text="Denominations",
        bg='grey')
    lbl.place(x=140,y=170)
    l1 = Label(top, text="2000",bg='grey')
    l2 = Label(top, text="500",bg='grey') 
    l3 = Label(top, text="100",bg='grey')
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
def topwin():
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    def calculate():
        try:
            amount = int(entry.get())
            note2000 = amount // 200
            amount%=2000
            note500 = amount // 500
            amount%=500
            note100 = amount // 100
            t1.insert(0, note2000)
            t2.insert(0, note500)
            t3.insert(0, note100)
        except:
            messagebox.showerror("Error","Enter valid number")
    btn = Button(top,
        text="Calculate",
        command=calculate,
        bg='brown',
        fg='white')
    btn.place(x=240, y=120)
root.mainloop()
    

    
    


