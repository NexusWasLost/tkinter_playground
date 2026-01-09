import tkinter as t

window = t.Tk()

window.geometry("640x480")
window.title("My tt window")

label = t.Label(window, text = "Hey from Window !", font = ("Arial", 16))
label.pack(padx = 20, pady = 20)

# kind of like a parent div
btnFrame = t.Frame(window)
btnFrame.columnconfigure(0, weight = 1) #column 1
btnFrame.columnconfigure(1, weight = 1) #column 2
btnFrame.columnconfigure(2, weight = 1) #column 3

count = 1
_row = 0
_col = 0

#3 rows and 3 columns of buttons
for _row in range(3):
    for _col in range(3):
        btn = t.Button(btnFrame, text = count)
        btn.grid(row = _row, column = _col, sticky = t.E + t.W)
        count += 1

btnFrame.pack(padx = 60, pady = 20, fill = 'x')

window.mainloop()

