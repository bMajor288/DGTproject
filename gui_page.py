from tkinter import *
#from PIL import Image, ImageTk
import time

root = Tk()
# root.geometry("360x800") #same screen ratio as my phone; 20:9, less pixels
# root.geometry("200x430") #same as wireframe dimensions
root.title("Superstar") #Not the final name of the app

#setting background
root.configure(bg="black")
bgimg = PhotoImage(file="")

#creating functions
def alternate_title(): #NOT WORKING
    number = 0
    while True:
        lang_title = titles[number]
        lang_menu.title(lang_title)
        time.wait(2)
        number += 1
        if number >= len(titles):
            number = 0
            continue
def open_language_menu():
    lang_menu = Toplevel(root)
    lang_menu.title(lang_title)
    Label(lang_menu, text="Language options will appear here").pack()
    alternate_title()
def open_plus_menu():
    pass
def open_settings():
    pass
def goto_prev_event():
    pass
def goto_next_event():
    pass
def show_event_details():
    description = Toplevel(root)
    description.title("Description")
    Label(description, text=current_description).pack()
    pass

#creating frames
top_frame = Frame(root, bg="black")
top_frame.grid(row=0, column=0)
middle_frame = Frame(root, bg="black")
middle_frame.grid(row=1, column=0)
location_frame = Frame(root, bg="black")
location_frame.grid(row=2, column=0)
bottom_frame = Frame(root, bg="black")
bottom_frame.grid(row=3, column=0)

#setting variables
current_event = StringVar()
current_event.set("METEOR")
current_countdown = StringVar()
current_countdown.set("16:19")
current_city = StringVar()
current_city.set("Auckland")
current_country = StringVar()
current_country.set("New Zealand")
current_description = StringVar()
current_description.set("A solar eclipse occurs when the moon passes in front of the sun and obscures it from view.")
#regular variable
lang_title = None
lang_menu = None
#arrays
titles = ["Select a language", "selecciona un idioma", "选择一种语言", "whiriwhiria he reo"]

##Setting icon images
#img=ImageTk.PhotoImage(file="images/left_arrow.png")
#middle frame
left_arrow = PhotoImage(file="images/left_arrow.png")#, width=40, height=50)
event_image = PhotoImage(file="images/solar_eclipse.png")#, width=100, height=100)
right_arrow = PhotoImage(file="images/right_arrow.png")#, width=40, height=50)
#bottom frame
translate_image = PhotoImage(file="images/translate_image.png")
plus_image = PhotoImage(file="images/plus_image.png")
settings_image = PhotoImage(file="images/settings_button.png")

##Setting labels
#labels in the top frame
next_event_text = Label(top_frame, text="NEXT EVENT:", fg="#7843e6", bg="black")
next_event_text.grid(row=0, column=0)
event_label = Label(top_frame, textvariable=current_event, fg="#ffca28", bg="black")
event_label.grid(row=1, column=0)
countdown_label = Label(top_frame, textvariable=current_countdown, fg="blue", bg="black")
countdown_label.grid(row=2, column=0)
#labels in the middle frame
prev_label = Label(middle_frame, text="PREV", fg="#7843e6", bg="black")
prev_label.grid(row=1, column=0)
next_label = Label(middle_frame, text="NEXT", fg="#7843e6", bg="black")
next_label.grid(row=1, column=2)
#labels in location frame
location_label = Label(location_frame, text="Location:", fg="blue", bg="black")
location_label.grid(row=0, column=1)
city_label = Label(location_frame, textvariable=current_city, fg="#ffca28", bg="black")
city_label.grid(row=1, column=1)
country_label = Label(location_frame, textvariable=current_country, fg="#ffca28", bg="black")
country_label.grid(row=2, column=1)

##Setting buttons
#buttons in middle frame
previous_button = Button(middle_frame, image=left_arrow, command=goto_prev_event)
previous_button.grid(row=0, column=0)
event_button = Button(middle_frame, image=event_image, command=show_event_details)
event_button.grid(row=0, column=1)
next_button = Button(middle_frame, image=right_arrow, command=goto_next_event)
next_button.grid(row=0, column=2)
#buttons in bottom frame
language_button = Button(bottom_frame, image=translate_image, command=open_language_menu)#, width=45, height=45)
language_button.grid(row=0, column=0)
plus_button = Button(bottom_frame, image=plus_image, command=open_plus_menu)#, width=45, height=45)
plus_button.grid(row=0, column=1)
settings_button = Button(bottom_frame, image=settings_image, command=open_settings)#, width=45, height=45)
settings_button.grid(row=0, column=2)


root.mainloop()