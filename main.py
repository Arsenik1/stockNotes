import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
from datetime import datetime
import os

class StockNotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Notes Manager")
        self.root.geometry("1600x900")  # Adjusted for 2K resolution

        # Ensure required directories exist
        os.makedirs('short_term', exist_ok=True)
        os.makedirs('long_term', exist_ok=True)

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
                # Validate date format and then reformat to string month
                datetime.strptime(note_date, "%d-%m-%Y")  # Validate date format
                note_date = datetime.strptime(note_date, "%d-%m-%Y").strftime("%d %B %Y")
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