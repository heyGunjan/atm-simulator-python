
import tkinter as tk
class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self,task,priority):
        self.tasks.append({
        "task": task,
        "done": False,
        "priority": priority
    })
    def delete_task(self,index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
    def toggle_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = not self.tasks[index]["done"]
    def edit_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["task"] = new_task

    def get_tasks(self):
        return self.tasks

root = tk.Tk()
root.title("To-Do App")
root.geometry("400x500")

manager = TaskManager()

frame = tk.Frame(root)
frame.pack()

task_entry = tk.Entry(root,width=30)
task_entry.pack(pady=10)
task_entry.bind("<Return>",lambda event: add("high"))


def refresh():
    task_list.delete(0,tk.END)

    for i,t in enumerate(manager.get_tasks()):
        status = "\u2714" if t["done"] else "\u2716"
        task_list.insert(
            tk.END,f"{i+1}.{t['task']} {t['priority']} [{status}]"
        )
def add(priority):
    task =  task_entry.get()

    if task:
        manager.add_task(task,priority)
        task_entry.delete(0,tk.END)
        refresh()
        save_tasks()
def delete():
    selected = task_list.curselection()

    if selected:
        manager.delete_task(selected[0])
        refresh()
        save_tasks()
def toggle_done():
    selected = task_list.curselection()
    if selected:
        manager.toggle_done(selected[0])
        refresh()
        save_tasks()
       
def edit_task():
    selected = task_list.curselection()
    new_task = task_entry.get()
    if selected and new_task:
        manager.edit_task(selected[0], new_task)
        task_entry.delete(0, tk.END)
        refresh()
        save_tasks()
    
def save_tasks():
    with open("tasks.txt", "w") as f:
        for t in manager.get_tasks():
            line = f"{t['task']}|{t['done']}|{t['priority']}\n"
            f.write(line)

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                parts = line.strip().split("|")

                task = parts[0]
                done = parts[1] == "True"
                priority = parts[2] if len(parts) > 2 else "low"

                manager.tasks.append({
                    "task": task,
                    "done": done,
                    "priority": priority
                })
    except:
        pass

tk.Button(root, text="Add High", command=lambda: add("high")).pack(pady=3)
tk.Button(root, text="Add Medium", command=lambda: add("medium")).pack(pady=3)
tk.Button(root, text="Add Low", command=lambda: add("low")).pack(pady=3)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

task_list = tk.Listbox(frame,width=40,height=15,yscrollcommand=scrollbar.set)
task_list.pack()
task_list.bind("<Double-Button-1>",lambda e: toggle_done())

scrollbar.config(command=task_list.yview)

load_tasks()
refresh()
root.mainloop()

