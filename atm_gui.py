import tkinter as tk

class ATM:
    def __init__(self,balance,pin):
        self.balance = balance
        self.pin = pin
    def check_balance(self,pin):
        if pin == self.pin:
            return f"balance:{self.balance}"
        else:
            return "wrong pin"
    def deposit(self,pin,amount):
        if pin == self.pin:
            self.balance += amount
            return f"Deposited {amount}"
        else:
            return "wrong pin"
    def withdraw(self,pin,amount):
        if pin == self.pin:
            if amount <= self.balance: 
                self.balance -= amount
                return f"Withdrewed {amount}"
            else:
                return "Insufficient Balance"
        else:
            return "wrong pin"

atm = ATM(9000 , 6789)

root = tk.Tk()
root.title("ATM system")
root.geometry("400x400+300+300")

tk.Label(root, text="Enter PIN", font=("Ariel",16) , fg = "blue", bg = "pink").pack()
pin_entry = tk.Entry(root , show="*")
pin_entry.pack(pady=5)

tk.Label(root , text="Enter Amount" , font=("Ariel",16),fg = "blue" , bg ="pink").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

output_Label = tk.Label(root , text="")
output_Label.pack()

def check_balance():
    pin = int(pin_entry.get())
    result = atm.check_balance(pin)
    output_Label.config(text=result)
def deposit():
    pin = int(pin_entry.get())
    amount = int(amount_entry.get())
    result = atm.deposit(pin,amount)
    output_Label.config(text=result)
def withdraw():
    pin = int(pin_entry.get())
    amount = int(amount_entry.get())
    result = atm.withdraw(pin,amount)
    output_Label.config(text=result)

tk.Button(root,text="Check Balance",command = check_balance).pack()
tk.Button(root,text="Deposit",command = deposit).pack()
tk.Button(root,text="Withdraw",command = withdraw).pack()

root.mainloop()

    
    
