import tkinter as tk
from tkinter import ttk, messagebox

def calculate_budget():
    # Validate input fields
    income_str = entry_income.get()
    if not income_str:
        messagebox.showerror("Error", "Please enter your income.")
        return
    
    if income_type.get() == "Hourly":
        hours_str = entry_hours.get()
        if not hours_str:
            messagebox.showerror("Error", "Please enter the hours worked per week.")
            return

    needs_percent_str = entry_needs_percent.get()
    if not needs_percent_str:
        messagebox.showerror("Error", "Please enter the percentage for Needs.")
        return
    
    wants_percent_str = entry_wants_percent.get()
    if not wants_percent_str:
        messagebox.showerror("Error", "Please enter the percentage for Wants.")
        return
    
    savings_percent_str = entry_savings_percent.get()
    if not savings_percent_str:
        messagebox.showerror("Error", "Please enter the percentage for Savings.")
        return
    
    # Convert input to appropriate types
    income = float(income_str)
    if income_type.get() == "Yearly":
        income /= 12  # Convert yearly income to monthly
    else:
        hours = float(hours_str)
        income *= hours * 4  # Multiply hourly rate by hours worked per week and weeks in a month

    needs_percent = float(needs_percent_str) / 100
    wants_percent = float(wants_percent_str) / 100
    savings_percent = float(savings_percent_str) / 100

    # Calculate budget breakdown
    needs = income * needs_percent
    wants = income * wants_percent
    savings = income * savings_percent

    # Update labels
    label_needs.config(text=f"Needs: ${needs:.2f}")
    label_wants.config(text=f"Wants: ${wants:.2f}")
    label_savings.config(text=f"Savings: ${savings:.2f}")

def calculate_expenses():
    # Validate input fields
    rent_str = entry_rent.get()
    if not rent_str:
        messagebox.showerror("Error", "Please enter your rent.")
        return
    
    cc_payments_str = entry_cc_payments.get()
    if not cc_payments_str:
        messagebox.showerror("Error", "Please enter your current credit card payments.")
        return
    
    savings_percent_str = entry_savings_percent_2.get()
    if not savings_percent_str:
        messagebox.showerror("Error", "Please enter the percentage for Savings.")
        return
    
    # Convert input to appropriate types
    rent = float(rent_str)
    cc_payments = float(cc_payments_str)
    savings_percent = float(savings_percent_str) / 100

    # Calculate total expenses
    total_expenses = rent + cc_payments

    # Calculate required income
    required_income_yearly = total_expenses / (1 - savings_percent)*12
    required_income_hourly = required_income_yearly / (40 * 4 * 12)  # Assuming 40 hours a week


    # Update label
    if income_display_type.get() == "Yearly":
        label_required_income.config(text=f"Required Income: ${required_income_yearly:.2f} per year")
    else:
        label_required_income.config(text=f"Required Income: ${required_income_hourly:.2f} per hour")

# Create main window
root = tk.Tk()
root.title("Budget Planning Tool")

# Create notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# First tab (budget calculator)
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Budget Calculator')

# Set default values
default_income = 50000  # Example yearly income
default_hours = 40  # Default hours worked per week
default_needs_percent = 50
default_wants_percent = 30
default_savings_percent = 20

# Create input fields and labels for budget calculator
label_income = ttk.Label(tab1, text="Income:")
label_income.grid(row=0, column=0, padx=10, pady=5)
entry_income = ttk.Entry(tab1)
entry_income.insert(0, default_income)
entry_income.grid(row=0, column=1, padx=10, pady=5)

income_type = tk.StringVar()
income_type.set("Yearly")
income_type_choices = ["Yearly", "Hourly"]
combo_income_type = ttk.Combobox(tab1, textvariable=income_type, values=income_type_choices, state="readonly", width=10)
combo_income_type.grid(row=0, column=2, padx=10, pady=5)

label_hours = ttk.Label(tab1, text="Hours Worked/Week:")
label_hours.grid(row=1, column=0, padx=10, pady=5)
entry_hours = ttk.Entry(tab1)
entry_hours.insert(0, default_hours)
entry_hours.grid(row=1, column=1, padx=10, pady=5)

label_needs_percent = ttk.Label(tab1, text="Needs (%):")
label_needs_percent.grid(row=2, column=0, padx=10, pady=5)
entry_needs_percent = ttk.Entry(tab1)
entry_needs_percent.insert(0, default_needs_percent)
entry_needs_percent.grid(row=2, column=1, padx=10, pady=5)

label_wants_percent = ttk.Label(tab1, text="Wants (%):")
label_wants_percent.grid(row=3, column=0, padx=10, pady=5)
entry_wants_percent = ttk.Entry(tab1)
entry_wants_percent.insert(0, default_wants_percent)
entry_wants_percent.grid(row=3, column=1, padx=10, pady=5)

label_savings_percent = ttk.Label(tab1, text="Savings (%):")
label_savings_percent.grid(row=4, column=0, padx=10, pady=5)
entry_savings_percent = ttk.Entry(tab1)
entry_savings_percent.insert(0, default_savings_percent)
entry_savings_percent.grid(row=4, column=1, padx=10, pady=5)

button_calculate = ttk.Button(tab1, text="Calculate", command=calculate_budget)
button_calculate.grid(row=5, column=1, padx=10, pady=5)

# Create labels to display budget breakdown
label_needs = ttk.Label(tab1, text="Needs: $0.00")
label_needs.grid(row=6, column=0, padx=10, pady=5, sticky="w")
label_wants = ttk.Label(tab1, text="Wants: $0.00")
label_wants.grid(row=7, column=0, padx=10, pady=5, sticky="w")
label_savings = ttk.Label(tab1, text="Savings: $0.00")
label_savings.grid(row=8, column=0, padx=10, pady=5, sticky="w")

# Second tab (expenses calculator)
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Expenses Calculator')

# Set default value for income display type
income_display_type = tk.StringVar()
income_display_type.set("Yearly")

# Create input fields and labels for expenses calculator
label_rent = ttk.Label(tab2, text="Rent:")
label_rent.grid(row=0, column=0, padx=10, pady=5)
entry_rent = ttk.Entry(tab2)
entry_rent.grid(row=0, column=1, padx=10, pady=5)

label_cc_payments = ttk.Label(tab2, text="Current Credit Card Payments:")
label_cc_payments.grid(row=1, column=0, padx=10, pady=5)
entry_cc_payments = ttk.Entry(tab2)
entry_cc_payments.grid(row=1, column=1, padx=10, pady=5)

label_savings_percent_2 = ttk.Label(tab2, text="Savings (%):")
label_savings_percent_2.grid(row=2, column=0, padx=10, pady=5)
entry_savings_percent_2 = ttk.Entry(tab2)
entry_savings_percent_2.grid(row=2, column=1, padx=10, pady=5)

label_income_display = ttk.Label(tab2, text="Display Income As:")
label_income_display.grid(row=3, column=0, padx=10, pady=5)
combo_income_display = ttk.Combobox(tab2, textvariable=income_display_type, values=["Yearly", "Hourly"], state="readonly", width=10)
combo_income_display.grid(row=3, column=1, padx=10, pady=5)

button_calculate_expenses = ttk.Button(tab2, text="Calculate", command=calculate_expenses)
button_calculate_expenses.grid(row=4, column=1, padx=10, pady=5)

# Create label to display required income
label_required_income = ttk.Label(tab2, text="Required Income: $0.00")
label_required_income.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
