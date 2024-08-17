import tkinter as tk
import os
from tkinter import ttk, filedialog, messagebox, PhotoImage
from windowHelpers import SetWindowCenterOfScreen
from converters import AppleToUniversal, UniversalToApple

downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

def selectAppleToUniversal():
    input_file = filedialog.askopenfilename(title="Select Input CSV File", initialdir=downloads_dir, filetypes=[("CSV Files", "*.csv")])
    if not input_file:
        messagebox.showinfo("No input file selected. Exiting.")
        return

    output_file = filedialog.asksaveasfilename(title="Save Converted CSV File As", initialdir=downloads_dir, defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if not output_file:
        messagebox.showinfo("No output file selected. Exiting.")
        return

    AppleToUniversal(input_file, output_file)
    messagebox.showinfo("Conversion Complete", f"Converted from Apple format to standard format. The file has been saved as: {output_file}")
    return

def selectUniversalToApple():
    input_file = filedialog.askopenfilename(title="Select Input CSV File", initialdir=downloads_dir, filetypes=[("CSV Files", "*.csv")])
    if not input_file:
        messagebox.showinfo("No input file selected. Exiting.")
        return

    output_file = filedialog.asksaveasfilename(title="Save Converted CSV File As", initialdir=downloads_dir, defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if not output_file:
        messagebox.showinfo("No output file selected. Exiting.")
        return

    UniversalToApple(input_file, output_file)
    messagebox.showinfo("Conversion Complete", f"Converted from standard format to Apple format. The file has been saved as: {output_file}")
    return

def main():
    root = tk.Tk()
    root.title('Keychain CSV Converter')
    root.resizable(False, False)
    
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label='Universal to Keychain', command=lambda: selectUniversalToApple())
    filemenu.add_command(label='Keychain to Universal', command=lambda: selectAppleToUniversal())
    menubar.add_cascade(label='Convert', menu=filemenu)
    root.config(menu=menubar)

    ttk.Label(root, text='This application converts CSV files between Keychain standard format and Universal standard password format.', wraplength=400).pack()
    ttk.Label(root, text='Select which action you would like to execute').pack()

    ttk.Button(root, text='Apple to Universal', command=lambda: selectAppleToUniversal()).pack()
    ttk.Button(root, text='Universal to Apple', command=lambda: selectUniversalToApple()).pack()

    SetWindowCenterOfScreen(root, 400, 200)

    root.mainloop()

if __name__ == '__main__':
    main()