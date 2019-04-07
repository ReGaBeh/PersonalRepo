from tkinter import *
from time import sleep
from webbrowser import open

print("DO NOT CLOSE THIS WINDOW")


def numrange():

    def execute1():
        # print("Execute function called")

        eowin = Tk()
        eowin.title("Even and odd numbers")
        Label(eowin, text="Results are printed in the console").pack()

        even = []

        a = entry1.get()
        b = entry2.get()

        for x in range(int(a), int(b)):
            mod = x % 2
            if mod > 0:
                pass
            else:
                even.append(x)

        counter1 = 0
        counter2 = 0

        print("*************")
        for x in range(int(a), int(b)):
            sleep(0.02)
            if x in even:
                print(x, "is even")
                counter1 = counter1 + 1
            elif x == 0:
                print(x, "is neither")
            else:
                print(x, "is odd")
                counter2 = counter2 + 1

        print("There are ", counter1, "even numbers between", a, "and", b)
        print("There are ", counter2, "odd numbers between", a, "and", b)

        if 0 in even:
            print("Not including 0")
        else:
            pass

    rangewin = Tk()
    rangewin.title("Even and Odd numbers")
    Label(rangewin, text="Enter the beginning of your range").grid()
    entry1 = Entry(rangewin)
    entry1.grid()
    Label(rangewin, text="Enter the end of you range").grid()
    entry2 = Entry(rangewin)
    entry2.grid()
    inbutton = Button(rangewin, text="Submit", command=execute1).grid()


# def primerange():
#
#     def execute2():
#         primerange = Tk()
#         primerange.title("Prime numbers")
#         Label(primerange, text="results areprinted in console")
#
#         primes = []
#         div = []
#
#         a = entry1.get()
#         b = entry2.get()
#
#         for x in range(int(a), int(b)):
#             if x > 1:
#                 for y in range(1, x):
#                     if x % y == 0:
#                         div.append(y)
#
#                         if div == [1, x] or [x, 1]:
#                             primes.append(x)
#                         else:
#                             pass
#
#         for x in range(int(a), int(b)):
#             sleep(0.02)
#             if x in primes:
#                 print(x, "Is a prime number")
#
#     primewin = Tk()
#     primewin.title("Prime numbers")
#     Label(primewin, text="Enter the beginning of your range").grid()
#     entry1 = Entry(primewin)
#     entry1.grid()
#     Label(primewin, text="Enter the end of your range").grid()
#     entry2 = Entry(primewin)
#     entry2.grid()
#     inbutton = Button(primewin, text="Submit", command=execute2).grid()


def triangle():

    def execute3():
        triwin2 = Tk()
        triwin2.title("Triangle numbers")
        Label(triwin2, text="Results are printed in the console").pack()

        trange = entry1.get()
        num = 0

        print("*************")
        for x in range(1, int(trange) + 1):
            num = num + x
            print(num)
            sleep(0.02)

    triwin = Tk()
    triwin.title("Triangle numbers")
    Label(triwin, text="Enter how many triangle numbers you want to display").grid()
    entry1 = Entry(triwin)
    entry1.grid()
    inbutton = Button(triwin, text="Submit", command=execute3).grid()


def currency():

    def yen():
        x = entry1.get()
        y = float(x) * 147.84
        print("*************")
        print(x, "GBP is equal to: ", y, "japanese yen.")

    def yuan():
        x = entry1.get()
        y = float(x) * 8.86
        print("*************")
        print(x, "GBP is equal to: ", y, "chinese yuan.")

    def usd():
        x = entry1.get()
        y = float(x) * 1.32
        print("*************")
        print(x, "GBP is equal to: ", y, "american dollars.")

    cwin = Tk()
    cwin.title("Currency converter")
    Label(cwin, text="Enter a number of GBP")
    entry1 = Entry(cwin)
    entry1.grid()
    ybutton = Button(cwin, text="Convert to Yen", command=yen).grid()
    yubutton = Button(cwin, text="Convert to Yuan", command=yuan).grid()
    ubutton = Button(cwin, text="Convert to US dollars", command=usd).grid()


window = Tk()
window.title("Number Program")
window.geometry("400x250")

rbutton = Button(window, text="Find the Even/Odd numbers in a range", command=numrange).pack()
# pButton = Button(window, text="Find all prime numbers in a range", command=primerange).pack()
tButton = Button(window, text="Triangle numbers", command=triangle).pack()
mbutton = Button(window, text="Currency converter", command=currency).pack()


def test():

    def stest1():
        print("Buttons = Functional")

    def stest2():
        x = tentry.get()
        print("The entry's input is: ", x)
        print("Entries = Functional")
        print(".get() = Functional")
        sleep(1)
        print("Sleep = Functional")

    print("Menu = Functional")
    nwin = Tk()
    nwin.title("Test")
    print("Windows = Functional")
    Button(nwin, text="Test", command=stest1).pack()
    tentry = Entry(nwin)
    tentry.pack()
    Button(nwin, text="Entry test", command=stest2).pack()


def quit():
    window.quit()


def egg():
    new = 2
    url = "https://www.youtube.com/watch?v=0DPdYp8MTDc"
    open(url, new=new)


menu = Menu(window)
# menu.add_command(label="Close this window", command=quit)
dmenu = Menu(menu, tearoff=0)
dmenu.add_command(label="Close this window", command=quit)
dmenu.add_command(label="Test the program", command=test)
dmenu.add_command(label="Easter egg", command=egg)
menu.add_cascade(label="Menu", menu=dmenu)


window.config(menu=menu)
window.mainloop()
