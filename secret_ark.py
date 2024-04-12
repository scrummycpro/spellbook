import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

def save_to_database():
    quark = quark_entry.get()
    if not quark:
        messagebox.showerror("Error", "Please enter a quark.")
        return

    # Connect to database
    conn = sqlite3.connect('whispers.db')
    c = conn.cursor()

    # Create table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS quarks (id INTEGER PRIMARY KEY, quark TEXT, timestamp TEXT)''')

    # Get current timestamp
    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert quark into database with timestamp
    c.execute('''INSERT INTO quarks (quark, timestamp) VALUES (?, ?)''', (quark, current_timestamp))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Clear the entry box
    quark_entry.delete(0, tk.END)

    # Show alert
    messagebox.showinfo("Success", "Quark saved.")

# Create the main window
root = tk.Tk()
root.title("Quark Saver")

# Create a label
label = tk.Label(root, text="Enter quark here:")
label.pack(pady=10)

# Create a text entry widget
quark_entry = tk.Entry(root, width=30)
quark_entry.pack()

# Create a button to save quark to database
save_button = tk.Button(root, text="Save to Database", command=save_to_database)
save_button.pack(pady=10)

# Run the GUI event loop
root.mainloop()
