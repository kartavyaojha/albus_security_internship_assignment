import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class FileManager(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("File Manager")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        self.dir_label=tk.Label(self, text="Current Directory:")
        self.dir_label.pack()

        self.dir_entry=tk.Entry(self, width=50)
        self.dir_entry.pack()

        self.browse_button=tk.Button(self, text="Browse", command=self.browse_directory)
        self.browse_button.pack()

        self.file_listbox=tk.Listbox(self, width=50, height=20)
        self.file_listbox.pack()

        self.copy_button=tk.Button(self, text="Copy", command=self.copy_file)
        self.copy_button.pack()

        self.move_button=tk.Button(self, text="Move", command=self.move_file)
        self.move_button.pack()

        self.delete_button=tk.Button(self, text="Delete", command=self.delete_file)
        self.delete_button.pack()

    def browse_directory(self):
        directory=filedialog.askdirectory()
        if directory:
            self.dir_entry.delete(0, tk.END)
            self.dir_entry.insert(0, directory)
            self.update_file_list()

    def update_file_list(self):
        directory=self.dir_entry.get()
        self.file_listbox.delete(0, tk.END)
        for filename in os.listdir(directory):
            self.file_listbox.insert(tk.END, filename)

    def copy_file(self):
        selected_file=self.file_listbox.get(self.file_listbox.curselection())
        source_path=os.path.join(self.dir_entry.get(), selected_file)
        destination_path=filedialog.askdirectory()
        if destination_path:
            try:
                shutil.copy(source_path, destination_path)
                messagebox.showinfo("Success", f"{selected_file} copied to {destination_path}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def move_file(self):
        selected_file=self.file_listbox.get(self.file_listbox.curselection())
        source_path=os.path.join(self.dir_entry.get(), selected_file)
        destination_path=filedialog.askdirectory()
        if destination_path:
            try:
                shutil.move(source_path, destination_path)
                messagebox.showinfo("Success", f"{selected_file} moved to {destination_path}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def delete_file(self):
        selected_file=self.file_listbox.get(self.file_listbox.curselection())
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete {selected_file}?"):
            try:
                os.remove(os.path.join(self.dir_entry.get(), selected_file))
                messagebox.showinfo("Success", f"{selected_file} deleted")
                self.update_file_list()
            except Exception as e:
                messagebox.showerror("Error", str(e))

if __name__=="__main__":
    app=FileManager()
    app.mainloop()