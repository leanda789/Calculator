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
   # results = " ".join(calculation.split())


#Finding an operator
    operator = None
    for char in calculation:
        if char in "+-x^÷%√":
            operator = char
            break
    if not operator:
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, "Please enter a VALID input")
        return
    
#edit
    #Split into 2 values
    parts = calculation.split(operator)
    #if len(parts) != 2:
     #   textbox.delete("1.0", tk.END)
      #  textbox.insert(tk.END, "Please enter a valid input: ")
       # return 
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
            #results = value2 ** (1/value1)
        elif operator == "÷":
            if value2 == 0:
                textbox.delete("1.0", tk.END)
                textbox.insert(tk.END, "Error: Cannot divide by zero")
                return
            results = value1 / value2
        elif operator == "%":
            results = (value1 / 100) * value2
        
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, results)
    except ZeroDivisionError:
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, "Cannot divide by zero")

def clear():            
    textbox.delete("1.0", tk.END)

#GUI
root = tk.Tk() #instantiate an instance
root.geometry("500x500")#size of window
root.title("Iconic Calculator")
root.configure(bg='lightblue')

label = tk.Label(root, text="Heyyy! :)", font=('Arial', 20), fg='black')
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 23))
textbox.pack(padx=20, pady=8)

#Create frame for buttons
buttonsframe = tk.Frame(root, bg='lightgrey')
for i in range(4):
    buttonsframe.columnconfigure(i, weight=1)
for i in range(6):
    buttonsframe.rowconfigure(i,weight=1)
#buttonsframe.columnconfigure(0, weight=1)
#buttonsframe.columnconfigure(1, weight=1)
#buttonsframe.columnconfigure(2, weight=1)
#buttonsframe.columnconfigure(3, weight=1)

#Create the answer button
answer_button = tk.Button(root, text="Answer", font = ('Arial', 18), bg='green', fg='blue', command=calculate)
answer_button.pack(pady=10) #was 10

#Clear button
clear_button = tk.Button(root, text="Clear", font=('Arial', 18), fg='red', command=clear)
clear_button.pack(pady=10) #was 10


#Create number buttons
for i in range(1, 10):
    button = tk.Button(buttonsframe, text=str(i), font=('Arial', 18), bg='lightgray', command=lambda i=i: appendText(i))
    button.grid(row=(i-1)//3, column=(i-1)%3, sticky=tk.W+tk.E, padx=3, pady=3)

#Create zero button
b0 = tk.Button(buttonsframe, text="0", font=('Arial', 18),fg='orange', command=lambda: appendText(0))
b0.grid(row=3, column=1, sticky=tk.W+tk.E, padx=4, pady=2)

#Create operator buttons
operators = ["+", "-", "x", "÷"]
for i, o in enumerate(operators):
    button = tk.Button(buttonsframe, text=o, font=('Arial', 18), fg='lightblue', command=lambda o=o: appendText(o))
    #button.grid(row=i//2, column=3, sticky=tk.W+tk.E, padx=2,pady=2)
    button.grid(row=i, column=3, sticky=tk.W+tk.E, padx=2, pady=2)
    buttonsframe.pack(fill='x', padx=10, pady=20)

operators = ["%", "^",".", "√"]
for i, o in enumerate(operators):
    button = tk.Button(buttonsframe, text=o, font=('Arial', 18), fg='lightblue', command=lambda o=o: appendText(o))
    #button.grid(row=i//2, column=3, sticky=tk.W+tk.E, padx=2,pady=2)
    button.grid(row=5, column=(i-1)%4, sticky=tk.W+tk.E, padx=3, pady=3)
    buttonsframe.pack(fill='x', padx=10, pady=20)


root.mainloop()