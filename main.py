from tkinter import *
from tkinter import ttk
from datetime import date, datetime
import calendar

def calculate_age():
    today = date.today()
    try:
        birth_date = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
        
        if birth_date > today:
            raise ValueError("Birth date cannot be in the future")
        
        age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        age_months = (today.month - birth_date.month) % 12
        age_days = (today - date(today.year, birth_date.month, birth_date.day)).days % 31
        
        day_of_week = calendar.day_name[birth_date.weekday()]
        
        result = f"{nameEntry.get()}, you are {age_years} years, {age_months} months, and {age_days} days old.\n"
        result += f"You were born on a {day_of_week}."
        
        resultLabel.config(text=result, fg="green")
    except ValueError as e:
        resultLabel.config(text=f"Error: {str(e)}", fg="red")

root = Tk()
root.geometry("600x700")
root.title("AGE CALCULATOR")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.theme_use('clam')

mainFrame = Frame(root, bg="#f0f0f0", padx=20, pady=20)
mainFrame.pack(expand=True, fill=BOTH)

titleLabel = Label(mainFrame, text="Age Calculator", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333333")
titleLabel.pack(pady=(0, 20))

inputFrame = Frame(mainFrame, bg="#f0f0f0")
inputFrame.pack(fill=X, pady=10)

labels = ["Name", "Year", "Month", "Day"]
entries = []

for i, label in enumerate(labels):
    Label(inputFrame, text=label, font=("Arial", 14), bg="#f0f0f0", fg="#555555").grid(row=i, column=0, sticky=W, pady=10)
    entry = Entry(inputFrame, font=("Arial", 14), width=25)
    entry.grid(row=i, column=1, padx=20, pady=10)
    entries.append(entry)

nameEntry, yearEntry, monthEntry, dayEntry = entries

calcButton = Button(mainFrame, text="Calculate Age", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", 
                    activebackground="#45a049", activeforeground="white", command=calculate_age)
calcButton.pack(pady=20)

resultLabel = Label(mainFrame, text="", font=("Arial", 14), bg="#f0f0f0", wraplength=500, justify=CENTER)
resultLabel.pack(pady=20)

root.mainloop()