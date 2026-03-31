import tkinter as gian
window = gian.Tk()
window.title("giana")
window.configure(bg = "light pink")
def register():
    popup = gian.TopLevel(window)
    popup.title(window)
    popup.configure(bg = "light pink")
    uname = gian.label(popup, text = "log in:", font = ("arial", 12, "bold"), bg = "light pink")
    uname.grid(column =0, row = 0, columnspan = 3)
    uname1 = gian.Label(popup)
    
    
    
    
    def log():
        popup=gian.Toplevel(window)
        popup.configure(bg ="light blue")
        register = gian.Label 

label = gian.Label(window, text = "welcome", font = ("times new roman", 20,"bold"), bg = "light blue")
label.pack()
andrei = gian.Button(window, text = "register", font = ("times new roman", 20,"bold"), command = register)
andrei.pack(pady=3)
log= gian.Button(window, text = "log in", font = ("times new roman", 20,"bold"), command = register)

window.mainloop()