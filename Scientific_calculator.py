import tkinter as tk
import math
import re

calculation = "" # Αρχικοποίση
angle_unit= "Deg" # Αρχική τιμή
memory_value = 0


def update_screen():
    text_result.delete(1.0, "end")
    text_result.insert(1.0,display_form())

def display_form():
    global calculation
    disp_f = calculation
    if (len(calculation)> 20):
        disp_f = re.sub(r'\d+\.?\d*', lambda x: "{:.5e}".format(float(x.group())), calculation)
    return disp_f

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    update_screen()


def alter_str(string):

    
    #pi
    string = re.sub(r'(π)', lambda x: str(math.pi), string)
    #e
    string = re.sub(r'(e)', lambda x: str(math.e), string)
    #root
    string = re.sub(r'(\d+)√(\d+)', lambda x: str(float(x.group(2)) ** (1 / int(x.group(1)))), string)
    #power
    string = re.sub(r'(\d+)\^(\d+)', lambda x: str(float(x.group(1)) ** int(x.group(2))), string)
    #log
    string = re.sub(r'log\((\d+(\.\d+)?)\)', lambda x: str(math.log(float(x.group(1)))), string)
    #log10
    string = re.sub(r'log10\((\d+(\.\d+)?)\)', lambda x:str(math.log10(float(x.group(1)))), string)
    #factorial
    string = re.sub(r'(\d+)!', lambda x:str(math.factorial(int(x.group(1)))), string)
    #sin
    if(angle_unit=="Deg"):
        string = re.sub(r'sin\((\d+(\.\d+)?)\)', lambda x: str(math.sin(math.radians(float(x.group(1))))), string)
    else:
        string = re.sub(r'sin\((\d+(\.\d+)?)\)', lambda x: str(math.sin(float(x.group(1)))), string)
    #cos
    if(angle_unit=="Deg"):
        string = re.sub(r'cos\((\d+(\.\d+)?)\)', lambda x: str(math.cos(math.radians(float(x.group(1))))), string)
    else:
        string = re.sub(r'cos\((\d+(\.\d+)?)\)', lambda x: str(math.cos(float(x.group(1)))), string)
    #tan
    if(angle_unit=="Deg"):
        string = re.sub(r'tan\((\d+(\.\d+)?)\)', lambda x: str(math.tan(math.radians(float(x.group(1))))), string)   
    else:
        string = re.sub(r'tan\((\d+(\.\d+)?)\)',  lambda x: str(math.tan(float(x.group(1)))), string)
    #sinh
    if(angle_unit=="Deg"):
        string = re.sub(r'sinh\((\d+(\.\d+)?)\)', lambda x: str(math.sinh(math.radians(float(x.group(1))))), string)
    else:
        string = re.sub(r'sinh\((\d+(\.\d+)?)\)', lambda x: str(math.sinh(float(x.group(1)))), string)
    #cosh
    if(angle_unit=="Deg"):
        string = re.sub(r'cosh\((\d+(\.\d+)?)\)', lambda x: str(math.cosh(math.radians(float(x.group(1))))), string)
    else:
        string = re.sub(r'cosh\((\d+(\.\d+)?)\)', lambda x: str(math.cosh(float(x.group(1)))), string)
    #tanh
    if(angle_unit=="Deg"):
        string = re.sub(r'tanh\((\d+(\.\d+)?)\)', lambda x: str(math.tanh(math.radians(float(x.group(1))))), string)   
    else:
        string = re.sub(r'tanh\((\d+(\.\d+)?)\)', lambda x: str(math.tanh(float(x.group(1)))), string)
    return string



#Διαβάζει το string 
def evaluate_calculation():
    global calculation
    calculation = alter_str(calculation)

    try:
        calculation = str(eval(calculation))
        update_screen()
    except:
        clear_field()
        text_result.insert(1.0, "Error")
        
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def back_Space():
    global calculation
    calculation = calculation[:-1]
    update_screen()

def Root():
    global calculation
    pattern = r"(\d+|\(([^()]+)\))[^(]*$"
    match = re.search(pattern, calculation)
    if match:
        if match.group(2):
            temp = eval(alter_str(match.group(2)))
            calculation = re.sub(pattern, lambda x: f"√({temp})", calculation)
        else:   
            calculation = re.sub(r'\d+(\.\d+)?$', lambda x: f"√{x.group(0)}", calculation)
    update_screen()

def Log():
    global calculation
    pattern = r"(\d+|\(([^()]+)\))[^(]*$"
    match = re.search(pattern, calculation)
    if match:
        if match.group(2):
            temp = eval(alter_str(match.group(2)))
            calculation = re.sub(pattern, lambda x: f"log({temp})", calculation)
        else:   
            calculation = re.sub(r'\d+(\.\d+)?$', lambda x: f"log({x.group(0)})", calculation)
    update_screen()

def Log10():
    global calculation
    pattern = r"(\d+|\(([^()]+)\))[^(]*$"
    match = re.search(pattern, calculation)
    if match:
        if match.group(2):
            temp = eval(alter_str(match.group(2)))
            calculation = re.sub(pattern, lambda x: f"log10({temp})", calculation)
        else:
            calculation = re.sub(r'\d+(\.\d+)?$',lambda x: f"log10({x.group(0)})", calculation)   
    update_screen()

    
def rev():
    global calculation
    pattern = r"(\d+|\(([^()]+)\))[^(]*$"
    match = re.search(pattern, calculation)
    if match.group(2):
            temp = eval(alter_str(match.group(2)))
            calculation = re.sub(pattern, lambda x: f"1/({temp})", calculation)
    else:
        calculation = re.sub(r'\d+(\.\d+)?$',lambda x: f"1/({x.group(0)})", calculation)
    update_screen()

def Sin():
    global calculation
    pattern = r"(\d+|\(([^()]+)\))[^(]*$"
    match = re.search(pattern, calculation)
    if match.group(2):
        temp = eval(alter_str(match.group(2)))
        calculation = re.sub(pattern, lambda x: f"sin({temp})", calculation)
    else:
        calculation = re.sub(r'\d+(\.\d+)?$',lambda x: f"sin({x.group(0)})", calculation)
    update_screen()

def Cos():
    global calculation
    pattern = r"(\d+|\(([^()]+)\))[^(]*$"
    match = re.search(pattern, calculation)
    if match.group(2):
        temp = eval(alter_str(match.group(2)))        
        calculation = re.sub(pattern,lambda x: f"cos({temp})", calculation)
    else:
        calculation = re.sub(r'\d+(\.\d+)?$',lambda x: f"cos({x.group(0)})", calculation)
    update_screen()

def Taaan():
    global calculation
    pattern = r"(\d+|\(([^()]+)\))[^(]*$"
    match = re.search(pattern, calculation)
    if match.group(2):
        temp = eval(alter_str(match.group(2))) 
        calculation = re.sub(pattern,lambda x: f"tan({temp})", calculation)
    else:
        calculation = re.sub(r'\d+(\.\d+)?$',lambda x: f"tan({x.group(0)})", calculation)
    update_screen()

def Sinh():
    global calculation
    pattern = r"(\d+|\(([^()]+)\))[^(]*$"
    match = re.search(pattern, calculation)
    if match.group(2):
        temp = eval(alter_str(match.group(2)))
        calculation = re.sub(pattern, lambda x: f"sinh({temp})", calculation)
    else:
        calculation = re.sub(r'\d+(\.\d+)?$',lambda x: f"sinh({x.group(0)})", calculation)
    update_screen()

def Cosh():
    global calculation
    pattern = r"(\d+|\(([^()]+)\))[^(]*$"
    match = re.search(pattern, calculation)
    if match.group(2):
        temp = eval(alter_str(match.group(2)))        
        calculation = re.sub(pattern,lambda x: f"cosh({temp})", calculation)
    else:
        calculation = re.sub(r'\d+(\.\d+)?$',lambda x: f"cosh({x.group(0)})", calculation)
    update_screen()

def Tanh():
    global calculation
    pattern = r"(\d+|\(([^()]+)\))[^(]*$"
    match = re.search(pattern, calculation)
    if match.group(2):
        temp = eval(alter_str(match.group(2))) 
        calculation = re.sub(pattern,lambda x: f"tanh({temp})", calculation)
    else:
        calculation = re.sub(r'\d+(\.\d+)?$',lambda x: f"tanh({x.group(0)})", calculation)
    update_screen()

def open_programmer_window():
    row_num = 2
    col_num = 0

    programmer_window = tk.Toplevel(root)
    programmer_window.title("Programmer")
    programmer_window.geometry("310x560")  # Αλλάξαμε το μέγεθος του παραθύρου
    programmer_window.config(bg="powderblue")

    def convert_number(*args):
        try:
            number = entry_number.get()
            selected_system = conversion_menu.get()
            result_label.config(text="")
            
            if selected_system == "Decimal":
                decimal = int(number)
            elif selected_system == "Binary":
                decimal = int(number, 2)
            elif selected_system == "Octal":
                decimal = int(number, 8)
            elif selected_system == "Hexadecimal":
                decimal = int(number, 16)
            
            binary = bin(decimal)[2:]
            octal = oct(decimal)[2:]
            hexadecimal = hex(decimal)[2:].upper()
            result_label.config(text=f"Decimal: {decimal}\nBinary: {binary}\nOctal: {octal}\nHexadecimal: {hexadecimal}")
        except ValueError:
            result_label.config(text="Invalid input")
            
    def clear_all():
        entry_number.delete(0, tk.END)
        result_label.config(text="")
        
    def add_number(number):
        entry_number.insert(tk.END, str(number))
        convert_number()  # Καλεί τη συνάρτηση μετατροπής μετά την προσθήκη αριθμού

    def clear_last_digit():
        current_value = entry_number.get()
        if current_value:
            entry_number.delete(len(current_value) - 1, tk.END)
            convert_number()
            
    entry_number = tk.Entry(programmer_window, font=("Arial", 14), bg="powderblue",bd=15,relief="sunken")
    entry_number.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    # Dropdown menu
    conversion_options = ["Decimal", "Binary", "Octal", "Hexadecimal"]
    conversion_menu = tk.StringVar(programmer_window)
    conversion_menu.set(conversion_options[0])  # Ορίζει την προεπιλεγμένη επιλογή
    conversion_dropdown = tk.OptionMenu(programmer_window, conversion_menu, *conversion_options)
    conversion_dropdown.grid(row=1, column=0, columnspan=5, padx=10, pady=10)
    conversion_dropdown.config(bg="powderblue", fg="black", activebackground="powderblue", activeforeground="black")
   

    # Buttons
    btn_7 = tk.Button(programmer_window, text="7", command=lambda: add_number(7), width=6, font=("Arial", 14,'bold'),bg="white",fg="black")
    btn_7.grid(row=2, column=0, padx=6, pady=6)
    btn_8 = tk.Button(programmer_window, text="8", command=lambda: add_number(8), width=6, font=("Arial", 14,'bold'),bg="white",fg="black")
    btn_8.grid(row=2, column=1, padx=6, pady=6)
    btn_9 = tk.Button(programmer_window, text="9", command=lambda: add_number(9), width=6, font=("Arial", 14,'bold'),bg="white",fg="black")
    btn_9.grid(row=2, column=2, padx=6, pady=6)
    
    btn_4 = tk.Button(programmer_window, text="4", command=lambda: add_number(4), width=6, font=("Arial", 14,'bold'),bg="white",fg="black")
    btn_4.grid(row=3, column=0, padx=6, pady=6)
    btn_5 = tk.Button(programmer_window, text="5", command=lambda: add_number(5), width=6, font=("Arial", 14,'bold'),bg="white",fg="black")
    btn_5.grid(row=3, column=1, padx=6, pady=6)
    btn_6 = tk.Button(programmer_window, text="6", command=lambda: add_number(6), width=6, font=("Arial", 14,'bold'),bg="white",fg="black")
    btn_6.grid(row=3, column=2, padx=6, pady=6)
    
    btn_1 = tk.Button(programmer_window, text="1", command=lambda: add_number(1), width=6, font=("Arial", 14,'bold'),bg="white",fg="black")
    btn_1.grid(row=4, column=0, padx=6, pady=6)
    btn_2 = tk.Button(programmer_window, text="2", command=lambda: add_number(2), width=6, font=("Arial", 14,'bold'),bg="white",fg="black")
    btn_2.grid(row=4, column=1, padx=6, pady=6)
    btn_3 = tk.Button(programmer_window, text="3", command=lambda: add_number(3), width=6, font=("Arial", 14,'bold'),bg="white",fg="black")
    btn_3.grid(row=4, column=2, padx=6, pady=6)
    
    btn_AC = tk.Button(programmer_window, text="AC", command=clear_all, width=6, font=("Arial", 14,'bold'),bg="powderblue",fg="black")
    btn_AC.grid(row=5, column=0, padx=6, pady=6)
    btn_0 = tk.Button(programmer_window, text="0", command=lambda: add_number(0), width=6, font=("Arial", 14,'bold'),bg="white",fg="black")
    btn_0.grid(row=5, column=1, padx=6, pady=6)
    btn_back = tk.Button(programmer_window, text="<<", command=clear_last_digit, width=6, font=("Arial", 14,'bold'),bg="powderblue",fg="black")
    btn_back.grid(row=5, column=2, padx=6, pady=6)
    
    # Hexadecimal buttons
    btn_A = tk.Button(programmer_window, text="A", command=lambda: add_number("A"), width=6, font=("Arial", 14,'bold'),bg="powderblue",fg="black")
    btn_A.grid(row=6, column=0, padx=6, pady=6)
    btn_B = tk.Button(programmer_window, text="B", command=lambda: add_number("B"), width=6, font=("Arial", 14,'bold'),bg="powderblue",fg="black")
    btn_B.grid(row=6, column=1, padx=6, pady=6)
    btn_C = tk.Button(programmer_window, text="C", command=lambda: add_number("C"), width=6, font=("Arial", 14,'bold'),bg="powderblue",fg="black")
    btn_C.grid(row=6, column=2, padx=6, pady=6)
    btn_D = tk.Button(programmer_window, text="D", command=lambda: add_number("D"), width=6, font=("Arial", 14,'bold'),bg="powderblue",fg="black")
    btn_D.grid(row=7, column=0, padx=6, pady=6)
    btn_E = tk.Button(programmer_window, text="E", command=lambda: add_number("E"), width=6, font=("Arial", 14,'bold'),bg="powderblue",fg="black")
    btn_E.grid(row=7, column=1, padx=6, pady=6)
    btn_F = tk.Button(programmer_window, text="F", command=lambda: add_number("F"), width=6, font=("Arial", 14,'bold'),bg="powderblue",fg="black")
    btn_F.grid(row=7, column=2, padx=6, pady=6)
    
    entry_number.bind("<KeyRelease>", convert_number)
    
    result_label = tk.Label(programmer_window, font=("Arial", 12),bg="powderblue",fg="black")
    result_label.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

##Memory

def memory_add():   #(M+)
    global memory_value
    memStr = alter_str(calculation)
    try:
        memory_value += float(eval(memStr))
        text_result_memory.delete(1.0, "end")
        text_result_memory.insert(1.0, memory_value)
    except:
        text_result_memory.insert(1.0,"Error")
        
    
def memory_recall():    #(MR)
    global memory_value
    global calculation
    add_to_calculation(memory_value)

def memory_clear():     #(MC)
    global memory_value

    text_result_memory.delete(1.0, "end")
    memory_value = 0

def measurement_unit():
    global angle_unit
    if(angle_unit=="Deg"):
        angle_unit = "Rad"
    else:
        angle_unit = "Deg"
    btn_angl.configure(text=f"{angle_unit}")

def change_sign():
    global calculation
    if calculation and calculation[0] == '-':
        calculation = calculation[1:]
    else:
        calculation = '-' + calculation
    update_screen()

#Window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("562x590")
root.configure(bg="powderblue")


text_result = tk.Text(root, height=2, width=28, font=("Arial", 24), bg="powderblue",bd=25,relief="sunken")
text_result.grid(row = 0, columnspan=6)

#menu

menubutton = tk.Menubutton(root, text="Trigonometry V",bg="powderblue",fg="black")
menubutton.grid(row=6)

# Προσθήκη μενού "File"
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="Mode", menu=file_menu) 
file_menu.add_command(label="Open Programmer", command=open_programmer_window)


##Memory
text_result_memory = tk.Text(root, height=1, width=30, font=("Arial",24))
text_result_memory.grid(row=1 , columnspan=6)

##Memory buttons
btn_Mplus = tk.Button(root, text="M+",command = memory_add , width=6, font=("Arial", 20,'bold'),bg="white",fg="black")
btn_Mplus.grid(row=3, column=2)
btn_MR = tk.Button(root, text="MR", command = memory_recall, width=6, font=("Arial", 20,'bold'),bg="white",fg="black")
btn_MR.grid(row=3, column=3)
btn_MC = tk.Button(root, text="MC", command = memory_clear, width=6, font=("Arial", 20,'bold'),bg="white",fg="black")
btn_MC.grid(row=3, column=4)


#Buttons
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=6, font=("Arial", 20,'bold'),bg="white",fg="black")
btn_1.grid(row=7, column=0)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=6, font=("Arial", 20,'bold'),bg="white",fg="black")
btn_2.grid(row=7, column=1)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=6, font=("Arial", 20,'bold'),bg="white",fg="black")
btn_3.grid(row=7, column=2)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=6, font=("Arial", 20,'bold'),bg="white",fg="black")
btn_4.grid(row=6, column=0)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=6, font=("Arial", 20,'bold'),bg="white",fg="black")
btn_5.grid(row=6, column=1)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=6, font=("Arial", 20,'bold'),bg="white",fg="black")
btn_6.grid(row=6, column=2)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=6, font=("Arial", 20,'bold'),bg="white",fg="black")
btn_7.grid(row=5, column=0)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=6, font=("Arial", 20,'bold'),bg="white",fg="black")
btn_8.grid(row=5, column=1)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=6, font=("Arial", 20,'bold'),bg="white",fg="black")
btn_9.grid(row=5, column=2)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=6, font=("Arial", 20,'bold'),bg="white",fg="black")
btn_0.grid(row=8, column=0)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=6, font=("Arial", 20,'bold'), bg="powderblue", fg="black")
btn_plus.grid(row=4, column=3)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=6, font=("Arial", 20,'bold'), bg="powderblue", fg="black")
btn_minus.grid(row=5, column=3)
btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=6, font=("Arial", 20,'bold'), bg="powderblue", fg="black")
btn_mul.grid(row=6, column=3)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=6, font=("Arial", 20,'bold'), bg="powderblue", fg="black")
btn_div.grid(row=7, column=3)
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=6, font=("Arial", 20,'bold'), bg="powderblue", fg="black")
btn_open.grid(row=9, column=0)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=6, font=("Arial", 20,'bold'), bg="powderblue", fg="black")
btn_close.grid(row=9, column=1)
btn_equals = tk.Button(root, text="=", command= evaluate_calculation, width=6, font=("Arial", 20,'bold'), bg="powderblue", fg="black")
btn_equals.grid(row=8, column=3)
btn_clear = tk.Button(root, text="AC", command= clear_field, width=6, font=("Arial", 20,'bold'), bg="powderblue", fg="black")
btn_clear.grid(row=4, column=1)
btn_Backspace = tk.Button(root, text="C", command=lambda: back_Space(), width=6, font=("Arial", 20,'bold'), bg="powderblue", fg="black")
btn_Backspace.grid(row= 4, column= 0)

btn_sqRoot = tk.Button(root, text="2√", command=lambda: add_to_calculation("2√"), width=6, font=("Arial", 20,'bold'), bg="powderblue", fg="black")
btn_sqRoot.grid(row= 5, column= 4)
btn_Root = tk.Button(root, text="√", command=lambda: add_to_calculation("√") , width=6, font=("Arial", 20,'bold'), bg="powderblue", fg="black")
btn_Root.grid(row=4, column= 2)
btn_power = tk.Button(root, text="x^", command=lambda: add_to_calculation("^"), width=6, font=("Arial",20,'bold') , bg="powderblue", fg="black")
btn_power.grid(row=7, column= 4)
btn_log = tk.Button(root, text="log", command=lambda: Log(), width=6, font=("Arial",20,'bold'), bg="powderblue", fg="black" )
btn_log.grid(row=9, column= 2)
btn_log10 = tk.Button(root, text="log10", command=lambda: Log10(), width=6, font=("Arial",20,'bold'), bg="powderblue", fg="black" )
btn_log10.grid(row=9, column= 3)
btn_fac = tk.Button(root, text="!", command=lambda: add_to_calculation("!"), width=6, font=("Arial",20,'bold'), bg="powderblue", fg="black" )
btn_fac.grid(row=9, column= 4)
btn_pi = tk.Button(root, text="π", command=lambda: add_to_calculation("π"), width=6, font=("Arial",20,'bold'), bg="powderblue", fg="black" )
btn_pi.grid(row=4, column= 4)
btn_e =  tk.Button(root, text="e", command=lambda: add_to_calculation("e"), width=6, font=("Arial",20,'bold'), bg="powderblue", fg="black" )
btn_e.grid(row=8, column= 4)
btn_dot = tk.Button(root, text= ".", command=lambda: add_to_calculation("."), width=6, font=("Arial",20,'bold'), bg="powderblue", fg="black")
btn_dot.grid(row=8, column= 1)
btn_rev = tk.Button(root, text="1/x", command=lambda: rev(), width=6, font=("Arial",20,'bold'), bg="powderblue", fg="black")
btn_rev.grid(row=6, column= 4)
btn_angl = tk.Button(root, text="Deg", command=lambda: measurement_unit(), width=6, font=("Arial",20,'bold'), bg="white", fg="black")
btn_angl.grid(row=3, column= 1)
btn_sign = tk.Button(root, text="+/-", command=lambda: change_sign(), width=6, font=("Arial", 20,'bold'), bg="powderblue", fg="black")
btn_sign.grid(row=8, column=2)

# Προσθήκη ετικέτας στο row 9
label_custom_text = tk.Label(root, text="ΠΛΗΠΡΟ-ΗΛΕ44", font=("Arial", 20,'bold'), bg="powderblue")
label_custom_text.grid(row=10, column=0, columnspan=6)



#menubutton
menu = tk.Menu(menubutton, tearoff=0)
menu.add_command(label="sin", command=lambda: Sin())
menu.add_command(label="cos", command=lambda: Cos())
menu.add_command(label="tan", command=lambda: Taaan())
menu.add_command(label="sinh", command=lambda: Sinh())
menu.add_command(label="cosh", command=lambda: Cosh())
menu.add_command(label="tanh", command=lambda: Tanh())

menubutton.config(menu=menu)
menubutton.grid(row=3)

#keys
key_1 = root.bind('1',lambda event: add_to_calculation(1))
key_2 = root.bind('2',lambda event: add_to_calculation(2))
key_3 = root.bind('3',lambda event: add_to_calculation(3))
key_4 = root.bind('4',lambda event: add_to_calculation(4))
key_5 = root.bind('5',lambda event: add_to_calculation(5))
key_6 = root.bind('6',lambda event: add_to_calculation(6))
key_7 = root.bind('7',lambda event: add_to_calculation(7))
key_8 = root.bind('8',lambda event: add_to_calculation(8))
key_9 = root.bind('9',lambda event: add_to_calculation(9))
key_0 = root.bind('0',lambda event: add_to_calculation(0))
key_plus = root.bind('+',lambda event: add_to_calculation('+'))
key_minus = root.bind('-', lambda event: add_to_calculation('-'))
key_mul = root.bind('*', lambda event: add_to_calculation('*'))
key_div = root.bind('/', lambda event: add_to_calculation('/'))
key_open = root.bind("(", lambda event: add_to_calculation("("))
key_close = root.bind(')', lambda event: add_to_calculation(')'))
key_equals = root.bind('=', lambda event: evaluate_calculation())
key_clear = root.bind('<Delete>', lambda event: clear_field())
key_baksp = root.bind('<BackSpace>', lambda event: back_Space())

root.mainloop()

