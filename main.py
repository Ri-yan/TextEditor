import os  # tell about  file directory
import tempfile
from tkinter import *  # this line means that we are importing all the classes and methods present in tkinter module
from tkinter import font, colorchooser, filedialog, messagebox
from tkinter.ttk import *


# functionality part
def toolBarFunc():
    if show_toolbar.get() == False:
        tool_bar.pack_forget()
    if show_toolbar.get() == True:
        textarea.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(fill=X)
        textarea.pack(fill=BOTH, expand=1)
        status_bar.pack()
        show_statusbar.set(True)


def statusbarFunc():
    if show_statusbar.get() == False:
        status_bar.pack_forget()
    else:
        status_bar.pack()


def statusBarFunc(event):
    if textarea.edit_modified():
        word = len(textarea.get(0.0, END).split())
        character = len(textarea.get(0.0, 'end-1c').replace('', ''))
        status_bar.config(text=f'Characters: {character} Words: {word}')
    textarea.edit_modified(False)


url = ''


def new_file():
    global url
    textarea.delete(0.0, END)


def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', 'txt'),
                                                                                             ('All File', '*.*')))
    if url != '':
        data = open(url, 'r')
        textarea.insert(0.0, data.read())
    root.title(os.path.basename(url))


def save_file(event=None):
    if url == '':
        save_url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text Files', 'txt'),
                                                                                          ('All Files', '*.*')))
        if save_url is None:
            pass
        else:
            content = textarea.get(0.0, END)
            save_url.write(content)
            save_url.close()
    else:
        content = textarea.get(0.0, END)
        file = open(url, 'w')
        file.write(content)


def saveas_file(event=None):
    save_url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text Files', 'txt'),
                                                                                      ('All Files', '*.*')))
    content = textarea.get(0.0, END)
    save_url.write(content)
    save_url.close()
    if url != '':
        os.remove(url)


def iexit(event=None):
    if textarea.edit_modified():
        result = messagebox.askyesnocancel('Warning', 'Do you want to save the file')
        if result is True:
            if url != '':
                content = textarea.get(0.0, END)
                file = open(url, 'w')
                file.write(content)
                root.destroy()
            else:
                content = textarea.get(0.0, END)
                save_url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', 'txt'),
                                                                                                  ('All File', '*.*')))
                save_url.write(content)
                save_url.close()
                root.destroy()

        elif result is False:
            root.destroy()

        else:
            pass
    else:
        root.destroy()


def print_out(event=None):
    file = tempfile.mktemp('.txt')
    open(file, 'w').write(textarea.get(1.0, END))
    os.startfile(file, 'print')


fontSize = 12
fontStyle = 'arial'


def font_style(event):
    global fontStyle
    fontStyle = font_family_variable.get()
    textarea.config(font=(fontStyle, fontSize))


def font_size(event):
    global fontSize
    fontSize = size_variable.get()
    textarea.config(font=(fontStyle, fontSize))


def bold_text():
    text_property = font.Font(font=textarea['font']).actual()
    if text_property['weight'] == 'normal':
        textarea.config(font=(fontStyle, fontSize, 'bold'))
    if text_property['weight'] == 'bold':
        textarea.config(font=(fontStyle, fontSize, 'normal'))


def italic_text():
    text_property = font.Font(font=textarea['font']).actual()
    if text_property['slant'] == 'roman':
        textarea.config(font=(fontStyle, fontSize, 'italic'))
    if text_property['slant'] == 'italic':
        textarea.config(font=(fontStyle, fontSize, 'roman'))


def underline_text():
    text_property = font.Font(font=textarea['font']).actual()
    if text_property['underline'] == 0:
        textarea.config(font=(fontStyle, fontSize, 'underline'))
    if text_property['underline'] == 1:
        textarea.config(font=(fontStyle, fontSize,))


def color_select():
    color = colorchooser.askcolor()
    textarea.config(fg=color[1])


def align_left():
    data = textarea.get(0.0, END)
    textarea.tag_config('left', justify=LEFT)
    textarea.delete(0.0, END)
    textarea.insert(INSERT, data, 'left')


def align_right():
    data = textarea.get(0.0, END)
    textarea.tag_config('right', justify=RIGHT)
    textarea.delete(0.0, END)
    textarea.insert(INSERT, data, 'right')


def align_center():
    data = textarea.get(0.0, END)
    textarea.tag_config('center', justify=CENTER)
    textarea.delete(0.0, END)
    textarea.insert(INSERT, data, 'center')


def find():
    textarea.tag_remove('match', 1.0, END)

    def find_word():
        start_pos = 1.0  # line 1 char 0
        word = findentryField.get()
        if word:
            while True:
                start_pos = textarea.search(word, start_pos, stopindex=END)
                if not start_pos:
                    break
                endpos = f'{start_pos}+{len(word)}c'
                textarea.tag_add('match', start_pos, endpos)
                textarea.tag_config('match', foreground='red', background='yellow')
                start_pos = endpos

    def replace_word():
        word = findentryField.get()
        replaceword = replaceentryField.get()
        content = textarea.get(1.0, END)
        new_content = content.replace(word, replaceword)
        textarea.delete(1.0, END)
        textarea.insert(1.0, new_content)

    root1 = Toplevel()
    root1.geometry('450x250+500+200')
    root1.title('Find')
    root1.resizable(0, 0)
    lableFrame = LabelFrame(root1, text='Find/Replace')
    lableFrame.pack(pady=50)
    findLable = Label(lableFrame, text='Find')
    findLable.grid(row=0, column=0, pady=5, padx=5)
    findentryField = Entry(lableFrame)
    findentryField.grid(row=0, column=1, padx=5, pady=5)
    replaceLable = Label(lableFrame, text='Replace')
    replaceLable.grid(row=1, column=0, pady=5, padx=5)
    replaceentryField = Entry(lableFrame)
    replaceentryField.grid(row=1, column=1, padx=5, pady=5)
    findButton = Button(lableFrame, text='Find', command=find_word)
    findButton.grid(row=2, column=0, padx=5, pady=5)
    replaceButton = Button(lableFrame, text='Replace', command=replace_word)
    replaceButton.grid(row=2, column=1, padx=5, pady=5)

    def doSomething():
        textarea.tag_remove('match', 1.0, END)
        root1.destroy()

    root1.protocol('WM_DELETE_WINDOW', doSomething)
    root1.mainloop()


def changeTheme(bg_color, fg_color):
    textarea.config(bg=bg_color, fg=fg_color)


# GUI PART
root = Tk()
root.geometry('1200x620+10+10')
root.title('TextEditor by Mohd Riyan')
root.resizable(0, 0)

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='File', menu=filemenu)
newImage = PhotoImage(file='./assets/new.png')
filemenu.add_command(label='New', accelerator='Ctrl+N', image=newImage, compound=LEFT, command=new_file)
openImage = PhotoImage(file='./assets/open.png')
filemenu.add_command(label='Open', accelerator='Ctrl+O', image=openImage, compound=LEFT, command=open_file)
saveImage = PhotoImage(file='./assets/save.png')
filemenu.add_command(label='Save', accelerator='Ctrl+S', image=saveImage, compound=LEFT, command=save_file)
save_asImage = PhotoImage(file='./assets/save_as.png')
filemenu.add_command(label='Save As', accelerator='Ctrl+Alt+S', image=save_asImage, compound=LEFT, command=saveas_file)

printImage = PhotoImage(file='./assets/printer (1).png')
filemenu.add_command(label='Print', accelerator='Ctrl+P', image=printImage, compound=LEFT, command=print_out)

filemenu.add_separator()
exitImage = PhotoImage(file='./assets/exit.png')
filemenu.add_command(label='Exit', accelerator='Ctrl+Q', image=exitImage, compound=LEFT, command=iexit)

editmenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='Edit', menu=editmenu)
cutImage = PhotoImage(file='./assets/cut.png')
editmenu.add_command(label='Cut', accelerator='Ctrl+N', image=cutImage, compound=LEFT,
                     command=lambda: textarea.event_generate('<Control x>'))
copyImage = PhotoImage(file='./assets/copy.png')
editmenu.add_command(label='Copy', accelerator='Ctrl+O', image=copyImage, compound=LEFT,
                     command=lambda: textarea.event_generate('<Control c>'))
pasteImage = PhotoImage(file='./assets/paste.png')
editmenu.add_command(label='Paste', accelerator='Ctrl+S', image=pasteImage, compound=LEFT,
                     command=lambda: textarea.event_generate('<Control v>'))
editmenu.add_separator()
selectImage = PhotoImage(file='./assets/checked.png')
editmenu.add_command(label='Select All', accelerator='Ctrl+A', image=selectImage, compound=LEFT,
                     command=lambda: textarea.delete(0.0, END))
undoImage = PhotoImage(file='./assets/undo.png')
editmenu.add_command(label='Undo', accelerator='Ctrl+Z', image=undoImage, compound=LEFT,
                     command=lambda: textarea.delete(0.0, END))
redoImage = PhotoImage(file='./assets/redo.png')
editmenu.add_command(label='Select All', accelerator='Ctrl+Y', image=redoImage, compound=LEFT,
                     )
clearImage = PhotoImage(file='./assets/clear_all.png')
editmenu.add_command(label='Clear', accelerator='Ctrl+Alt+S', image=clearImage, compound=LEFT,
                     command=lambda: textarea.delete(0.0, END))
editmenu.add_separator()
findImage = PhotoImage(file='./assets/find.png')
editmenu.add_command(label='Find', accelerator='Ctrl+Q', image=findImage, compound=LEFT, command=find)

show_toolbar = BooleanVar()
show_statusbar = BooleanVar()

viewmenu = Menu(menubar, tearoff=False)
toolbarImage = PhotoImage(file='./assets/tool_bar.png')
viewmenu.add_checkbutton(label='Tool Bar', variable=show_toolbar,
                         onvalue=True, offvalue=False, image=toolbarImage, compound=LEFT, command=toolBarFunc)
show_toolbar.set(True)
statusbarImage = PhotoImage(file='./assets/status_bar.png')
viewmenu.add_checkbutton(label='Status Bar', variable=show_statusbar,
                         onvalue=True, offvalue=False, image=statusbarImage, compound=LEFT, command=statusbarFunc)
show_statusbar.set(True)
menubar.add_cascade(label='View', menu=viewmenu)

theme_choice = StringVar()
thememenu = Menu(menubar, tearoff=False)
LightImage = PhotoImage(file='./assets/light_default.png')
thememenu.add_radiobutton(label='Light Defaut', image=LightImage, compound=LEFT, variable=theme_choice,
                          command=lambda: changeTheme('white', 'black'))
DarkImage = PhotoImage(file='./assets/dark.png')
thememenu.add_radiobutton(label='Dark', image=DarkImage, compound=LEFT, variable=theme_choice,
                          command=lambda: changeTheme('gray20', 'white'))
PinkImage = PhotoImage(file='./assets/red.png')
thememenu.add_radiobutton(label='Pink', image=PinkImage, compound=LEFT, variable=theme_choice,
                          command=lambda: changeTheme('pink', 'blue'))
MonokaiImage = PhotoImage(file='./assets/monokai.png')
thememenu.add_radiobutton(label='Monokai', image=MonokaiImage, compound=LEFT, variable=theme_choice,
                          command=lambda: changeTheme('orange', 'white'))
menubar.add_cascade(label='Theme', menu=thememenu)

tool_bar = Label(root)
tool_bar.pack(side=TOP, fill=X)
font_families = font.families()
font_family_variable = StringVar()
fontfamily_Combobox = Combobox(tool_bar, width=30, values=font_families, state='readonly',
                               textvariable=font_family_variable)
fontfamily_Combobox.current(font_families.index('Arial'))
fontfamily_Combobox.grid(row=0, column=0, padx=5)
fontfamily_Combobox.bind('<<ComboboxSelected>>', font_style)

size_variable = IntVar()
font_size_Combobox = Combobox(tool_bar, width=14,
                              textvariable=size_variable, state='readonly', values=tuple(range(8, 80)))
font_size_Combobox.current(4)
font_size_Combobox.grid(row=0, column=1, padx=5)
font_size_Combobox.bind('<<ComboboxSelected>>', font_size)

boldImage = PhotoImage(file='./assets/bold.png')
boldButton = Button(tool_bar, image=boldImage, command=bold_text)
boldButton.grid(row=0, column=2, padx=5)

italicImage = PhotoImage(file='./assets/italic.png')
italicButton = Button(tool_bar, image=italicImage, command=italic_text)
italicButton.grid(row=0, column=3, padx=5)

underlineImage = PhotoImage(file='./assets/underline.png')
underlineButton = Button(tool_bar, image=underlineImage, command=underline_text)
underlineButton.grid(row=0, column=4, padx=5)

font_colorImage = PhotoImage(file='./assets/font_color.png')
font_colorButton = Button(tool_bar, image=font_colorImage, command=color_select)
font_colorButton.grid(row=0, column=5, padx=5)

leftAlignImage = PhotoImage(file='./assets/left.png')
leftAlignButton = Button(tool_bar, image=leftAlignImage, command=align_left)
leftAlignButton.grid(row=0, column=6, padx=5)

rightAlignImage = PhotoImage(file='./assets/right.png')
rightAlignButton = Button(tool_bar, image=rightAlignImage, command=align_right)
rightAlignButton.grid(row=0, column=7, padx=5)

centerAlignImage = PhotoImage(file='./assets/center.png')
centerAlignButton = Button(tool_bar, image=centerAlignImage, command=align_center)
centerAlignButton.grid(row=0, column=8, padx=5)

scrollBar = Scrollbar(root)
scrollBar.pack(side=RIGHT, fill=Y)
textarea = Text(root, yscrollcommand=scrollBar.set, font=('arial', 12), undo=True)
textarea.pack(fill=BOTH, expand=True)
scrollBar.config(command=textarea.yview)

status_bar = Label(root, text='Status Bar')
status_bar.pack(side=BOTTOM)
textarea.bind('<<Modified>>', statusBarFunc)
root.bind("<Control-o>", open_file)
root.bind("<Control-s>", save_file)
root.bind("<Control-p>", print_out)
root.bind("<Control-Alt-s>", saveas_file)
root.bind("<Control-q>", iexit)

root.mainloop()
