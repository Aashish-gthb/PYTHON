from tkinter import *

windows = Tk()
windows.title("Mile to Kilometer Converter")
windows.minsize(width= 130 , height= 90)
windows.config(padx=20,pady=20)

input = Entry(width= 7)
input.grid(column=1,row = 0)

my_label = Label(text="Miles")
my_label.grid(column=2,row=0)

my_label = Label(text="is equal to")
my_label.grid(column=0,row=1)

def calculate():
    miles = float(input.get())
    km = miles * 1.609
    kilometer_result_label.config(text= f"{km}")

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1,row=1)

my_label = Label(text= "km" )
my_label.grid(column=2,row=1)



# def button_clicked():
#     print("YaY u died")
#     my_label.config(text = input.get())
#     print(input.get())

button = Button(text="Calculate",command= calculate)
button.grid(column=1,row=2)







windows.mainloop()