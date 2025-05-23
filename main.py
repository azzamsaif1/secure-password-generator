from tkinter import *
from tkinter import messagebox
import pyperclip
#---------Password Generater -------#
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list=password_letters + password_symbols +password_numbers
    random.shuffle(password_list)

    password = "" .join(password_list)
    password_entry.insert(0 , password)
   # for char in password_list:
      #  password += char
    pyperclip.copy(password)

    print(f"Your generated password is: {password}")





#----------Save Password ----------#
def save():
    website=website_entry.get()
    Email=email_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo("oop" , message="Please make sure you have not filed empty.")
    else:
        is_ok = messagebox.askokcancel(title="website", message=f"there are details entered :\n Email {Email} "
                                                                f" password {password} \n website {website}")

        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"\n{website}| {Email}| {password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# ---------- Logo ----------
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="second.png")  #
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# ---------- Labels ----------
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="E", pady=(10, 0))

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="E", pady=(10, 0))

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="E", pady=(10, 0))

# ---------- Entries ----------
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, pady=(10, 0))
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, pady=(10, 0))
email_entry.insert(0,"nameexample@....")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, pady=(10, 0))

# ---------- Buttons ----------
generate_password_button = Button(text="Generate Password" ,command=generate_password)
generate_password_button.grid(row=3, column=2, pady=(10, 0))

add_button = Button(text="Add", width=36 , command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=(20, 0))

window.mainloop()
