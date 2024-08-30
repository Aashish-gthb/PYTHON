import email
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    input_password.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_list = [choice(letters) for _ in range(randint(8, 10))]+\
        [choice(symbols) for _ in range(randint(2, 4))]+\
            [choice(numbers) for _ in range(randint(2, 4))]
    

    shuffle(password_list)

    password = "".join(password_list)

    input_password.insert(0,f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
        website = input_wesite.get()
        email = input_email.get()
        password = input_password.get()
        new_data = {
             website:{
                  "email":email,
                  "password":password
             }
        }

        if len(website) == 0 or len(password) == 0 :
            messagebox.showinfo(title ="OOPS", message = "Please don't leave any fields empty")  

        else:
            try:
                with open("C:/Users/ashuj/Python/password-manager-start/data.json",'r') as file:
                    data = json.load(file)
                    
            except FileNotFoundError:
                with open("C:/Users/ashuj/Python/password-manager-start/data.json",'w') as file:
                    json.dump(new_data,file,indent=4) 
            except json.JSONDecodeError:
                with open("C:/Users/ashuj/Python/password-manager-start/data.json",'w') as file:
                    json.dump(new_data,file,indent=4)                
            else:
                data.update(new_data)
                with open("C:/Users/ashuj/Python/password-manager-start/data.json",'w') as file:
                    json.dump(data,file,indent=4)
            finally:        
                input_password.delete(0,END)
                input_wesite.delete(0,END)
#-----------------------------finding password ------------------------#
def find_passwrod():
    website = input_wesite.get()
    try:
        with open("C:/Users/ashuj/Python/password-manager-start/data.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("C:/Users/ashuj/Python/password-manager-start/data.json",'w') as file:
            json.dump({},file)
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
       

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width= 200 , height=200)
logo = PhotoImage(file="/Users/ashuj/Python/password-manager-start/logo.png")

canvas.create_image(100,100,image = logo)
canvas.grid(row=0,column=1) 

#labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)


#Entries
input_wesite = Entry(width=35)
input_wesite.grid(row= 1,column=1,columnspan=2,sticky = "EW")

input_email = Entry(width=35)
input_email.grid(row= 2,column=1,columnspan=2,sticky = "EW")
input_email.insert(0,"ashishvhanghas123@gmail.com")
 
input_password = Entry(width=21)
input_password.grid(row= 3,column=1,sticky = "EW")


#Buttons

password_button = Button(text= "Generate Password",command=generate_password)
password_button.grid(row=3,column=2,sticky = "EW")

search_button = Button(text= "Search",command=find_passwrod)
search_button.grid(row=1,column=2,sticky = "EW")

add_button = Button(text= "Add",width=36,command= save)
add_button.grid(row=4,column=1,columnspan=2,sticky = "EW")




window.mainloop()