from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font

root = Tk()
root.title("DevSoni Mid Evaluation Word Clone")
#messagebox.showinfo("Welcome to my version of word","This clone has a lot of imperfections and repairs are currently on the way!")

#creating a menu for opening and saving a file
main_menu = Menu(root)
root.config(menu = main_menu)

#function for opening a file
def open_file():
    text_file = filedialog.askopenfilename(initialdir="", title= "Open a file", filetypes=(("Text files", "*.txt"), ))
    new_text_file = open(text_file, 'r')
    stuff = new_text_file.read()
    text_main.insert(END, stuff)
    new_text_file.close()

def new_file():
    messagebox.showinfo("Sorry for the inconvenience","Coming Soon!" )
def save_file():
    messagebox.showinfo("Procedure","To save a file, open an already saved file on your PC, edit that file and the changes can be in the crrently opened file, a better version of this is coming soon!" )
    text_file = filedialog.askopenfilename(initialdir="", title= "Open a file", filetypes=(("Text files", "*.txt"), ))
    new_text_file = open(text_file, 'w')
    new_text_file.write(text_main.get(1.0, END))
def font_family_choose(e):
    present_font.config(family = font_family_listbox.get(font_family_listbox.curselection()))
def font_size_choose(v):
    present_font.config(size = font_size_listbox.get(font_size_listbox.curselection()))
def font_style_choose(v):
    style_choosen = font_style_listbox.get(font_style_listbox.curselection())
    if style_choosen =="Bold":
        present_font.config(weight = "bold")
    elif style_choosen=="Regular":
        present_font.config(weight = "normal", slant = "roman")
        
    elif style_choosen =="Italics":
        present_font.config(slant = "italic")
    elif style_choosen=="Underline":
        present_font.config(underline=1)
#creating a sub_menu for options like open file, save file
file_menu = Menu(main_menu)
main_menu.add_cascade(label="File(Open|Save|New)", menu = file_menu)
file_menu.add_command(label = "Open File", command = open_file)
file_menu.add_separator()
file_menu.add_command(label = "New File", command = new_file)
file_menu.add_separator()
file_menu.add_command(label = "Save File", command = save_file)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)

#present font selection
present_font = font.Font(family= "Helvetica", size = "16")

#creating frames

#layer 1, leftmost frame  , for changing font style and font size
l1_left_frame = LabelFrame(root, text = "", padx=10, pady=10)
l1_left_frame.grid(row = 0, column =0)

#layer 1, middle frame  , fir our text widget
l1_mid_frame = LabelFrame(root, text = "", padx =10, pady=10)
l1_mid_frame.grid(row=0, column=1)

#Main text widget
text_main = Text(l1_mid_frame, width=50,height= 20, font = present_font)
text_main.grid(row = 0, column =0)

#layer 1, right frame   , for bold, italics, underline
l1_right_frame = LabelFrame(root, text = "", padx =10, pady=10)
l1_right_frame.grid(row=0,column=2)
#test button
b1= Button(l1_right_frame, text = "test")
b1.grid(row =0,column =0)


#adding list boxes for font size in left frame layer 1
font_size_label = Label(l1_left_frame, text = "Font Size")
font_size_label.grid(row=0,column=0)

font_size_listbox = Listbox(l1_left_frame, selectmode=SINGLE, width =20)
font_size_listbox.grid(row=1,column =0)

font_sizes = [8,9,10,11,12,14,16,18,20,22,24,26,28,36]
for size in font_sizes:
    font_size_listbox.insert('end',size)

#adding list boxes for font styled in left frame 
font_family_label = Label(l1_left_frame, text = "Font Family")
font_family_label.grid(row=2,column=0)
font_family_listbox = Listbox(l1_left_frame, selectmode=SINGLE, width =20)
font_family_listbox.grid(row=3,column =0)
for f in font.families():
    font_family_listbox.insert('end', f)

#adding bold, italics, underline in right frame
font_style_label = Label(l1_right_frame, text = "Font Style")
font_style_label.grid(row=0,column=0)
font_style_listbox = Listbox(l1_right_frame, selectmode=SINGLE, width =20)
font_style_listbox.grid(row=1,column =0)
font_styles = ["Regular", "Bold", "Italics", "Underline"]
for style in font_styles:
    font_style_listbox.insert('end', style)

#binding listboxes:
font_style_listbox.bind('<ButtonRelease-1>', font_style_choose)
font_family_listbox.bind('<ButtonRelease-1>', font_family_choose)
font_size_listbox.bind('<ButtonRelease-1>', font_size_choose)

root.mainloop()