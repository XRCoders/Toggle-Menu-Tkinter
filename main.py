#Importing Libraries
import customtkinter
import tkinter

#Creating a window
root = customtkinter.CTk()

#Defining window properties
root.geometry('800x550')
root.title('Toggle Side Menu')

#Functions
def on_hover(e):
    home_button.configure(fg_color='#FF7575',bg_color='#FF7575',text_color='black')

def on_leave(e):
    home_button.configure(fg_color='gray17',bg_color='gray17',text_color='#FF7575')

def on_hover2(e):
    setting_button.configure(fg_color='#FF7575',bg_color='#FF7575',text_color='black')

def on_leave2(e):
    setting_button.configure(fg_color='gray17',bg_color='gray17',text_color='#FF7575')
#Content
def remove():
    main_frame = customtkinter.CTkFrame(root,width=800,height=550,fg_color='transparent')
    main_frame.place(x=0,y=0)

    open_button = customtkinter.CTkButton(main_frame,command=toggle,text='O P E N',width=100,height=50,fg_color='gray17',bg_color='gray17',hover_color='#FF7575')
    open_button.place(x=0,rely=0.005)
def toggle():
    global home_button,setting_button
    side_menu = customtkinter.CTkFrame(root,width=200,height=800)
    side_menu.place(x=0,y=0.5)

    close_button = customtkinter.CTkButton(side_menu,text='C L O S E',command=remove,width=100,height=50,fg_color='gray17',bg_color='gray17',hover_color='#FF7575')
    close_button.place(x=0,rely=0.005)
    home_button = customtkinter.CTkButton(side_menu,text='H O M E',width=200,height=50,fg_color='transparent',bg_color='gray17',text_color='#FF7575')
    home_button.place(x=0,rely=0.1)

    setting_button = customtkinter.CTkButton(side_menu,text='S E T T I N G',width=200,height=50,fg_color='transparent',bg_color='gray17',text_color='#FF7575')
    setting_button.place(x=0,rely=0.16)

    home_button.bind('<Enter>',on_hover)
    home_button.bind('<Leave>',on_leave)

    setting_button.bind('<Enter>',on_hover2)
    setting_button.bind('<Leave>',on_leave2)
#Running the app
if __name__ == '__main__':
    remove()
    root.mainloop()