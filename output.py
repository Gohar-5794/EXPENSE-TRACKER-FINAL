# Summary Output Page
class SummaryPage(tk.Frame):
    def _init_(self, parent, controller):
        super()._init_(parent)
        tk.Label(self, text="📊 Expense Summary", font=("Helvetica", 18)).pack(pady=20)

        self.output_text = tk.Text(self, width=60, height=15)
        self.output_text.pack(pady=10)

        tk.Button(self, text="🔁 Generate Summary", command=self.generate_summary).pack(pady=5)
        tk.Button(self, text="⬅ Back", command=lambda: controller.show_frame("HomePage")).pack()

    def generate_summary(self):
        self.output_text.delete(1.0, tk.END)

        conn = sqlite3.connect('expenses.db')
        c = conn.cursor()

        c.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
        summary_data = c.fetchall()

        c.execute("SELECT SUM(amount) FROM expenses")
        total = c.fetchone()[0] or 0

        output = "Summary by Category:\n\n"
        for category, amount in summary_data:
            output += f"{category}: Rs. {amount:.2f}\n"

        output += f"\nTotal Spent: Rs. {total:.2f}"
        self.output_text.insert(tk.END, output)

        conn.close()


if _name_ == "_main_":
    app = ExpenseTrackerApp()
    app.mainloop()