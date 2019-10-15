from tkinter import *
import tkinter.messagebox
import shelve

root = Tk()
data = shelve.open("database")
root.title("Phonebook")
# root.geometry("500x250")
type = "No type!"
cmd = IntVar()
boolean_delete_search = "nothing"
current_location = "main"
printrecord = "nothing"
printname = "nothing"
printphone = "nothing"
printaddress = "nothing"
printtype = "nothing"


def raise_frame(frame):
    global current_location
    global boolean_delete_search
    global printrecord
    global printname
    global printphone
    global printaddress
    global printtype

    if frame == searchy:
        boolean_delete_search = "search"
    if frame == deletey:
        boolean_delete_search = "delete"
    if frame == createy:
        boolean_delete_search = "record"
    if frame == printy:
        boolean_delete_search = "print"
    if frame == mainy:
        if current_location == "insearch":
            printrecord.destroy()
            printname.destroy()
            printphone.destroy()
            printaddress.destroy()
            printtype.destroy()
    frame.tkraise()


mainy = Frame(root)
createy = Frame(root)
searchy = Frame(root)
deletey = Frame(root)
printy = Frame(root)
blankframe = Frame(root)

for frame in (mainy, createy, searchy, deletey, printy,blankframe):
    frame.grid(row=0, column=0, sticky='news')

create = Button(mainy, text="Create/Edit Record", width="25", command=lambda: raise_frame(createy))
search = Button(mainy, text="Search Record", width="25", command=lambda: raise_frame(searchy))
delete = Button(mainy, text="Delete Record", width="25", command=lambda: raise_frame(deletey))

printall = Button(mainy, text="Print All Users", width=25,command=lambda: raise_frame(printy))


create.pack()
search.pack()
delete.pack()
printall.pack()
# contains the create/edit frame
name = Label(createy, text="Name")
phone = Label(createy, text="Phone")
address = Label(createy, text="Address")
entry_name = Entry(createy)
entry_phone = Entry(createy)
entry_address = Entry(createy)

name.grid(row=0, sticky=E)
phone.grid(row=1, sticky=E)
address.grid(row=2, sticky=E)
entry_name.grid(row=0, column=1)
entry_phone.grid(row=1, column=1)
entry_address.grid(row=2, column=1)


def setstuff():
    global type
    c = cmd.get()
    if c == 1:
        type = "personal"
    else:
        type = "business"


personal = Radiobutton(createy, text="personal", variable=cmd, value=1, command=setstuff)
personal.grid(row=3, column=0)
buisness = Radiobutton(createy, text="business", variable=cmd, value=2, command=setstuff)
buisness.grid(row=3, column=1)


def doRadio():
    global type
    if type == "No type!" or entry_name.get() == "" or entry_phone.get() == "" or entry_address.get() == "":
        tkinter.messagebox.showinfo("Save Info", "Please fill in everything")
    else:
        data[entry_name.get()] = entry_name.get(), entry_phone.get(), entry_address.get(), type
        tkinter.messagebox.showinfo("Save Info", "Your record has been saved")


save_record = Button(createy, text="Save record", command=doRadio)
save_record.grid(row=4, column=1)

home_button = Button(createy, text="Go Home", command=lambda: raise_frame(mainy))
home_button.grid(row=5, column=1)
# contains search frame
search_name = Label(searchy, text="Name")
search_entry = Entry(searchy)

search_name.grid(row=0, sticky=E)
search_entry.grid(row=0, column=1)


def printinfo():
    global boolean_delete_search
    global current_location
    global printrecord
    global printname
    global printphone
    global printaddress
    global printtype
    if boolean_delete_search == "search":

        if search_entry.get() in data:
            current_location = "insearch"
            printrecord = Label(searchy, text="Record found:")
            printrecord.grid(row=1, column=1)
            printname = Label(searchy, text="Name: " + data[search_entry.get()][0])
            printname.grid(row=2, column=1)
            printphone = Label(searchy, text="Phone: " + data[search_entry.get()][1])
            printphone.grid(row=3, column=1)
            printaddress = Label(searchy, text="Address: " + data[search_entry.get()][2])
            printaddress.grid(row=4, column=1)
            printtype = Label(searchy, text="Type: " + data[search_entry.get()][3])
            printtype.grid(row=5, column=1)

        else:
            tkinter.messagebox.showinfo("Search Info", "There was no such record")
    if boolean_delete_search == "delete":
        if delete_entry.get() in data:
            del data[delete_entry.get()]
            tkinter.messagebox.showinfo("Delete Info", "The record has been deleted")
        else:
            tkinter.messagebox.showinfo("Delete Info", "No record to delete")

    if boolean_delete_search == "record":
        doRadio()
    if boolean_delete_search == "print":
        current_location = "inprint"
        for x in data:
            thislabel = Label(printy, text="Name: " + data[x][0] + " Phone: " + data[x][1] + " Address: " + data[x][
                2] + " Type: " + data[x][3])
            thislabel.grid(row=1, column=0)


home_buttons = Button(searchy, text="Go Home", command=lambda: raise_frame(mainy))
home_buttons.grid(row=0, column=4)

search_button = Button(searchy, text="Search", command=printinfo)
search_button.grid(row=0, column=3)

# contains delete frame

delete_name = Label(deletey, text="Name")
delete_entry = Entry(deletey)

delete_name.grid(row=0, sticky=E)
delete_entry.grid(row=0, column=1)

home_buttond = Button(deletey, text="Go Home", command=lambda: raise_frame(mainy))
home_buttond.grid(row=0, column=4)

delete_button = Button(deletey, text="Delete", command=printinfo)
delete_button.grid(row=0, column=3)


# contains stuff for print all frame
mylist = []
def otherfunction():
    for y in mylist:
        y.destroy()
    counter = 2
    for x in data:
        thislabel = Label(printy, text="Name: " + data[x][0] + " Phone: " + data[x][1] + " Address: " + data[x][
            2] + " Type: " + data[x][3])
        thislabel.grid(row=counter, column=0)
        mylist.append(thislabel)

        counter = counter + 1


click_print = Button(printy, text="Press to Print All User", command=otherfunction)
click_print.grid(row=0, column=0)
go_home_print = Button(printy, text="Go Home", command=lambda: raise_frame(mainy))
go_home_print.grid(row=0, column=1)

go_home_print1 = Button(blankframe, text="Go Home", command=lambda: raise_frame(mainy))
go_home_print1.grid(row=0, column=1)

raise_frame(mainy)

root.mainloop()
