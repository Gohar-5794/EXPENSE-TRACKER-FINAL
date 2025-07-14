# Page 2: Add Expense
#Added by Kamran Ali
class AddExpensePage(tk.Frame):
    def _init_(self, parent, controller):
        super()._init_(parent)

        tk.Label(self, text="Add New Expense", font=("Helvetica", 18)).pack(pady=20)

        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        self.category_var = tk.StringVar()
        self.amount_var = tk.StringVar()
        self.date_var = tk.StringVar()

        # Category
        tk.Label(form_frame, text="Category:", anchor='w', width=20).grid(row=0, column=0, pady=5, sticky='e')
        tk.Entry(form_frame, textvariable=self.category_var, width=30).grid(row=0, column=1, pady=5)

        # Amount
        tk.Label(form_frame, text="Amount:", anchor='w', width=20).grid(row=1, column=0, pady=5, sticky='e')
        tk.Entry(form_frame, textvariable=self.amount_var, width=30).grid(row=1, column=1, pady=5)

        # Date
        tk.Label(form_frame, text="Date (YYYY-MM-DD):", anchor='w', width=20).grid(row=2, column=0, pady=5, sticky='e')
        tk.Entry(form_frame, textvariable=self.date_var, width=30).grid(row=2, column=1, pady=5)

        # Buttons
        tk.Button(self, text="Save Expense", command=self.save_expense, width=20).pack(pady=10)
        tk.Button(self, text="⬅ Back", command=lambda: controller.show_frame("HomePage")).pack()

    def save_expense(self):
        category = self.category_var.get()
        amount = self.amount_var.get()
        date = self.date_var.get()

        if not category or not amount or not date:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
            return

        # Insert into DB
        conn = sqlite3.connect('expenses.db')
        c = conn.cursor()
        c.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)",
                  (category, amount, date))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Expense added successfully!")

        self.category_var.set("")
        self.amount_var.set("")
        self.date_var.set("")

