from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()

root.title("rating")
root.geometry("1000x700")
# root.update_idletasks()
app = Frame(root)



# buttons
rootWidth = 200
print(rootWidth)
buttons = []
button_states = []
image = Image.open('smileface.png')
image = image.resize((int(rootWidth/5), int(float(image.size[1])*rootWidth/5/float(image.size[0]))))
image2 = Image.open('smileface2.png')
image2 = image2.resize((int(rootWidth/5), int(float(image.size[1])*rootWidth/5/float(image.size[0]))))
click_btn = ImageTk.PhotoImage(image)
click_btn2 = ImageTk.PhotoImage(image2)

def confirm():
    num_group = num_group_entry.get()
    max_score = max_score_entry.get()
    if num_group == "" or max_score == "":
        messagebox.showerror(title="错误提示", message="请将信息填写完整")

    try:
        n = int(num_group)
        m = int(max_score)
        clear_frame()
        display_img(n, m)
    except:
        messagebox.showerror(title="错误提示", message="请确认填写信息均为整数")


def changeColor(cord):
    i,j = cord
    if button_states[i][j] == 1:
        if j==len(buttons[i])-1 or button_states[i][j+1]==0:
            for k in range(len(buttons[i])):
                button_states[i][k] = 0
                buttons[i][k].configure(image=click_btn)
            return
    for k in range(len(buttons[i])):
        button_states[i][k] = 0
        buttons[i][k].configure(image=click_btn)
    for k in range(j + 1):
        button_states[i][k] = 1
        buttons[i][k].configure(image=click_btn2)


def clear_frame():
    for widget in app.winfo_children():
        widget.destroy()


def display_img(n, m):
    if n <= 6:
        for i in range(n):
            frame = Frame(app)
            group = Label(frame, text=f"{i+1} 组", font=('bold', 20), pady=20, padx=40)
            group.pack(side=LEFT)
            buttons.append([])
            button_states.append([])
            for j in range(m):
                b = Button(frame, width=int(rootWidth/5), height=int(float(image.size[1])*rootWidth/5/float(image.size[0])), image=click_btn, command=lambda cord=(i, j): changeColor(cord), borderwidth=0, relief=SUNKEN)
                b.config(activebackground=b.cget('background'))
                b.pack(side=LEFT, padx=5)
                buttons[i].append(b)
                button_states[i].append(0)
                if i == 0:
                    frame.pack(pady=(80,10))
                else:
                    frame.pack(ipady=10)


# max score
max_score_text = StringVar()
max_score_label = Label(app, text="最多分数", font=('bold', 20), pady=10)
max_score_label.pack(padx=100, pady=(80, 0))
max_score_entry = Entry(app, textvariable=max_score_text)
max_score_entry.pack(padx=100)

# num of groups
num_group_text = StringVar()
num_group_label = Label(app, text="组数", font=('bold', 20), pady=10)
num_group_label.pack(padx=100, pady=(70, 0))
num_group_entry = Entry(app, textvariable=num_group_text)
num_group_entry.pack(padx=100)

# confirm button
button = Button(app, text="确认", command=confirm, borderwidth="0",font=('bold', 30), bg="#119c3f", activebackground="green")
button.pack(pady=(120, 0))

app.pack()
root.update_idletasks()

app.mainloop()
