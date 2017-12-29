# ---------------------------------------
# External Modules:
# ---------------------------------------

from tkinter import *

# ---------------------------------------
# Main frame:
# ---------------------------------------

def Window00():
    '''Main frame for GUI'''

    root = Tk()
    root.title("Accounting F17 Project 1")
    frame00 = Frame(root, width=400)
    frame00.grid(row=0)

    Window01(root)

# ---------------------------------------
# Trial Balance Number:
# ---------------------------------------

def Window01(master):
    '''Frame for number of accounts on trial balance'''

    def Help():
        '''What to do when <Help> button is clicked'''
        print("Window 01 <Help>")

    def Next(*args):
        '''What to do when <Next> button is clicked'''
        print("Window 01 <Next>")
        Window02(master, 2)
        frame01.grid_forget()

    def Exit():
        '''What to do when <Exit> button is clicked'''
        print("Window 01 <Exit>")
        master.destroy()

    frame01 = Frame(master, width=400)
    frame01.grid(row=0)

    # Bind '<Return>' key to Next function:
    master.bind('<Return>', Next)

    # Define text variable:
    Status = StringVar(frame01)

    # Set text variable default:
    Status.set("Click <Next> to continue.")

    # Define number entry field:
    number_entry = Entry(frame01, width=15)

    # Define text grid handles:
    text01 = Label(frame01, text="How many accounts on the trial balance?")
    text02 = Label(frame01, text="Enter a number:")
    text03 = Label(frame01, textvariable=Status)

    # Define spacers:
    spacer01 = Frame(frame01, height=2, width=400, bd=1, relief=SUNKEN)
    spacer02 = Frame(frame01, height=20, width=195)
    spacer03 = Frame(frame01, height=20, width=395)
    spacer04 = Frame(frame01, height=20, width=395)
    spacer05 = Frame(frame01, height=20, width=395)
    spacer06 = Frame(frame01, height=2, width=400, bd=1, relief=SUNKEN)
    spacer07 = Frame(frame01, width=95)

    # Define buttons:
    help_button = Button(frame01, text="Help", command=Help)
    next_button = Button(frame01, text="Next", command=Next)
    exit_button = Button(frame01, text="Exit", command=Exit)

    # Place window elements:
    text01.grid(row=2, columnspan=4)
    spacer01.grid(row=3, columnspan=4)
    text02.grid(row=4, sticky=W)
    spacer02.grid(row=4, column=1)
    number_entry.grid(row=4, column=2, sticky=E, padx=5, pady=5, columnspan=2)
    spacer03.grid(row=5, columnspan=4)
    spacer04.grid(row=6, columnspan=4)
    spacer05.grid(row=7, columnspan=4)
    text03.grid(row=8, columnspan=4)
    spacer06.grid(row=9, columnspan=4)
    help_button.grid(row=10, sticky=W, padx=5)
    spacer07.grid(row=10, column=1)
    next_button.grid(row=10, column=2, sticky=E, pady=5)
    exit_button.grid(row=10, column=3, sticky=E, padx=5)

# ---------------------------------------
# Trial Balance accounts frame:
# ---------------------------------------

def Window02(master, number):
    '''Frame for accounts on trial balance'''

    def Help():
        '''What to do when <Help> button is clicked'''
        print("Window 02 <Help>")

    def Next(*args):
        '''What to do when <Next> button is clicked'''
        print("Window 02 <Next>")

    def Exit():
        '''What to do when <Exit> button is clicked'''
        print("Window 02 <Exit>")
        master.destroy()

    frame02 = Frame(master, width=400)
    frame02.grid(row=1)

    # Bind '<Return>' key to Next function
    master.bind('<Return>', Next)

    # Define text variables:
    Menu01 = StringVar(frame02)
    Menu02 = StringVar(frame02)
    Status = StringVar(frame02)

    # Set text variable defaults:
    Menu01.set('-----')
    Menu02.set('-----')
    Status.set("Click <Next> to continue.")

    # Define text grid handles:
    text01 = Label(frame02, text="Enter the following for each account.")
    text02 = Label(frame02, text="Name:")
    text03 = Label(frame02, text="Balance:")
    text04 = Label(frame02, text="Normal Balance:")
    text05 = Label(frame02, text="Type:")
    text06 = Label(frame02, textvariable=Status)

    # Define menu option lists:
    norm_bal_options = ("Debit", "Credit")
    acct_type_options = ("Asset", "Liabitity", "Owner Equity", "Revenue",
                         "Expense")

    # Define entry fields and menus:
    name_entry = Entry(frame02, width=20)
    bal_entry = Entry(frame02, width=20)
    norm_bal_menu = OptionMenu(frame02, Menu01, *norm_bal_options)
    acct_type_menu = OptionMenu(frame02, Menu02, *acct_type_options)

    # Define spacers:
    spacer01 = Frame(frame02, height=2, width=400, bd=1, relief=SUNKEN)
    spacer02 = Frame(frame02, height=25, width=40)
    spacer03 = Frame(frame02, height=20, width=40)
    spacer04 = Frame(frame02, height=20, width=40)
    spacer05 = Frame(frame02, height=20, width=40)
    spacer06 = Frame(frame02, height=2, width=400, bd=1, relief=SUNKEN)
    spacer07 = Frame(frame02, height=20, width=20)
    
    # Define buttons:
    help_button = Button(frame02, text="Help", command=Help)
    next_button = Button(frame02, text="Next", command=Next)
    exit_button = Button(frame02, text="Exit", command=Exit)

    # Place frame elements:
    text01.grid(row=2, columnspan=4)
    spacer01.grid(row=3, columnspan=4)
    text02.grid(row=4, sticky=W)
    spacer02.grid(row=4, column=1)
    name_entry.grid(row=4, column=2, sticky=E, padx=5, columnspan=2)
    text03.grid(row=5, sticky=W)
    spacer03.grid(row=5, column=1)
    bal_entry.grid(row=5, column=2, sticky=E, padx=5, columnspan=2)
    text04.grid(row=6, sticky=W)
    spacer04.grid(row=6, column=1)
    norm_bal_menu.grid(row=6, column=2, sticky=E, padx=2.5, columnspan=2)
    text05.grid(row=7, sticky=W)
    spacer05.grid(row=7, column=1)
    acct_type_menu.grid(row=7, column=2, sticky=E, padx=2.5, columnspan=2, )
    text06.grid(row=8, columnspan=4)
    spacer06.grid(row=9, columnspan=4)
    help_button.grid(row=10, sticky=W, padx=5)
    spacer07.grid(row=10, column=1)
    next_button.grid(row=10, column=2, sticky=E, pady=5)
    exit_button.grid(row=10, column=3, sticky=E, padx=5)

# ---------------------------------------
# Initiator:
# ---------------------------------------

Window00()
