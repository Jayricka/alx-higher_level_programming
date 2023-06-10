Python - Import & Modules
In this project, the focus is on understanding and utilizing the concepts of importing functions and creating modules in Python. Additionally, there is practice in using the built-in function dir() and incorporating command line arguments in Python programs.

Tasks 📃
Task 0: Importing a Simple Function from a Simple File

File: 0-add.py
Description: This Python program imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3.
Output: <a value> + <b value> = <add(a, b) value> followed by a new line.
Task 1: My First Toolbox!

File: 1-calculation.py
Description: This Python program imports functions from the file calculator_1.py and prints the result of the addition, subtraction, multiplication, and division of 10 and 5.
Output: <a value> <operator> <b value> = <operation(a, b) value> followed by a new line.
Task 2: Making a Script Dynamic!

File: 2-args.py
Description: This Python program prints the number of arguments passed and lists all the arguments.
Output: [Number of arguments] argument (if the number is one) or arguments (otherwise), followed by:
: (or . if no arguments were passed), followed by
A new line, followed by
One argument per line - the position of the argument (starting at 1) followed by : followed by the argument value and another new line.
Task 3: Infinite Addition

File: 3-infinite_add.py
Description: This Python program prints the result of adding all the arguments.
Output: The sum of the arguments followed by a new line.
Task 4: Who Are You?

File: 4-hidden_discovery.py
Description: This Python program prints all the names defined by the compiled module hidden_4.pyc.
Output: One name per line in alphabetical order.
Names starting with __ are not printed.
Task 5: Everything Can Be Imported

File: 5-variable_load.py
Description: This Python program imports the variable a from the file variable_load_5.py and prints its value.
Task 6: Build My Own Calculator!

File: 100-my_calculator.py
Description: This Python program imports all functions from the file calculator_1.py and handles basic operations.
Usage: ./100-my_calculator.py <a> <operator> <b> followed by a new line.
Output: <a> <operator> <b> = <result> followed by a new line.
The parameter operator can be:
+ for addition
- for subtraction
* for multiplication
/ for division
If the operator is none of the above, the function prints `Unknown operator. Available
