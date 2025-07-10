# import os
# from datetime import datetime

# default_date = ""
# date_flag = False
# mode = "undefined"

# def set_default_date():
#     global default_date
#     global date_flag
#     print("\n\n1. Today's date\n2. Custom date\n")
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         default_date = datetime.today().strftime("%d-%m-%Y")
#     elif choice == "2":
#         default_date = input("Enter the default date (DD-MM-YYYY): ")
#     else:
#         print("Invalid choice.")
#         input("Press Enter to continue...")
#         return
    
#     default_date = convert_date(default_date)
#     date_flag = True
#     print("Default date set successfully.")
#     input("Press Enter to continue...")

# def convert_date(date_string):
#     date = datetime.strptime(date_string, "%d-%m-%Y")
#     return date.strftime("%d %B %Y")

# def add_stock():
#     stock_code = input("Enter the stock code name: ")
#     stock_code = stock_code.upper()
#     filename_short_term = "short_term/" + stock_code + ".txt"
#     filename_long_term = "long_term/" + stock_code + ".txt"
#     if os.path.exists(filename_short_term) or os.path.exists(filename_long_term):
#         print("Notes for this stock already exist.")
#         input("Press Enter to continue...")
#     else:
#         with open(filename_short_term, "w", encoding="utf-8") as f:
#             f.write("Notes for " + stock_code + "\n\n")
#         with open(filename_long_term, "w", encoding="utf-8") as f:
#             f.write("Notes for " + stock_code + "\n\n")

# def add_note(stock_code = ""):
#     global mode
#     if mode == "undefined":
#         print("Please set the mode first.")
#         input("Press Enter to continue...")
#         return
#     if stock_code == "":
#         stock_code = input("Enter the stock code name: ")
#     stock_code = stock_code.upper()
#     filename_short_term = "short_term/" + stock_code + ".txt"
#     filename_long_term = "long_term/" + stock_code + ".txt"
#     if os.path.exists(filename_short_term) and os.path.exists(filename_long_term):
#         note = input("Enter your note: ")
#         note = "- " + note
#         if(date_flag == False):
#             date = input("Enter the date (DD-MM-YYYY): ")
#             date = convert_date(date)
#         else:
#             date = default_date
#         if mode == "short":
#             with open(filename_short_term, "a", encoding="utf-8") as f:
#                 f.write(date + ": " + note + "\n")
#         elif mode == "long":
#             with open(filename_long_term, "a", encoding="utf-8") as f:
#                 f.write(date + ": " + note + "\n")
#         print("Note added successfully.")
#         input("Press Enter to continue...")

#     else:
#         print("Notes for this stock do not exist.")
#         input("Press Enter to continue...")

# def read_notes(stock_code = ""):
#     global mode
#     if mode == "undefined":
#         print("Please set the mode first.")
#         input("Press Enter to continue...")
#         return

#     if stock_code == "":
#         stock_code = input("Enter the stock code name: ")
#     filename_short_term = "short_term/" + stock_code + ".txt"
#     filename_long_term = "long_term/" + stock_code + ".txt"
#     if os.path.exists(filename_short_term) and os.path.exists(filename_long_term):
#         with open(filename_short_term, "r", encoding="utf-8") as f1, open(filename_long_term, "r", encoding="utf-8") as f2:
#             # if mode == "short":
#             #     print(f1.read())
#             # elif mode == "long":
#             #     print(f2.read())
#             print("\033[2J\033[1;1HSHORT TERM\n" + f1.read() + "\n------------------------------\nLONG TERM\n" + f2.read())
#             input("Press Enter to continue...")
#     else:
#         print("Notes for this stock do not exist.")
#         input("Press Enter to continue...")

# def list_companies():
#     i = 1
#     print("\033[2J\033[1;1HCompanies:\n")
#     for foldername, subfolders, filenames in os.walk('.'):
#         if 'short_term' in foldername:
#             for filename in filenames:
#                 if filename.endswith('.txt'):
#                     print(str(i) + ". " + filename[:-4])
#                     i += 1
#             choice = input("\nEnter the company number: ")
#             if int(choice) <= 0 or int(choice) >= i:
#                 print("Invalid choice.")
#                 input("Press Enter to continue...")
#                 return "invalid"
#             i = 1
#             for filename in filenames:
#                 if filename.endswith('.txt'):
#                     if i == int(choice):
#                         return filename[:-4]
#                     i += 1
# def read_all_notes():
#     filename_yatirim = r"C:\\Users\salih\Desktop\\AllNotes.txt"

#     with open(filename_yatirim, 'w', encoding="utf-8") as outfile:
#         for foldername, subfolders, filenames in os.walk('.'):
#             if 'short_term' in foldername:
#                 # outfile.write(f"\n{foldername}\n")
#                 for filename in filenames:
#                     if filename.endswith('.txt'):
#                         for _foldername, _subfolders, _filenames in os.walk('.'):
#                             if 'long_term' in _foldername:
#                                 for _filename in _filenames:
#                                     if filename == _filename:
#                                         with open(os.path.join(foldername, filename), 'r', encoding="utf-8") as readfile:
#                                             outfile.write("\nShort Term ")
#                                             outfile.write(readfile.read())
#                                             outfile.write('\n')
#                                         with open(os.path.join(_foldername, _filename), 'r', encoding="utf-8") as readfile:
#                                             outfile.write("\nLong Term ")
#                                             outfile.write(readfile.read())
#                                             outfile.write('\n')
#     print('All notes saved to YATIRIM.txt')

# # def read_all_notes_today():
# #     filename_yatirim = r"C:\Users\salih\Desktop\YATIRIM.txt"

# #     with open(filename_yatirim, 'w', encoding="utf-8") as outfile:
# #         for foldername, subfolders, filenames in os.walk('.'):
# #             if 'short_term' in foldername:
# #                 # outfile.write(f"\n{foldername}\n")
# #                 for filename in filenames:
# #                     if filename.endswith('.txt'):
# #                         for _foldername, _subfolders, _filenames in os.walk('.'):
# #                             if 'long_term' in _foldername:
# #                                 for _filename in _filenames:
# #                                     if filename == _filename:
# #                                         with open(os.path.join(foldername, filename), 'r', encoding="utf-8") as readfile:
# #                                             outfile.write("\nShort Term ")
# #                                             outfile.write(readfile.read())
# #                                             outfile.write('\n')
# #                                         with open(os.path.join(_foldername, _filename), 'r', encoding="utf-8") as readfile:
# #                                             outfile.write("\nLong Term ")
# #                                             outfile.write(readfile.read())
# #                                             outfile.write('\n')
# #     print('All notes saved to YATIRIM.txt')

# def dayNotes():
#     file_path = r"C:\\Users\salih\Desktop\\AllNotes.txt"
#     newlines = []
#     # substring = convert_date(substring)
#     if(default_date == ""):
#         print("Please set the date first.")
#         input("Press Enter to continue...")
#         return
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#     with open(r"C:\\Users\salih\Desktop\\TodayNotes.txt", 'w') as output_file:
#         for line in lines:
#             if default_date in line or "Term Notes for" in line:
#                 newlines.append(line)
#         for i in range(0, len(newlines) - 1):
#             if(not (newlines[i].startswith("Short Term") and newlines[i + 1].startswith("Long Term")
#                or newlines[i].startswith("Long Term") and newlines[i + 1].startswith("Short Term"))):
#                 if newlines[i].startswith("Short Term") or newlines[i].startswith("Long Term"):
#                     output_file.write("\n")
#                 output_file.write(newlines[i])
                

# def menu():
#     global mode
#     while True:
#         print("\033[2J\033[1;1H \nWelcome to Stock Notes" + "\n( {" + mode + "} term mode)" + "\n( {" + str(date_flag) + "} date flag)")
#         if(date_flag == True):
#             print("(Default date: " + default_date + ")")
#         print("------------------------------")
#         print("\n0. Set default date for notes")
#         print("1. Add new stock code name")
#         print("2. Add note about existing code name of a stock with date info")
#         print("3. Read specific code names of the stock notes that you took")
#         print("4. Switch mode")
#         print("5. List all companies")
#         print("6. Read all notes and save to YATIRIM.txt")
#         print("7. Read all notes and save to YATIRIM.txt (only today)")
#         print("8. Exit")
#         choice = input("\nEnter your choice: ")
#         if choice == "0":
#             set_default_date()
#         elif choice == "1":
#             add_stock()
#         elif choice == "2":
#             add_note()
#         elif choice == "3":
#             read_notes()
#         elif choice == "4":
#             if(mode != "long"):
#                 mode = "long"
#                 print("Switched to long-term mode.")
#             elif(mode != "short"):
#                 mode = "short"
#                 print("Switched to short-term mode.")
#         elif choice == "5":
#             company_code = list_companies()
#             if(company_code != "invalid"):
#                 while(True):
#                     print("1. Add note about existing code name of a stock with date info")
#                     print("2. Read specific code names of the stock notes that you took")
#                     selection = int(input())
#                     if(selection == 1):
#                         add_note(company_code)
#                     elif(selection == 2):
#                         read_notes(company_code)
#                     else: break
#         elif choice == "6":
#             read_all_notes()
#         elif choice == "7":
#             dayNotes()
#         elif choice == "8":
#             break
#         else:
#             print("Invalid choice. Please try again.")

# menu()

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
from datetime import datetime
import os

class StockNotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Notes Manager")
        self.root.geometry("1600x900")  # Adjusted for 2K resolution

        # Apply a theme
        self.style = ttk.Style()
        # Import the tcl file with the tk.call method
        root.tk.call('source', 'forestTheme\\forest-light.tcl')  # Put here the path of your theme file

        # Set the theme with the theme_use method
        ttk.Style().theme_use('forest-light')

        # Customize the style for buttons
        card = ttk.Frame(root, style='Card', padding=(5, 6, 7, 8))
        self.style.configure('Accent.TButton', padding=10)
        self.style.map('Accent.TButton', )

        # Initialize application variables
        self.mode = tk.StringVar(value="undefined")
        self.default_date = tk.StringVar(value="")
        self.date_flag = tk.BooleanVar(value=False)

        # Setup the GUI layout
        self.setup_gui()

    def setup_gui(self):
        # Mode and Date Display
        mode_frame = ttk.Frame(self.root)
        mode_frame.pack(pady=10)
        ttk.Label(mode_frame, text="Mode: ").pack(side=tk.LEFT)
        ttk.Label(mode_frame, textvariable=self.mode).pack(side=tk.LEFT)
        ttk.Label(mode_frame, text=" | Default Date: ").pack(side=tk.LEFT)
        ttk.Label(mode_frame, textvariable=self.default_date).pack(side=tk.LEFT)

        # Buttons for actions
        actions_frame = ttk.Frame(self.root)
        actions_frame.pack(pady=10, fill=tk.X)
        ttk.Button(actions_frame, text="Set Default Date", command=self.set_default_date).pack(fill=tk.X)
        ttk.Button(actions_frame, text="Switch Mode", command=self.switch_mode).pack(fill=tk.X)
        ttk.Button(actions_frame, text="List All Companies", command=self.list_companies_gui).pack(fill=tk.X)
        ttk.Button(actions_frame, text="Add New Stock Code", command=self.add_stock_gui).pack(fill=tk.X)
        ttk.Button(actions_frame, text="Add Note", command=self.add_note_gui).pack(fill=tk.X)
        ttk.Button(actions_frame, text="Read Notes", command=self.read_notes_gui).pack(fill=tk.X)
        ttk.Button(actions_frame, text="Read All Notes", command=self.read_all_notes_gui).pack(fill=tk.X)
        ttk.Button(actions_frame, text="Exit", command=self.exit_app).pack(fill=tk.X)

    def exit_app(self):
        self.root.quit()

    # Placeholder for additional helper functions

    def set_default_date(self):
        date_choice = simpledialog.askstring("Set Default Date", "Choose date option:\n1. Today's date\n2. Custom date\nEnter your choice (1 or 2):")
        if date_choice == "1":
            self.default_date.set(datetime.today().strftime("%d-%m-%Y"))
            self.date_flag.set(True)
        elif date_choice == "2":
            custom_date = simpledialog.askstring("Custom Date", "Enter the default date (DD-MM-YYYY):")
            try:
                # Validate and set custom date
                datetime.strptime(custom_date, "%d-%m-%Y")
                self.default_date.set(custom_date)
                self.date_flag.set(True)
            except ValueError:
                messagebox.showerror("Error", "Invalid date format. Please use DD-MM-YYYY.")
        else:
            messagebox.showinfo("Cancelled", "Default date setting cancelled.")

    def add_stock_gui(self):
        stock_code = simpledialog.askstring("Add Stock Code", "Enter the stock code name:")
        if stock_code:
            stock_code = stock_code.upper()
            filename_short_term = "short_term/" + stock_code + ".txt"
            filename_long_term = "long_term/" + stock_code + ".txt"
            if os.path.exists(filename_short_term) or os.path.exists(filename_long_term):
                messagebox.showinfo("Info", "Notes for this stock already exist.")
            else:
                with open(filename_short_term, "w", encoding="utf-8") as f:
                    f.write("Notes for " + stock_code + "\n\n")
                with open(filename_long_term, "w", encoding="utf-8") as f:
                    f.write("Notes for " + stock_code + "\n\n")
                messagebox.showinfo("Success", "Stock code added successfully.")

    def add_note_gui(self, stock_code=""):
        if self.mode.get() == "undefined":
            messagebox.showwarning("Warning", "Please set the mode first.")
            return

        if not stock_code:
            stock_code = simpledialog.askstring("Add Note", "Enter the stock code name:")

        if stock_code:
            self.add_note_for_stock_code(stock_code.upper())

    def add_note_for_stock_code(self, stock_code):
        if self.mode.get() == "undefined":
            messagebox.showerror("Error", "Mode is undefined. Please set the mode first.")
            return

        # Ensure stock code is provided
        if not stock_code:
            messagebox.showerror("Error", "No stock code provided.")
            return
        
        # Asking for the note
        note = simpledialog.askstring("Add Note", "Enter your note for " + stock_code + ":")
        if not note:  # User cancelled or entered an empty note
            return

        # Preparing filenames based on mode
        filename = f"{'short_term' if self.mode.get() == 'short' else 'long_term'}/{stock_code.upper()}.txt"
        if not os.path.exists(filename):
            messagebox.showerror("Error", f"Notes file for {stock_code} does not exist.")
            return

        # Date handling
        if self.date_flag.get():
            note_date = self.default_date.get()
        else:
            note_date = simpledialog.askstring("Note Date", "Enter the date for the note (DD-MM-YYYY):")
            try:
                #change the date format to string month instead of number
                note_date = datetime.strptime(note_date, "%d-%m-%Y").strftime("%d %B %Y")
                datetime.strptime(note_date, "%d-%m-%Y")  # Validate date format
                self.default_date.set(note_date)  # Optionally update the default_date
            except ValueError:
                messagebox.showerror("Error", "Invalid date format. Please use DD-MM-YYYY.")
                return

        # Writing the note to the file
        try:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(f"{note_date}: {note}\n")
            messagebox.showinfo("Success", "Note added successfully for " + stock_code + ".")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add note for {stock_code}. Error: {str(e)}")


    def switch_mode(self):
        if self.mode.get() != "long":
            self.mode.set("long")
            messagebox.showinfo("Mode Switched", "Switched to long-term mode.")
        else:
            self.mode.set("short")
            messagebox.showinfo("Mode Switched", "Switched to short-term mode.")

    def read_notes_gui(self):
        if self.mode.get() == "undefined":
            messagebox.showwarning("Warning", "Please set the mode first.")
            return

        stock_code = simpledialog.askstring("Read Notes", "Enter the stock code name:")
        if stock_code:
            stock_code = stock_code.upper()
            filename_short_term = "short_term/" + stock_code + ".txt"
            filename_long_term = "long_term/" + stock_code + ".txt"
            
            if not os.path.exists(filename_short_term) or not os.path.exists(filename_long_term):
                messagebox.showerror("Error", "Notes for this stock do not exist.")
                return
            
            # Create a new window to display the notes
            notes_window = tk.Toplevel(self.root)
            notes_window.title(f"Notes for {stock_code}")
            text_area = tk.Text(notes_window, wrap="word")
            text_area.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
            
            with open(filename_short_term, "r", encoding="utf-8") as f_short, open(filename_long_term, "r", encoding="utf-8") as f_long:
                short_term_notes = f_short.read()
                long_term_notes = f_long.read()
                notes_content = f"SHORT TERM\n{short_term_notes}\n------------------------------\nLONG TERM\n{long_term_notes}"
                text_area.insert(tk.END, notes_content)
                text_area.config(state=tk.DISABLED)  # Make the text area read-only

    def list_companies_gui(self):
        companies_window = tk.Toplevel(self.root)
        companies_window.title("List of Companies")
        companies_window.geometry("800x600")  # Adjusted size
        lb = tk.Listbox(companies_window, width=50, height=25)  # Optionally adjust Listbox size
        lb.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        companies = []
        for foldername, _, filenames in os.walk('.'):
            if 'short_term' in foldername or 'long_term' in foldername:
                for filename in filenames:
                    if filename.endswith('.txt'):
                        company = filename[:-4].upper()
                        if company not in companies:
                            companies.append(company)
                            lb.insert(tk.END, company)
        
        lb.bind('<<ListboxSelect>>', lambda event: self.on_company_selected(event, lb, companies_window))

    def on_company_selected(self, event, lb, window):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            stock_code = event.widget.get(index)
            window.destroy()  # Close the selection window

            self.read_notes_gui_for_company(stock_code)



    def read_all_notes_gui(self):
        filename_yatirim = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not filename_yatirim:
            return  # User cancelled the save dialog
        
        with open(filename_yatirim, 'w', encoding="utf-8") as outfile:
            for foldername, _, filenames in os.walk('.'):
                if 'short_term' in foldername:
                    for filename in filenames:
                        if filename.endswith('.txt'):
                            with open(os.path.join(foldername, filename), 'r', encoding="utf-8") as readfile:
                                outfile.write(f"\nShort Term for {filename[:-4]}\n")
                                outfile.write(readfile.read())
                elif 'long_term' in foldername:
                    for filename in filenames:
                        if filename.endswith('.txt'):
                            with open(os.path.join(foldername, filename), 'r', encoding="utf-8") as readfile:
                                outfile.write(f"\nLong Term for {filename[:-4]}\n")
                                outfile.write(readfile.read())
        
        messagebox.showinfo("Success", "All notes saved successfully.")

    def read_notes_gui_for_company(self, stock_code):
        if not stock_code:
            messagebox.showerror("Error", "No stock code provided.")
            return

        stock_code = stock_code.upper()
        filename_short_term = f"short_term/{stock_code}.txt"
        filename_long_term = f"long_term/{stock_code}.txt"
        
        if not os.path.exists(filename_short_term) or not os.path.exists(filename_long_term):
            messagebox.showerror("Error", "Notes for this stock do not exist.")
            return
        
        # Create a new window to display the notes
        notes_window = tk.Toplevel(self.root)
        notes_window.title(f"Notes for {stock_code}")
        notes_window.geometry("1400x800")  # Adjusted size
        
        # Text area for displaying notes
        text_area = tk.Text(notes_window, wrap="word", height=40, width=100)  # Optionally adjust the initial size
        text_area.pack(padx=10, pady=10, expand=True, fill=tk.BOTH, side=tk.TOP)
        
        try:
            with open(filename_short_term, "r", encoding="utf-8") as f_short, open(filename_long_term, "r", encoding="utf-8") as f_long:
                short_term_notes = f_short.read()
                long_term_notes = f_long.read()
                notes_content = f"SHORT TERM\n{short_term_notes}\n------------------------------\nLONG TERM\n{long_term_notes}"
                text_area.insert(tk.END, notes_content)
                text_area.config(state=tk.DISABLED)  # Make the text area read-only
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read notes for {stock_code}. Error: {str(e)}")

        def refresh_notes_display():
            """Fetch and update the notes content in the text area."""
            text_area.config(state=tk.NORMAL)
            text_area.delete(1.0, tk.END)  # Clear existing content
            try:
                with open(filename_short_term, "r", encoding="utf-8") as f_short, open(filename_long_term, "r", encoding="utf-8") as f_long:
                    short_term_notes = f_short.read()
                    long_term_notes = f_long.read()
                    notes_content = f"SHORT TERM\n{short_term_notes}\n------------------------------\nLONG TERM\n{long_term_notes}"
                    text_area.insert(tk.END, notes_content)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read notes for {stock_code}. Error: {str(e)}")
            text_area.config(state=tk.DISABLED)
        
        refresh_notes_display()  # Initial display of notes
        
        # Button for adding a new note for this stock code
        button_frame = ttk.Frame(notes_window)  # Frame to hold the button, for layout purposes
        button_frame.pack(padx=10, pady=10, fill=tk.X, side=tk.BOTTOM)

            # Frame for buttons
        button_frame = ttk.Frame(notes_window)
        button_frame.pack(padx=10, pady=10, fill=tk.X, side=tk.BOTTOM)
        
        # Button to manually refresh the notes after adding
        refresh_button = ttk.Button(button_frame, text="Refresh Notes", command=refresh_notes_display)
        refresh_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Modify the existing add note button to not immediately attempt to refresh
        add_note_button = ttk.Button(button_frame, text="Add Note for This Stock", command=lambda: self.add_note_gui(stock_code))
        add_note_button.pack(side=tk.RIGHT, padx=10, pady=10)

def main():
    root = tk.Tk()
    root.geometry("1600x900")  # Adjust as needed for 2K resolution
    app = StockNotesApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()