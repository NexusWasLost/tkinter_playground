'''

Create a Tkinter window with the following behavior:

- Layout

A parent frame that fills the window horizontally.

Inside it, place another frame using grid.

- Inner frame requirements

The inner frame must contain 3 columns and 2 rows.

Configure column weights so that:

Column 0 never grows.

Column 1 grows twice as much as column 2.

Only configure what is necessary (don’t over-configure).

- Widgets

Place one button in each cell (total 6 buttons).

Every button must:

Stretch horizontally

NOT stretch vertically

Button text should clearly identify its (row, column) position.

- Resize behavior (this is the real test)

When you resize the window horizontally:

Column 0 stays fixed

Column 1 grows more than column 2

Buttons stretch only as much as their cell allows

No weird gaps, overlaps, or stacking issues

'''

import tkinter as t

def set_geom(window):
    window.geometry("640x480")
    window.title("task")
    return window

def conf_frame(frame):
    frame.columnconfigure(0, weight = 0) # dosent grow
    frame.columnconfigure(1, weight = 2) # grows twice
    frame.columnconfigure(2, weight = 1) # grows half the times of col 1

    frame.rowconfigure(0, weight = 1) # rows grow equally
    frame.rowconfigure(1, weight = 1)
    return frame

window = t.Tk()

window = set_geom(window)

# create a main frame
frame = t.Frame(window)
frame.columnconfigure(0, weight = 1)

# create a sub frame
sub_frame = t.Frame(frame)
sub_frame = conf_frame(sub_frame)


# widgets
_row = 0
_col = 0
count = 1

for _row in range(2):
    
    for _col in range(3):
        btn = t.Button(sub_frame, text = count)
        btn.grid(row = _row, column = _col, sticky = t.E + t.W)
        count += 1
    
sub_frame.grid(row = 0, column = 0, sticky = t.E + t.W) # sticky so that it stretches the only column in frame
frame.pack(padx = 20, pady = 20, fill = 'x')

t.mainloop()
