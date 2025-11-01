import tkinter as tk
import math

#Append button value to the textbox
def appendText(value):
    current_text = textbox.get("1.0", tk.END).strip()
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, current_text + str(value))

#Perform calculations
def calculate():
    calculation = textbox.get("1.0", tk.END).strip()

#Sin function
    if calculation.startswith("sin"):
        try:
            num = float(calculation[3:])  # Get number after "sin"
            results = math.sin(math.radians(num)) #Converts from degrees to radians
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, results)
            return
        except:
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, "Express in the form: sin(value)")
            return
#Cos function        
    elif calculation.startswith("cos"):
        try:
            value = float(calculation[3:]) 
            results = math.cos(math.radians(value))
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, results)
            return
        except:
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, "Express in the form:  cos(value)")
            return
        
#Tan function       
    elif calculation.startswith("tan"):
        try:
            value = float(calculation[3:])
            results = math.tan(math.radians(value))
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, results)
            return
        except:
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, "Express in the form: tan(value)")
            return
    
  #FV (Future Value) = PV × (1 + r)^n
  #PV - the present value (initial investment)
  #r - the annual interest rate (decimal)
  #n - number of years the money is invested
  #So how much will your investment be worth in the future?
    if calculation.startswith("FV(") and calculation.endswith(")"):
        try:
            parts = calculation[3:-1].split(",")
            pv = float(parts[0])
            rate = float(parts[1])
            years = float(parts[2])
            results = pv * ((1 + rate) ** years)
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, f"£{results:,.2f}")
            return
        except:
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, "Express in the form: FV(pv,rate,years)")
            return
    
# ROI (Return on Investment) = [(Current - Cost) ÷ Cost] × 100
# ROI - a measure of profitability of an investment
# Current - the current value of the investment
# Cost - the initial amount invested
    elif calculation.startswith("ROI(") and calculation.endswith(")"):
        try:
            parts = calculation[4:-1].split(",")
            cost = float(parts[0])
            current = float(parts[1])
            result = ((current - cost) / cost) * 100
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, f"{result:.1f}%")
            return
        except:
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, "Express in the form: ROI(cost,current_value)")
            return
    
# Present Value: PV = FV ÷ (1 + r)^n
    elif calculation.startswith("PV(") and calculation.endswith(")"):
        try:
            parts = calculation[3:-1].split(",")
            fv = float(parts[0])
            rate = float(parts[1])
            years = float(parts[2])
            result = fv / ((1 + rate) ** years)
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, f"£{result:,.2f}")
            return
        except:
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, "Express in the form: PV(fv,rate,years)")
            return  
        
# Finding an operator
    operator = None
    for char in calculation:
        if char in "+-x^÷%√":
            operator = char
            break
    if not operator:
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, "Please enter a VALID input")
        return
    

# Split into 2 values
    parts = calculation.split(operator)
    if len(parts) == 1:
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END,f"Answer: {results}")
        return
    try:
        value1 = float(parts[0])
        value2 = float(parts[1])

        if operator == "+":
            results = value1 + value2
        elif operator == "-":
            results = value1 - value2
        elif operator == "x":
            results = value1 *  value2
        elif operator == "^":
            results = value1 ** value2
        elif operator == "√":
            results = value1*(math.sqrt(value2))
        elif operator == "÷":
            if value2 == 0:
                textbox.delete("1.0", tk.END)
                textbox.insert(tk.END, "Error: Cannot divide by zero")
                return
            results = value1 / value2
        elif operator == "%":
            results = (value1 / 100) * value2
        elif operator == "!":
            results = math.factorial(value1)
        
        
    
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, results)
    except ZeroDivisionError:
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, "Cannot divide by zero")

def clear():            
    textbox.delete("1.0", tk.END)

# GUI
root = tk.Tk() #instantiate an instance
root.geometry("600x550")#size of window
root.title("Iconic Calculator")
root.configure(bg='lightblue')

label = tk.Label(root, text="Heyyy! :)", font=('Arial', 20), fg='black')
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 23))
textbox.pack(padx=20, pady=8)

# Create buttonframe for buttons
buttonsframe = tk.Frame(root, bg='lightgrey')
for i in range(4):
    buttonsframe.columnconfigure(i, weight=1)
for i in range(6):
    buttonsframe.rowconfigure(i,weight=1)


# Create the answer button
answer_button = tk.Button(root, text="Answer", font = ('Arial', 18), bg='blue', fg='blue', command=calculate)
answer_button.pack(pady=10)

# Clear button
clear_button = tk.Button(root, text="Clear", font=('Arial', 18), fg='red', command=clear)
clear_button.pack(pady=10)


# Create number buttons
for i in range(1, 10):
    button = tk.Button(buttonsframe, text=str(i), font=('Arial', 18), bg='lightgrey', command=lambda i=i: appendText(i))
    button.grid(row=(i-1)//3, column=(i-1)%3, sticky=tk.W+tk.E, padx=3, pady=3)

# Create brackets buttons
button_brackets = [")", "("]
for i, o in enumerate(button_brackets):
    button = tk.Button(buttonsframe, text=o, font=('Arial', 18), fg='lightblue', command=lambda o=o: appendText(o))
    button.grid(row=3, column=(i-1)%2, sticky=tk.W+tk.E, padx=2, pady=2)
    buttonsframe.pack(fill='x', padx=10, pady=20)


# Create zero button
b0 = tk.Button(buttonsframe, text="0", font=('Arial', 18),fg='orange', command=lambda: appendText(0))
b0.grid(row=3, column=2, sticky=tk.W+tk.E, padx=4, pady=2)


# Create operator buttons
operators = ["+", "-", "x", "÷"]
for i, o in enumerate(operators):
    button = tk.Button(buttonsframe, text=o, font=('Arial', 18), fg='lightblue', command=lambda o=o: appendText(o))
    button.grid(row=i, column=3, sticky=tk.W+tk.E, padx=2, pady=2)
    buttonsframe.pack(fill='x', padx=10, pady=20)


# Create operator buttons
operators = ["%", "^",".", "√"]
for i, o in enumerate(operators):
    button = tk.Button(buttonsframe, text=o, font=('Arial', 18), fg='lightblue', command=lambda o=o: appendText(o))
    button.grid(row=5, column=(i-1)%4, sticky=tk.W+tk.E, padx=3, pady=3)
    buttonsframe.pack(fill='x', padx=10, pady=20)

# Create trigonometric buttons
operators = ["sin","cos","tan"]
for i, o in enumerate(operators):
    button = tk.Button(buttonsframe, text=o, font=('Arial', 18), fg='lightblue', command=lambda o=o: appendText(o))
    button.grid(row=6, column=(i-1)%3, sticky=tk.W+tk.E, padx=3, pady=3)
    buttonsframe.pack(fill='x', padx=4, pady=2)

# Create comma button
operators = [","]
for i, o in enumerate(operators):
    button = tk.Button(buttonsframe, text=o, font=('Arial', 18), fg='lightblue', command=lambda o=o: appendText(o))
    button.grid(row=6, column=3, sticky=tk.W+tk.E, padx=3, pady=3)
    buttonsframe.pack(fill='x', padx=4, pady=2)

# Financial buttons
financial_buttons = ["FV", "PV", "ROI", "PMT"]
for i, btn_text in enumerate(financial_buttons):
    button = tk.Button(buttonsframe, text=btn_text, font=('Arial', 14), bg='gold', fg='gold', command=lambda text=btn_text: appendText(text + "("))
    button.grid(row=7, column=(i-1)%4, sticky=tk.W+tk.E, padx=3, pady=3)
    buttonsframe.pack(fill='x', padx=4, pady=2)
root.mainloop()
