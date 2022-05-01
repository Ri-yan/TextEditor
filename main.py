from tkinter import *  # this line means that we are importing all the classes and methods present in tkinter module
from tkinter.ttk import *
from tkinter import  font
root = Tk()
root.geometry('1200x620+10+10')
root.title('TextEditor by Mohd Riyan')
root.resizable(0, 0)

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='File', menu=filemenu)
newImage = PhotoImage(file='./assets/new.png')
filemenu.add_command(label='New', accelerator='Ctrl+N', image=newImage, compound=LEFT)
openImage = PhotoImage(file='./assets/open.png')
filemenu.add_command(label='Open', accelerator='Ctrl+O', image=openImage, compound=LEFT)
saveImage = PhotoImage(file='./assets/save.png')
filemenu.add_command(label='Save', accelerator='Ctrl+S' , image=saveImage, compound=LEFT)
save_asImage = PhotoImage(file='./assets/save_as.png')
filemenu.add_command(label='Save As', accelerator='Ctrl+Alt+S' , image=save_asImage, compound=LEFT)
filemenu.add_separator()
exitImage = PhotoImage(file='./assets/exit.png')
filemenu.add_command(label='Exit',accelerator='Ctrl+Q', image=exitImage, compound=LEFT)

editmenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='Edit', menu=editmenu)
cutImage = PhotoImage(file='./assets/cut.png')
editmenu.add_command(label='Cut', accelerator='Ctrl+N', image=cutImage, compound=LEFT)
copyImage = PhotoImage(file='./assets/copy.png')
editmenu.add_command(label='Copy', accelerator='Ctrl+O', image=copyImage, compound=LEFT)
pasteImage = PhotoImage(file='./assets/paste.png')
editmenu.add_command(label='Paste', accelerator='Ctrl+S', image=pasteImage, compound=LEFT)
clearImage = PhotoImage(file='./assets/clear_all.png')
editmenu.add_command(label='Clear', accelerator='Ctrl+Alt+S', image=clearImage, compound=LEFT)
editmenu.add_separator()
findImage = PhotoImage(file='./assets/find.png')
editmenu.add_command(label='Find', accelerator='Ctrl+Q', image=findImage, compound=LEFT)


show_toolbar = BooleanVar()
show_statusbar = BooleanVar()

viewmenu = Menu(menubar, tearoff=False)
toolbarImage = PhotoImage(file='./assets/tool_bar.png')
viewmenu.add_checkbutton(label='Tool Bar' , variable=show_toolbar,
                         onvalue=True, offvalue=False, image=toolbarImage, compound=LEFT)
statusbarImage = PhotoImage(file='./assets/status_bar.png')
viewmenu.add_checkbutton(label='Status Bar', variable=show_statusbar,
                         onvalue=True,offvalue=False, image=statusbarImage, compound=LEFT)
menubar.add_cascade(label='View', menu=viewmenu)

theme_choice = StringVar()
thememenu = Menu(menubar, tearoff=False)
LightImage = PhotoImage(file='./assets/light_default.png')
thememenu.add_radiobutton(label='Light Defaut', image=LightImage,compound=LEFT, variable=theme_choice)
DarkImage = PhotoImage(file='./assets/dark.png')
thememenu.add_radiobutton(label='Dark', image=DarkImage,compound=LEFT, variable=theme_choice)
PinkImage = PhotoImage(file='./assets/red.png')
thememenu.add_radiobutton(label='Pink', image=PinkImage,compound=LEFT, variable=theme_choice)
MonokaiImage = PhotoImage(file='./assets/monokai.png')
thememenu.add_radiobutton(label='Monokai', image=MonokaiImage,compound=LEFT, variable=theme_choice)
menubar.add_cascade(label='View', menu=thememenu)

tool_bar=Label(root)
tool_bar.pack(side=TOP, fill=X)
font_families=font.families()
font_family_variable = StringVar()
fontfamily_Combobox=Combobox(tool_bar, width=30,values=font_families,state='readonly',textvariable=font_family_variable)
fontfamily_Combobox.current(font_families.index('Arial'))
fontfamily_Combobox.grid(row=0,column=0,padx=5)


size_variable=IntVar()
font_size_Combobox=Combobox(tool_bar,width=14,
                            textvariable=size_variable,state='readonly',values=tuple(range(8,80)))
font_size_Combobox.current(4)
font_size_Combobox.grid(row=0,column=1,padx=5)

boldImage = PhotoImage(file='./assets/bold.png')
boldButton=Button(tool_bar,image=boldImage)
boldButton.grid(row=0,column=2,padx=5)

italicImage = PhotoImage(file='./assets/italic.png')
italicButton=Button(tool_bar,image=italicImage)
italicButton.grid(row=0,column=3,padx=5)

underlineImage = PhotoImage(file='./assets/underline.png')
underlineButton=Button(tool_bar,image=underlineImage)
underlineButton.grid(row=0,column=4,padx=5)

font_colorImage = PhotoImage(file='./assets/font_color.png')
font_colorButton=Button(tool_bar,image=font_colorImage)
font_colorButton.grid(row=0,column=5,padx=5)

leftAlignImage = PhotoImage(file='./assets/left.png')
leftAlignButton=Button(tool_bar,image=leftAlignImage)
leftAlignButton.grid(row=0,column=6,padx=5)

rightAlignImage = PhotoImage(file='./assets/right.png')
rightAlignButton=Button(tool_bar,image=rightAlignImage)
rightAlignButton.grid(row=0,column=7,padx=5)

centerAlignImage = PhotoImage(file='./assets/center.png')
centerAlignButton=Button(tool_bar,image=centerAlignImage)
centerAlignButton.grid(row=0,column=8,padx=5)

scrollBar=Scrollbar(root)
scrollBar.pack(side=RIGHT,fill=Y)
textarea = Text(root,yscrollcommand=scrollBar.set,font=('arial', 12))
textarea.pack(fill=BOTH, expand=True)
scrollBar.config(command=textarea.yview)


status_bar=Label(root,text='Status Bar')
status_bar.pack(side=BOTTOM)
root.mainloop()
