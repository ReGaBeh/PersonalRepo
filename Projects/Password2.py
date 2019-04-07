from tkinter import *
import webbrowser  # Importing the necessary libraries
from random import randint


def meme():  # This function is called when the checkbutton is interacted with
    new = 2

    url = "https://www.youtube.com/watch?v=z-nfbDXTiHg"  # List of possible urls
    url1 = "https://www.youtube.com/watch?v=MNKKg82g-I4"
    url2 = "https://www.youtube.com/watch?v=YG8vtggc1Ok"

    i = randint(1, 3)  # Randomly chooses a number between 1 and 3

    if i == 1:  # Decides which url to request based on the randomly generated 'i'
        webbrowser.open(url, new=new)
    elif i == 2:
        webbrowser.open(url1, new=new)
    else:
        webbrowser.open(url2, new=new)


def newLogin():  # This function creates new details and writes them to a .txt file

    uNew = uEntry.get()
    pNew = pEntry.get()

    z = str(uNew[0]) + str(len(uNew))  # These 3 lines create and individual id for each set
    a = str(z) + uNew + "\n"           # To prevent mixing and matching usernames/passwords
    b = str(z) + pNew + "\n"

    uList = []
    pList = []

    file = open("usernames.txt", "r")  # Reads the username and password files and adds them
    for x in file:                     # To seperate lists for comparing
        uList.append(x)

    file2 = open("passwords.txt", "r")
    for x in file2:
        pList.append(x)

    if a in uList and b in pList:  # Determines if the details already exist
        already = Tk()
        already.title("Details already used")
        Label(already, text="These details have already been used").pack()
        Label(already, text="Please enter new details").pack()
    else:  # This statement writes the new details if hey don't previously exist
        file = open("usernames.txt", "a")
        file.write(str(z) + uNew + "\n")
        file.close()

        file2 = open("passwords.txt", "a")
        file2.write(str(z) + pNew + "\n")
        file2.close()


def compare():  # This function compares the details to the input
    u1 = "Username"  # Hardwired username and password
    p1 = "Password"

    uList = []  # Lists of all the usernames/passwords
    pList = []

    uInput = uEntry.get()  # Deefines the input
    pInput = pEntry.get()

    file = open("usernames.txt", "r")  # Writes the existing usernames to uList
    for x in file:
        uList.append(x)

    file2 = open("passwords.txt", "r")  # Writes the existing passwords to pList
    for x in file2:
        pList.append(x)

    file.close()
    file2.close()

    print(uList, "\n", pList)  # Console output for monitoring
    print(uInput, "\n", pInput)

    z = str(uInput[0]) + str(len(uInput))  # Adds the id to the input, for comparison
    a = str(z) + uInput + "\n"             # With the unique username/password sets
    b = str(z) + pInput + "\n"

    if uInput == u1 and pInput == p1:  # Checks if input == hardwired userame/password
        print("Username/Password is correct")  # Tkinter to display an entry granted window

        entrance = Tk()
        entrance.title("Entry granted")
        Label(entrance, text="Entry granted").pack()
        entrance.mainloop()

    elif a in uList and b in pList:  # Checks if the input with the id is an existing set
        print("Username/Password is correct")  # Tkinter to display an entry granted window

        entrance = Tk()
        entrance.title("Entry granted")
        Label(entrance, text="Entry granted").pack()
        entrance.mainloop()

    else:  # Denial of entry
        print("Username and/or password is incorrect")

        denied = Tk()
        denied.title("Entry  denied")
        Label(denied, text="Entry denied").pack()
        denied.mainloop()


window = Tk()  # Tkinter window for entering input and creating new details
window.title("LOCKED")
window.geometry("240x100")
Label(window, text="Username").grid(row=0)
Label(window, text="Password").grid(row=1)
uEntry = Entry(window)
pEntry = Entry(window)
# Button for calling compare()
inButton = Button(window, text="Submit", command=compare).grid(row=2, column=1)
# Checkbutton for calling meme()
check = Checkbutton(window, text="Keep me logged in", command=meme)
# Button for calling newLogin()
newButton = Button(window, text="Create new details", command=newLogin).grid(row=3)

uEntry.grid(row=0, column=1)  # Packing the buttons
pEntry.grid(row=1, column=1)
check.grid(row=2, column=0)

window.mainloop()
