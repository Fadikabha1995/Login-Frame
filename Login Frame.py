import tkinter as tk
import tkinter.simpledialog as simpledialog

# Create a dictionary to store the username and password
user_pass = {}

# Create a list to store the banned users
banned_users = []

# Create the main window
root = tk.Tk()
root.geometry("500x250")
root.title("Username and Password Login")

# Function to check if the username and password match
def check_user_pass(username, password):
    if username in user_pass and user_pass[username] == password:
        return True
    return False

# Function to create a new username and password
def create_user_pass(username, password):
    user_pass[username] = password
    label_result.config(text="Account created successfully")

def on_button_click():
    password = simpledialog.askstring("Password", "Enter password:", show='*')
    if password == "Admin":
        label_result.config(text="Access Granted")
    else:
        label_result.config(text="Access Denied")

# Function to handle the login process
def login():
    global attempts
    username = entry_username.get()
    password = entry_password.get()
    if username in banned_users:
        label_result.config(text="This user is banned")
        return
    if user_pass == {}:
        label_result.config(text="No Data Exist Please Create a new user")
        return
    if username == "" and password == "":
          label_result.config(text="Enter A Values!!!")
          return
    if check_user_pass(username, password):
        label_result.config(text="Login Successful")
    else:
        attempts += 1
        if attempts == 3:
            banned_users.append(username)
            label_result.config(text="Too many attempts. You are now banned")
            attempts = 0
        else:
            label_result.config(text=f"Incorrect username or password. {3 - attempts} attempts remaining")

# Function to handle the create account process
def create_account():
    username = entry_username.get()
    password = entry_password.get()
    if username in user_pass:
        label_result.config(text="Username already exists")
        return
    if username != "":
       create_user_pass(username, password)
    else:
       label_result.config(text="Enter A Value!!!")

# Function to handle the unlock account process
def unlock_account():
    username = entry_username.get()
    password = entry_password.get()
    if username not in banned_users:
        label_result.config(text="This user is not banned")
        return
    if check_user_pass(username, password):
        banned_users.remove(username)
        label_result.config(text="Account Unlocked")
    else:
        label_result.config(text="Incorrect username or password")

# Function to show all the users in a new frame
def show_all_users():
    # Create a new frame to display all the users
    new_frame = tk.Toplevel(root)
    new_frame.title("All Users")
    new_frame.geometry("500x200")

    # Display all the users and their passwords in a listbox
    listbox = tk.Listbox(new_frame,height=400,width=100)
    if user_pass == {}:
       listbox.insert(tk.END, f"Your DataBase still empty!!!")
    for username, password in user_pass.items():
        listbox.insert(tk.END, f"Username: {username}    ---     Password: {password}")
    listbox.pack()

# Create the GUI elements
label_username = tk.Label(root, text="Username",foreground="red")
label_password = tk.Label(root, text="Password",foreground="red")
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")
button_login = tk.Button(root, text="Login", command=login)
button_create = tk.Button(root, text="Create Account", command=create_account)
button_unlock = tk.Button(root, text="Unlock Account", command=unlock_account)
# Add the button for showing all users
button_show_users = tk.Button(root, text="Show All Users", command=show_all_users)
label_result = tk.Label(root, text="")

#Pack the GUI elements onto the screen
frame = tk.Frame(root, bg='white', bd=5)
frame.place(relx=0.5, rely=0.5, anchor='center')
root.resizable(False, False)
label_username.pack()
entry_username.pack()
label_password.pack()
entry_password.pack()
button_login.pack()
button_create.pack(side="left", padx = 30)
button_unlock.pack(side="left" , padx = 60)
button_show_users.pack(side="left" , padx = 10)
label_result.pack()
label_result.place(x=200,y=120)

#Initialize the number of attempts
attempts = 0

#Start the GUI event loop
root.mainloop()
