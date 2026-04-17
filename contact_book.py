import tkinter as tk

class Contact_book:
    def __init__(self):
        self.contacts = {}

    def edit_contact(self):
        name = input("Enter name: ")

        if name in self.contacts:
            print("Old numbers:", self.contacts[name])
            old = input("Enter number to replace: ")

            if old in self.contacts[name]:
                new = input("Enter new number: ")

                index = self.contacts[name].index(old)
                self.contacts[name][index] = new
                print("Updated")
            else:
                print("Number not found")
        else:
            print("Contacts not found")
                
    def add_contacts(self,name,phone):
        if name in self.contacts:
            self.contacts[name].append(phone)
        else:
            self.contacts[name] = [phone]
        return "Contact Added"

    def view_contacts(self):
        contact_list.delete(0,tk.END)
        for name , phones in self.contacts.items():
            contact_list.insert(tk.END,f"{name}: {', '.join(phones)}")
        return "All contacts shown"
        

    def search_contacts(self,name):
       contact_list.delete(0,tk.END)
       if name in self.contacts:
           phones = self.contacts[name]
           contact_list.insert(tk.END,f"{name}: {', '.join(phones)}")
           return "Found"
       else:
           contact_list.insert(tk.END,"Not Found")
        
    def delete_contacts(self,name,phone):
            if name in self.contacts:
                if phone in self.contacts[name]:
                      self.contacts[name].remove(phone)
                      return "deleted"
                else:
                    return "Number not found"
            else:
                return "contact not found"


root = tk.Tk()
root.title("Contact Book")
root.geometry("400x400+300+300")
frame = tk.Frame(root, borderwidth=2, relief="ridge")
frame.grid(row=0,column=0)

tk.Label(frame,text="Name").grid(row=0,column=0)
name_entry = tk.Entry(frame)
name_entry.grid(row=0,column=1)
name_entry.bind("<Return>",lambda event: phone_entry.focus())

tk.Label(frame,text="Phone").grid(row=1,column=0)
phone_entry = tk.Entry(frame)
phone_entry.grid(row=1,column=1)
phone_entry.bind("<Return>",lambda event: add())

book = Contact_book()

output = tk.Label(frame,text="",fg="purple",justify="left")
output.grid(row=4,column=0,columnspan=2,pady=20)

def add():
    name = name_entry.get()
    phone = phone_entry.get()

    result = book.add_contacts(name,phone)
    output.config(text="Saved")
    name_entry.focus()

def view():
    result = book.view_contacts()
    output.config(text=result)

def search():
    name = name_entry.get()
    result = book.search_contacts(name)
    output.config(text=result)

def delete():
    name = name_entry.get()
    phone = phone_entry.get()
    
    result = book.delete_contacts(name,phone)
    output.config(text=result)

def clear():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

tk.Button(frame,text="Add",width=10,command=add).grid(row=2,column=0,pady=10)
tk.Button(frame,text="View",width=10,command=view).grid(row=2,column=1)
tk.Button(frame,text="Search",width=10,command=search).grid(row=3,column=0)
tk.Button(frame,text="Delete",width=10,command=delete).grid(row=3,column=1)
tk.Button(frame,text="Clear",command=clear).grid(row=5, column=0, columnspan=2)

list_frame = tk.Frame(root)
list_frame.grid(pady=20)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.grid(row=0, column=1,sticky="ns")

contact_list = tk.Listbox(list_frame,width=40,height=10,yscrollcommand=scrollbar.set)
contact_list.grid(row=0, column=0)

scrollbar.config(command=contact_list.yview)





root.mainloop()
