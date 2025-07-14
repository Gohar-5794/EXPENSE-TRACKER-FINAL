    
    # added by younis mujahid(f2023105222)
    # age 1: Home
class HomePage(tk.Frame):
    def _init_(self, parent, controller):
        super()._init_(parent)
        tk.Label(self, text="💰 Expense Tracker", font=("Helvetica", 20)).pack(pady=30)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="➕ Add Expense", command=lambda: controller.show_frame("AddExpensePage"),
                  width=20).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(btn_frame, text="📋 View Expenses", command=lambda: controller.show_frame("ViewExpensesPage"),
                  width=20).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(btn_frame, text="📊 Show Summary", command=lambda: controller.show_frame("SummaryPage"),
                  width=20).grid(row=2, column=0, padx=10, pady=10)
