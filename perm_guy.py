import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from itertools import permutations
import sqlite3
from datetime import datetime

def generate_permutations():
    word = entry.get()
    if not word:
        messagebox.showerror("Error", "Please enter a word.")
        return

    # Generate permutations with timestamps
    perm_list = [''.join(perm) + f" ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})" for perm in permutations(word)]

    # Display permutations in the text box
    result_text.config(state='normal')
    result_text.delete(1.0, tk.END)
    for perm in perm_list:
        result_text.insert(tk.END, perm.split(' ')[0] + '\n')
    result_text.config(state='disabled')

def save_to_database():
    word = entry.get()
    if not word:
        messagebox.showerror("Error", "Please enter a word.")
        return

    # Connect to database
    conn = sqlite3.connect('whispers.db')
    c = conn.cursor()

    # Create table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS permutations (id INTEGER PRIMARY KEY, permutation TEXT)''')

    # Generate permutations
    perm_list = [''.join(perm) for perm in permutations(word)]

    # Insert permutations into database
    c.executemany('''INSERT INTO permutations (permutation) VALUES (?)''', [(perm,) for perm in perm_list])

    # Commit changes and close connection
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Permutations saved to database.")

def save_to_file():
    word = entry.get()
    if not word:
        messagebox.showerror("Error", "Please enter a word.")
        return

    # Generate permutations
    perm_list = [''.join(perm) for perm in permutations(word)]

    # Ask user to choose file path
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return  # User canceled file selection

    # Write permutations to the chosen file
    with open(file_path, 'w') as f:
        for perm in perm_list:
            f.write(perm + '\n')

    messagebox.showinfo("Success", f"Permutations saved to {file_path}.")

# Create the main window
root = tk.Tk()
root.title("Permutations Generator")
root.geometry("500x400")

# Padding
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# Create a text entry widget
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, pady=10, padx=10)

# Create a button to generate permutations
generate_button = tk.Button(root, text="Generate Permutations", command=generate_permutations)
generate_button.grid(row=0, column=1, pady=10)

# Create a scrolled text widget to display permutations
result_text = scrolledtext.ScrolledText(root, height=10, width=40)
result_text.grid(row=1, column=0, columnspan=2, pady=10, padx=10)
result_text.config(state='disabled')

# Create a button to save permutations to database
save_db_button = tk.Button(root, text="Save to Database", command=save_to_database)
save_db_button.grid(row=2, column=0, pady=10, padx=10, sticky="w")

# Create a button to save permutations to a text file
save_file_button = tk.Button(root, text="Save to Text File", command=save_to_file)
save_file_button.grid(row=2, column=1, pady=10, padx=10, sticky="e")

# Run the GUI event loop
root.mainloop()
